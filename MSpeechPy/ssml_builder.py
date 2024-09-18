# ------------------------------------
# Copyright (c) PauloCesar-dev404.
# Licensed under the MIT License.
#
# create ssml usinhg this class
# version: 0.1
# refe: https://learn.microsoft.com/pt-br/azure/ai-services/speech-service/speech-synthesis-markup-structure
#
# ------------------------------------

from typing import List, Dict, Optional


class SSMLBuilder:
    def __init__(self, lang: str = "en-US"):
        """
        Inicializa o construtor SSML com idioma padrão e configurações vazias.
        :param lang: Código do idioma para o SSML.
        """
        self.lang = lang
        self.voices: List[Dict[str, str]] = []

    def add_voice(self, name: str, effect: str = "default"):
        """
        Adiciona um novo bloco de voz.
        :param name: Nome da voz.
        :param effect: Efeito da voz.
        """
        self.voices.append({
            "name": name,
            "effect": effect,
            "elements": []
        })

    def add_voice_element(self, voice_index: int, text: str, volume: Optional[str] = None, rate: Optional[str] = None,
                          pitch: Optional[str] = None, time: Optional[str] = None):
        """
        Adiciona elementos ao bloco de voz especificado com opções de prosódia, volume, taxa, tom e tempo.
        :param voice_index: Índice do bloco de voz onde adicionar o elemento.
        :param text: Texto a ser incluído.
        :param volume: Volume da fala (opcional).
        :param rate: Taxa da fala (opcional).
        :param pitch: Tom da fala (opcional).
        :param time: Tempo de pausa (opcional).
        """
        if voice_index >= len(self.voices):
            raise IndexError("Índice de voz fora do intervalo")

        # Cria a tag de prosódia, se necessário
        prosody_attributes = []
        if volume:
            prosody_attributes.append(f'volume="{volume}"')
        if rate:
            prosody_attributes.append(f'rate="{rate}"')
        if pitch:
            prosody_attributes.append(f'pitch="{pitch}"')

        prosody_tag = f'<prosody {" ".join(prosody_attributes)}>' if prosody_attributes else ''
        prosody_end_tag = '</prosody>' if prosody_attributes else ''

        # Adiciona o texto com a possível pausa
        text_with_pause = text
        if time:
            text_with_pause = f'<break time="{time}"/> {text_with_pause}'

        # Adiciona o elemento ao bloco de voz
        self.voices[voice_index]["elements"].append(f"{prosody_tag}{text_with_pause}{prosody_end_tag}")

    def add_silence(self, voice_index: int, silence_type: str, value: str):
        """
        Adiciona um elemento de silêncio ao bloco de voz.
        :param voice_index: Índice do bloco de voz onde adicionar o silêncio.
        :param silence_type: Tipo de silêncio a ser inserido (Sentenceboundary, Leading, etc.).
        :param value: Duração do silêncio (ex: '200ms').
        """
        if voice_index >= len(self.voices):
            raise IndexError("Índice de voz fora do intervalo")

        # Adiciona o silêncio como elemento da voz
        silence_element = f'<mstts:silence type="{silence_type}" value="{value}"/>'
        self.voices[voice_index]["elements"].append(silence_element)

    def add_emphasis(self, voice_index: int, text: str, level: str = "moderate"):
        self.voices[voice_index]["elements"].append(f'<emphasis level="{level}">{text}</emphasis>')

    def add_phoneme(self, voice_index: int, text: str, alphabet: str, ph: str):
        self.voices[voice_index]["elements"].append(f'<phoneme alphabet="{alphabet}" ph="{ph}">{text}</phoneme>')

    def add_say_as(self, voice_index: int, text: str, interpret_as: str, format: Optional[str] = None):
        if format:
            self.voices[voice_index]["elements"].append(
                f'<say-as interpret-as="{interpret_as}" format="{format}">{text}</say-as>')
        else:
            self.voices[voice_index]["elements"].append(f'<say-as interpret-as="{interpret_as}">{text}</say-as>')

    def add_express_as(self, voice_index: int, style: str, styledegree: Optional[str] = None,
                       role: Optional[str] = None):
        express_attributes = [f'style="{style}"']
        if styledegree:
            express_attributes.append(f'styledegree="{styledegree}"')
        if role:
            express_attributes.append(f'role="{role}"')

        self.voices[voice_index]["elements"].append(f'<mstts:express-as {" ".join(express_attributes)}>')

    def add_audio(self, voice_index: int, src: str, fallback_text: Optional[str] = None,
                  inner_elements: Optional[List[str]] = None):
        """
        Adiciona o elemento <audio> com suporte a fallback de texto e elementos SSML aninhados.

        :param voice_index: O índice da voz no documento SSML.
        :param src: O caminho ou URL do arquivo de áudio.
        :param fallback_text: Texto de fallback que será falado se o áudio não puder ser reproduzido.
        :param inner_elements: Lista de elementos SSML aninhados (como <break>, <prosody>, etc.).
        """
        # Elementos internos (como <break>, <prosody>, etc.)
        inner_content = ""

        if inner_elements:
            inner_content = " ".join(inner_elements)

        # Texto de fallback que será falado se o áudio não for reproduzido
        if fallback_text:
            audio_element = f'<audio src="{src}">{fallback_text} {inner_content}</audio>'
        else:
            audio_element = f'<audio src="{src}">{inner_content}</audio>'

        self.voices[voice_index]["elements"].append(audio_element)

    def build(self) -> str:
        """
        Constrói e retorna o SSML completo.
        """
        voices_tags = '\n'.join(
            f'''
            <voice name="{voice["name"]}" effect="{voice["effect"]}">
                {"\n".join(voice["elements"])}
            </voice>
            '''
            for voice in self.voices
        )

        return f"""
        <speak version="1.0" xmlns="http://www.w3.org/2001/10/synthesis" 
            xmlns:mstts="https://www.w3.org/2001/mstts" xml:lang="{self.lang}">
            {voices_tags}
        </speak>
        """
