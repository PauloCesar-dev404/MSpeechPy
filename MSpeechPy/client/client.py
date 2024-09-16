import requests
from ..builds.voices import Voices
from ..builds.speech import SpeechText

from ..section.Auth import AuthMicrosoft

auth = AuthMicrosoft()


class SpeechpyClient:
    def __init__(self):
        self.__token = auth.load_section()

    @property
    def get_voices(self) -> Voices:
        # Endpoint da API para obter a lista de vozes
        endpoint = 'https://westeurope.tts.speech.microsoft.com/cognitiveservices/voices/list'  # Substitua 'westeurope' pela sua região

        # Cabeçalhos para a requisição
        headers = {
            'Authorization': f'Bearer {self.__token}',
            'Content-Type': 'application/ssml+xml'
        }

        # Enviar requisição GET para a API
        response = requests.get(endpoint, headers=headers)
        response.raise_for_status()  # Levanta um erro se a requisição falhar

        # Parsear a resposta JSON
        voices = response.json()
        vc = Voices(voices=voices)
        return vc

    @property
    def text_to_speech(self) -> SpeechText:
        """converter texto para voz"""
        v = SpeechText()
        return v
