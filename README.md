<div align="center">
<img src="assets/MSpeechPy.png" alt="MSpeechPy-logo" width="200"/>

<i>Converter textos para voz usando Python!</i>  


![Versão](https://img.shields.io/badge/version-0.0.5-orange)
![Licença](https://img.shields.io/badge/license-MIT-orange)
[![Sponsor](https://img.shields.io/badge/💲Donate-yellow)](https://apoia.se/paulocesar-dev404)

</div>
    
  
---

## Funcionalidades

- Obter todas as vozes locais.
- Filtrar vozes por localidade.
- Listar vozes multilíngues.
- Obter detalhes de uma voz específica.
- Converter texto para áudio usando uma voz selecionada.

## Obter todas as vozes locais

```python
from MSpeechPy import SpeechpyClient

# Inicializa o cliente
engine = SpeechpyClient()

# Obter todas as vozes locais
voices = engine.get_voices.get_all_local_voices()  
print("Todas as vozes locais:")
for v in voices:
    print(v)
```

## Obter vozes por localidade

```python
from MSpeechPy import SpeechpyClient

engine = SpeechpyClient()

# Obter vozes por localidade
local = 'Portuguese (Brazil)'
voices_pt_br = engine.get_voices.filter_voices_by_locale_name(local)  
print(f"\nVozes para a localidade '{local}':")
for v in voices_pt_br:
    print(v)
```

## Obter vozes multilíngues

```python
from MSpeechPy import SpeechpyClient

engine = SpeechpyClient()

# Obter vozes multilíngues
voices_multilingual = engine.get_voices.get_all_multilingual()  
print("\nTodas as vozes multilíngues:")
for v in voices_multilingual:
    print(v)
```

## Obter detalhes de uma voz específica

```python
from MSpeechPy import SpeechpyClient

# Inicializa o cliente
engine = SpeechpyClient()

# Nome curto da voz
short_name = 'pt-BR-Daniel'

# Obtém as informações da voz pelo nome curto
voice_info = engine.get_voices.filter_voices_by_voice_name(short_name=short_name)

# Imprime os detalhes da voz
print(f"Voice Type: {voice_info.voice_type}")
print(f"Sample Rate Hertz: {voice_info.sample_rate_hertz}")
print(f"Name: {voice_info.name}")
print(f"Short Name: {voice_info.short_name}")
print(f"Status: {voice_info.status}")
print(f"Output Format: {voice_info.get_output_format}")
print(f"Display Name: {voice_info.display_name}")
print(f"Gender: {voice_info.gender}")
print(f"Locale Name: {voice_info.locale_name}")
print(f"Style List: {voice_info.style_list}")
print(f"Words Per Minute: {voice_info.words_per_minute}")
```

## Converter texto para voz usando uma voz

```python
import os
from MSpeechPy import SpeechpyClient

# Inicializa o cliente
engine = SpeechpyClient()

# Nome curto da voz
short_name = 'pt-BR-Daniel'

# Obtém as informações da voz pelo nome curto
voice_info = engine.get_voices.filter_voices_by_voice_name(short_name=short_name)

# Verifica se a voz foi encontrada
if not voice_info:
    print(f"Nenhuma voz encontrada com o nome curto '{short_name}'")
    exit()

# Texto para conversão
text = "Eu sou o Daniel e vou me livrar da maldição dizendo olá mundo!"

# Diretório de saída
out_dir = 'daniel_teste'
os.makedirs(out_dir, exist_ok=True)

try:
    # Converte o texto em áudio
    audio_file_path = engine.text_to_speech.text_to_speech(
        text=text,
        voice_name=short_name,
        output_name='daniel_helloWorld',  # Nome do arquivo
        volume='loud',  # Ajusta o volume da voz
        pitch='-50%',   # Adiciona o valor do pitch (tom de voz)
        output_format='audio-16khz-128kbitrate-mono-mp3',  # Formato de saída
        output_dir=out_dir,
        emphasis='strong'  # Adiciona ênfase
    )

    # Verifica se o arquivo foi gerado corretamente
    if os.path.exists(audio_file_path):
        print(f"Arquivo de áudio gerado com sucesso: {audio_file_path}")
    else:
        print("Falha ao gerar o arquivo de áudio.")
except Exception as e:
    print(f"Ocorreu um erro: {e}")
```

## Contribuições e Suporte

Se tiver dúvidas ou sugestões, abra uma [issue aqui](https://github.com/PauloCesar-dev404/youtube_analyzer/issues).

---



