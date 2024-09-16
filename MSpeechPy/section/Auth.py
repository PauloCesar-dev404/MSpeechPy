import os
import json
from datetime import datetime, timezone
from azure.identity import InteractiveBrowserCredential
from ..CONSTANTS import CONFIG_FILE


class AuthMicrosoft:
    """Classe para autenticação com a Microsoft Azure"""

    def __init__(self):
        self.__token = None
        self.__timestamp = None
        self.__load_config()

    def __load_config(self):
        """Carrega o token e a data de expiração do arquivo de configuração, se existir."""
        if os.path.exists(CONFIG_FILE):
            with open(CONFIG_FILE, 'r') as file:
                config = json.load(file)
                self.__token = config.get('token')
                self.__timestamp = config.get('timestamp', 0)

    def __save_config(self):
        """Salva o token e a data de expiração no arquivo de configuração."""
        with open(CONFIG_FILE, 'w') as file:
            json.dump({
                'token': self.__token,
                'timestamp': self.__timestamp
            }, file)

    def get_token_expiry_details(self):
        """
        Obtém o tempo restante até a expiração do token em minutos e segundos.

        Returns:
            dict: Um dicionário com o tempo restante em minutos e segundos.
        """
        if self.__timestamp is None:
            return {
                'valid': False,
                'minutes': 0,
                'seconds': 0
            }

        current_time = datetime.now(timezone.utc).timestamp()
        time_remaining = self.__timestamp - current_time

        if time_remaining < 0:
            return {
                'valid': False,
                'minutes': 0,
                'seconds': 0
            }

        minutes, seconds = divmod(time_remaining, 60)
        return {
            'valid': True,
            'minutes': int(minutes),
            'seconds': int(seconds)
        }

    def check_login(self):
        """Verifica se o usuário está logado e se o token é válido."""
        return self.__token is not None and self.get_token_expiry_details()['valid']

    def login(self):
        """Realiza o login do usuário e salva o token e sua data de expiração se necessário."""
        if self.check_login():
            return
        print("Realizando login...")
        ibc = InteractiveBrowserCredential()
        aadToken = ibc.get_token("https://cognitiveservices.azure.com/.default")

        self.__token = aadToken.token
        # Atualize a data de expiração conforme o timestamp de expiração retornado pela API
        self.__timestamp = aadToken.expires_on
        # Salve as variáveis de ambiente no arquivo de configuração
        self.__save_config()
        return self.__token

    def load_section(self):
        """retorna a seção do user seu token"""
        while True:
            if self.check_login():
                return self.__token
            else:
                self.login()
                continue



