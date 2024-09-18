import requests


class SpeechpyClient:
    @property
    def get_voices(self):
        from ._builds import get_access_token
        from ._builds import Voices
        # Endpoint da API para obter a lista de vozes
        endpoint = 'https://westeurope.tts.speech.microsoft.com/cognitiveservices/voices/list'

        # Cabeçalhos para a requisição
        headers = {
            'Authorization': f'Bearer {get_access_token()}',
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
    def text_to_speech(self):
        from ._builds import SpeechText
        """converter texto para voz"""
        v = SpeechText()
        return v


def authenticate():
    """obter o token de seção atual"""
    from ._builds.api import get_access_token
    return get_access_token()
