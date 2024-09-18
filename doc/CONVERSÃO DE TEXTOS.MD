## Convertendo um Texto para Voz

Você pode converter seu texto em voz utilizando o método:

- **`text_to_speech`**: do objeto `SpeechText`.

Ou, se preferir, pode criar um SSML (Speech Synthesis Markup Language) usando o:

- **`SSMLBuilder`**: criador de SSML.

### Exemplo de Conversão Direta

```python
import MSpeechPy

client = MSpeechPy.SpeechpyClient()

output_f = 'audio-16khz-128kbitrate-mono-mp3'
antonio = 'pt-BR-AntonioNeural'

file = client.text_to_speech.text_to_speech(
    text="Ligue para o número 123456789. O evento será em 18/09/2024 às 15:30. O valor é de 100 dólares.",
    say_as=[
        "telephone",  # Interpretar como número de telefone
        "date",       # Interpretar como data
        "time",       # Interpretar como horário
        "currency"    # Interpretar como valor monetário
    ],
    voice_name=antonio,
    output_dir='daniel_teste',
    output_format=output_f,
    output_name='tst002',
    pitch='-30%'  # Ajustar tom de voz
)

if file:
    print(f"Salvo em {file}")
```

### Parâmetros Explicados

- **text**: O texto completo que será convertido em voz.
- **say_as**: Lista de interpretações para partes específicas do texto:
  - **'telephone'** — Para interpretar como número de telefone.
  - **'date'** — Para interpretar como data.
  - **'time'** — Para interpretar como horário.
  - **'currency'** — Para interpretar como valor monetário.
  - **'number'** — Para interpretar como número geral.
  - **'spell-out'** — Para interpretar como sequência de caracteres soletrada.
  - **'address'** — Para interpretar como endereço.
- **voice_name**: O nome curto da voz que será utilizada (ex.: `pt-BR-AntonioNeural`).
- **output_dir**: O diretório onde o arquivo de áudio será salvo.
- **output_format**: O formato do arquivo de saída (ex.: `'audio-16khz-128kbitrate-mono-mp3'`).
- **output_name**: O nome do arquivo de saída sem a extensão.
- **pitch**: Ajusta o tom de voz (ex.: '-30%' para diminuir o tom da fala).

---

## Gerando um SSML usando o `SSMLBuilder`

O **SSMLBuilder** é uma ferramenta poderosa para criar configurações avançadas de fala, como ajustar pausas, volumes, tons de voz e estilos. Aqui está como você pode gerar um SSML e convertê-lo para um arquivo de áudio.

### Exemplo de Uso do SSMLBuilder

sonsulte :[DOCUMENTAÇÃO SSML Builder](DOCUMENTAÇÃO%20SSMLBuilder.md)

```python
from MSpeechPy import SSMLBuilder, SpeechpyClient

client = SpeechpyClient()
builder = SSMLBuilder(lang="pt-BR")

# Adicionar uma voz
builder.add_voice(name="pt-BR-AntonioNeural")

# Adicionar elementos de voz
builder.add_voice_element(voice_index=0, text="Hoje o clima está ótimo,", volume="medium")
builder.add_silence(voice_index=0, silence_type="comma-exact", value="50ms")
builder.add_voice_element(voice_index=0, text=" perfeito para uma caminhada.")
builder.add_silence(voice_index=0, silence_type="Sentenceboundary", value="200ms")
builder.add_voice_element(voice_index=0, text="Depois, podemos tomar um café.")

# Gerar o SSML
ssml_output = builder.build()

# Converter o SSML em áudio
output_f = 'audio-16khz-128kbitrate-mono-mp3'
client.text_to_speech.set_ssml_format(
    output_name='versao_02',
    output_format=output_f,
    output_dir='daniel_teste',
    ssml=ssml_output
)
```

### Explicação do SSMLBuilder

- **add_voice(name)**: Adiciona uma voz ao SSML. Aqui, foi usada a voz `pt-BR-AntonioNeural`.
- **add_voice_element()**: Adiciona um trecho de fala com volume, tom ou ênfase definidos.
- **add_silence()**: Insere uma pausa com duração personalizada (ex.: `50ms`).
- **build()**: Gera o SSML final que pode ser usado para a síntese de voz.

### obtendo o audio passando uma string ssml
  Após criar um ssml ou usando o gerador da  biblioteca ou de outra maneira, você pode passar ao método `set_ssml_format`,se o ssml for válido será obtido um resultado em audio.

> Vc deve saber quais formatos,região e efeitos são suportados da voz escolhida e. seu ssml.

```python
from MSpeechPy import SpeechpyClient

client = SpeechpyClient()

ssml = """<speak version="1.0" xmlns="http://www.w3.org/2001/10/synthesis" 
            xmlns:mstts="https://www.w3.org/2001/mstts" xml:lang="pt-BR">
            <voice name="pt-BR-AntonioNeural" effect="default">
                <prosody volume="medium" rate="medium">Olá, como você está?</prosody>
                <mstts:silence type="Sentenceboundary" value="1s"/>
                <emphasis level="strong">Espero que esteja bem.</emphasis>
            </voice>
        </speak>"""

file = client.text_to_speech.set_ssml_format(ssml=ssml,
                                             output_dir='dir_testes',
                                             output_name='tst_001',
                                             output_format='audio-16khz-128kbitrate-mono-mp3'
                                             )
if file:
    print(f"criado em : {file}")
```
