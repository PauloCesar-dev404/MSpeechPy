from typing import Optional
from ..CONSTANTS import FORMATS


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


def get_say_as_tags(say_as: Optional[dict]) -> str:
    """
        Retorna as tags Say-as para o SSML.
        """
    if say_as is None:
        return ''

    tags = []
    for item in say_as:
        format_type, text = item, say_as[item]
        tags.append(f'<say-as interpret-as="{format_type}">{text}</say-as>')

    return ''.join(tags)


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


def build_ssml(text: str, voice_name: str, volume: str, rate: str, pitch: str, pause: Optional[str],
                emphasis: Optional[str], say_as: Optional[dict]) -> str:
    """
    Constrói o corpo da requisição SSML.
    """
    pause_tag = get_pause_tag(pause)
    emphasis_tag, end_emphasis_tag = get_emphasis_tags(emphasis)
    say_as_tags = get_say_as_tags(say_as)

    return f"""
    <speak version="1.0" xmlns="http://www.w3.org/2001/10/synthesis" xml:lang="en-US">
        <voice name="{voice_name}">
            <prosody volume="{volume}" rate="{rate}" pitch="{pitch}">
                {emphasis_tag}{say_as_tags}{text.replace(" ", f" {pause_tag} ")}{end_emphasis_tag}
            </prosody>
        </voice>
    </speak>
    """
