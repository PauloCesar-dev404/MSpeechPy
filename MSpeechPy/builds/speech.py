from typing import Optional
import os
import requests
from ..section.Auth import AuthMicrosoft
from ..exeptions import NetworkError
from .api import build_ssml, get_format

auth = AuthMicrosoft()


class SpeechText:
    def __init__(self):
        """
        Inicializa a classe SpeechText com um token de autenticação.
        """
        self.__token = auth.load_section()

    def text_to_speech(self, text: str,
                       voice_name: str,
                       output_name: str,
                       output_dir: str,
                       output_format: str,
                       region: str = 'westeurope',
                       volume: str = 'default',
                       rate: str = 'default',
                       pitch: str = 'default',
                       pause: Optional[str] = 'none',
                       emphasis: Optional[str] = None,
                       say_as: Optional[dict] = None) -> str:
        """
        Converte o texto em fala e salva o áudio em um arquivo.

        :param text: Texto a ser convertido em fala.
        :param voice_name: Nome da voz a ser usada.
        :param output_name: Nome do arquivo de saída.
        :param output_dir: Diretório onde o arquivo será salvo.
        :param output_format: Formato do arquivo de saída ('mp3', 'pcm').
        :param region: Região do endpoint da API.
        :param volume: Volume da fala ('default', 'loud', 'soft').
        :param rate: Taxa de fala ('default', 'fast', 'slow').
        :param pitch: Tom da fala ('default', 'high', 'low').
        :param pause: Pausa entre palavras ('none', 'short', 'medium', 'long' ou valor em milissegundos).
        :param emphasis: Ênfase na fala ('strong', 'moderate', 'reduced').
        :param say_as: Dicionário para marcação Say-as com formato e texto.
        :return: Caminho para o arquivo de áudio salvo.
        """
        endpoint = f'https://{region}.tts.speech.microsoft.com/cognitiveservices/v1'
        headers = {
            'Authorization': f'Bearer {self.__token}',
            'Content-Type': 'application/ssml+xml',
            'X-Microsoft-OutputFormat': output_format
        }

        # Montagem do SSML
        body = build_ssml(text, voice_name, volume, rate, pitch, pause, emphasis, say_as)

        try:
            response = requests.post(endpoint, headers=headers, data=body.encode('utf-8'))
            response.raise_for_status()

            file_extension = get_format(output_format)
            file_path = os.path.join(output_dir, f'{output_name}.{file_extension}')
            os.makedirs(output_dir, exist_ok=True)

            if os.path.exists(file_path):
                os.remove(file_path)

            with open(file_path, 'wb') as audio_file:
                audio_file.write(response.content)

            return file_path

        except requests.exceptions.RequestException as e:
            raise NetworkError(f"Erro ao chamar a API: {e}")
        except ValueError as e:
            raise NetworkError(f"Erro de valor: {e}")