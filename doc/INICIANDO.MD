#### Obter Todos Idiomas de Vozes

obtém todos os idiomas de vozes disponíveis

```python
import time
import MSpeechPy

client = MSpeechPy.SpeechpyClient()
voices = client.get_voices.get_all_local_voices()
for v in voices:
    print(v)
    time.sleep(1)
```

#### Obter Todas as Vozes de um Idioma Específico

Este código filtra e obtém todas as vozes disponíveis para um idioma específico, no exemplo, "Portuguese (Brazil)":

```python
import time
import MSpeechPy

client = MSpeechPy.SpeechpyClient()
voices_pt_br = client.get_voices.filter_voices_by_locale_name(locale_name='Portuguese (Brazil)')
for v in voices_pt_br:
    print(v)
    time.sleep(0.3)
```

#### Obter Todas as Vozes Multilíngues

Este código obtém todas as vozes multilíngues disponíveis:

```python
import time
import MSpeechPy

client = MSpeechPy.SpeechpyClient()
voices_multilingual = client.get_voices.get_all_multilingual()
for v in voices_multilingual:
    print(v)
    time.sleep(0.3)
```

#### Obter Detalhes de uma Voz Específica

Este código obtém e imprime detalhes de uma voz específica, no exemplo, "pt-BR-Daniel":

```python
import MSpeechPy

client = MSpeechPy.SpeechpyClient()
voices_pt_br_daniel = client.get_voices.filter_voices_by_voice_name(short_name='pt-BR-Daniel')
print("Tipo:", voices_pt_br_daniel.voice_type)
print("Sample Hertz:", voices_pt_br_daniel.sample_rate_hertz)
print("Nome curto:", voices_pt_br_daniel.short_name)
print("Nome:", voices_pt_br_daniel.name)
print("Gênero:", voices_pt_br_daniel.gender)
print("Palavras por minuto:", voices_pt_br_daniel.words_per_minute)
print("Estilos aplicáveis:", voices_pt_br_daniel.style_list)
print("Formato de saída suportado:", voices_pt_br_daniel.get_output_format)
print("Status:", voices_pt_br_daniel.status)
```

