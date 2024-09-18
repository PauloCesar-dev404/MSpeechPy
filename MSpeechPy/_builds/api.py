import os
from typing import Optional, List
import requests
from azure.core.exceptions import HttpResponseError
from azure.identity import DefaultAzureCredential
from ..exeptions import NetworkError


def get_pause_tag(pause: Optional[str]) -> str:
    """
    Retorna a tag de pausa adequada para o SSML.
    """
    if isinstance(pause, int):
        return f'<break time="{pause}ms"/>'
    elif pause == 'short':
        return '<break time="300ms"/>'
    elif pause == 'medium':
        return '<break time="500ms"/>'
    elif pause == 'long':
        return '<break time="1000ms"/>'
    return ''


def get_emphasis_tags(emphasis: Optional[str]) -> tuple:
    """
    Retorna as tags de ênfase para o SSML.
    """
    if emphasis == 'strong':
        return '<emphasis level="strong">', '</emphasis>'
    elif emphasis == 'moderate':
        return '<emphasis level="moderate">', '</emphasis>'
    elif emphasis == 'reduced':
        return '<emphasis level="reduced">', '</emphasis>'
    return '', ''


def get_say_as_tags(types: Optional[List[str]]) -> str:
    """
    Gera as tags SSML 'say-as' a partir da lista de tipos fornecida.

    A lista deve conter tipos como:
    - 'time' - para tempo
    - 'telephone' - para número de telefone
    - 'address' - para endereço
    - 'number' - para número
    - 'currency' - para quantia monetária
    - 'spell-out' - para sequência de caracteres
    """
    if not types:
        return ""

    tags = []
    for type_ in types:
        if type_ == "time":
            tags.append('<say-as interpret-as="time"></say-as>')
        elif type_ == "telephone":
            tags.append(f'<say-as interpret-as="telephone"></say-as>')
        elif type_ == "address":
            tags.append(f'<say-as interpret-as="address"></say-as>')
        elif type_ == "number":
            tags.append(f'<say-as interpret-as="number"></say-as>')
        elif type_ == "currency":
            tags.append(f'<say-as interpret-as="currency"></say-as>')
        elif type_ == "spell-out":
            tags.append(f'<say-as interpret-as="spell-out"></say-as>')
        elif type_ == "date":
            tags.append(f'<say-as interpret-as="date"></say-as>')

        else:
            raise ValueError(f"Tipo de 'say-as' desconhecido: {type_}")
    return ''.join(tags)


def build_ssml(text: str,
               voice_name: str,
               volume: str,
               rate: str,
               pitch: str,
               pause: Optional[str],
               say_as: Optional[dict]) -> str:
    """
    Constrói o corpo da requisição SSML.
    """
    pause_tag = get_pause_tag(pause)
    say_as_tags = get_say_as_tags(say_as)

    return f"""
    <speak version="1.0" xmlns="http://www.w3.org/2001/10/synthesis" xml:lang="en-US">
        <voice name="{voice_name}">
            <prosody volume="{volume}" rate="{rate}" pitch="{pitch}">
              {say_as_tags}{text.replace(" ", f" {pause_tag} ")}
            </prosody>
        </voice>
    </speak>
    """


def get_format(output_format: str) -> str:
    """
    Determina a extensão do arquivo com base no formato de saída.
    """
    if 'mp3' in output_format:
        return 'mp3'
    elif 'pcm' in output_format:
        return 'wav'
    else:
        raise ValueError("Formato de saída não suportado")


def get_access_token():
    """Obtém um token de acesso, chamando o callback quando um novo token é obtido."""
    credential = DefaultAzureCredential()
    try:
        token = credential.get_token("https://cognitiveservices.azure.com/.default")
        return token.token
    except HttpResponseError as e:
        raise ConnectionError(f"Erro ao obter o token: {e}")


def get_ssml(output_name,
             output_format: str,
             output_dir: str,
             ssml: str,
             region_api: str = 'westeurope'):
    """realizar uma requisição com o seu ssml"""
    endpoint = f'https://{region_api}.tts.speech.microsoft.com/cognitiveservices/v1'
    headers = {
        'Authorization': f'Bearer {get_access_token()}',
        'Content-Type': 'application/ssml+xml',
        'X-Microsoft-OutputFormat': output_format
    }
    # corpo do SSML
    body = ssml
    try:
        response = requests.post(endpoint, headers=headers, data=body.encode('utf-8'))
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
