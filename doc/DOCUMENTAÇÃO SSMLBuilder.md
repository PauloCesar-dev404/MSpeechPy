# Documentação: Como Usar a Classe `SSMLBuilder`

## Visão Geral

A classe `SSMLBuilder` foi projetada para ajudar na criação de documentos SSML (Speech Synthesis Markup Language) de forma simples e estruturada. O SSML é usado para gerar conteúdo de fala em aplicativos como serviços de síntese de voz. Esta documentação detalha como usar a classe para gerar SSML passo a passo.

### Requisitos
- Conhecimento básico de SSML e seus componentes.
- Familiaridade com a API de síntese de voz da Microsoft (opcional, mas recomendável [consute a documentação](https://learn.microsoft.com/pt-br/azure/ai-services/speech-service/speech-synthesis-markup-structure)) 


## Inicialização da Classe

### Passo 1: Criando uma Instância

O primeiro passo é criar uma instância da classe `SSMLBuilder`. A classe aceita um parâmetro opcional `lang`, que define o idioma do documento SSML. O valor padrão é "en-US" (Inglês - Estados Unidos).

```python
from ssml_builder import SSMLBuilder

# Criando uma instância com o idioma padrão
ssml = SSMLBuilder()

# Criando uma instância com outro idioma (ex: Português - Brasil)
ssml = SSMLBuilder(lang="pt-BR")
```

## Passo 2: Adicionando Blocos de Voz

Para adicionar uma voz ao documento SSML, use o método `add_voice`. Você pode definir o nome da voz e um efeito opcional.

```python
# Adicionando uma voz com nome específico e efeito padrão
ssml.add_voice(name="Microsoft-AriaNeural")

# Adicionando uma voz com um efeito especial
ssml.add_voice(name="Microsoft-JennyNeural", effect="whisper")
```

## Passo 3: Adicionando Elementos de Voz

Uma vez que a voz é criada, você pode adicionar elementos de texto, controlar volume, velocidade, tom e pausas. Use o método `add_voice_element` para isso.

### Exemplo:
```python
# Adicionando um texto com volume e taxa de fala personalizados
ssml.add_voice_element(voice_index=0, text="Olá, seja bem-vindo.", volume="loud", rate="medium", pitch="high")

# Adicionando uma pausa de 500ms antes do texto
ssml.add_voice_element(voice_index=0, text="Como posso ajudar?", time="500ms")
```

### Personalização de Prosódia:
- `volume`: Define o volume da fala (ex: "x-loud", "soft").
- `rate`: Define a velocidade da fala (ex: "slow", "fast").
- `pitch`: Define o tom da fala (ex: "low", "high").
- `time`: Define pausas em milissegundos (ex: "500ms").

## Passo 4: Adicionando Silêncio

Para adicionar um silêncio personalizado, utilize o método `add_silence`. Você pode definir o tipo de silêncio e a duração.

```python
# Adicionando um silêncio de 200ms após uma frase
ssml.add_silence(voice_index=0, silence_type="Sentenceboundary", value="200ms")
```

## Passo 5: Adicionando Outros Elementos SSML

### Ênfase

Você pode adicionar ênfase às palavras com o método `add_emphasis`.

```python
# Adicionando ênfase moderada a uma palavra
ssml.add_emphasis(voice_index=0, text="incrível", level="strong")
```

### Fonemas

Para melhorar a pronúncia, você pode usar o método `add_phoneme`, especificando o alfabeto fonético e a pronúncia.

```python
# Adicionando fonema para uma palavra
ssml.add_phoneme(voice_index=0, text="Python", alphabet="ipa", ph="ˈpaɪθɑn")
```

### Formatação de Expressão

Para adicionar um estilo de expressão específico (como "news" ou "cheerful"), use o método `add_express_as`.

```python
# Adicionando estilo de fala
ssml.add_express_as(voice_index=0, style="cheerful")
```

### Formatação de Texto com Say-as

O método `add_say_as` permite que você formate a maneira como o texto será interpretado, como números ou data.

```python
# Interpretando um número como cardinal
ssml.add_say_as(voice_index=0, text="1234", interpret_as="cardinal")
```

## Passo 6: Adicionando Áudio

O método `add_audio` permite adicionar um arquivo de áudio externo ao documento SSML.

```python
# Adicionando um arquivo de áudio com fallback de texto
ssml.add_audio(voice_index=0, src="https://example.com/audio.mp3", fallback_text="Áudio não disponível.")
```

## Passo 7: Gerando o Documento SSML

Depois de configurar todas as vozes e elementos, você pode gerar o documento SSML final usando o método `build`.

```python
# Gerando o SSML completo
ssml_document = ssml.build()

# Exibindo o SSML gerado
print(ssml_document)
```

### Exemplo Completo

```python
ssml = SSMLBuilder(lang="en-US")
ssml.add_voice(name="Microsoft-AriaNeural")
ssml.add_voice_element(voice_index=0, text="Hello, welcome to our service.", rate="slow")
ssml.add_silence(voice_index=0, silence_type="Sentenceboundary", value="500ms")
ssml.add_voice_element(voice_index=0, text="How can I assist you today?", volume="loud")
ssml_document = ssml.build()

print(ssml_document)
```

## Conclusão

A classe `SSMLBuilder` fornece uma maneira eficiente e flexível de gerar documentos SSML personalizados, permitindo o controle detalhado sobre prosódia, ênfase, pausas e até mesmo a inclusão de elementos multimídia como áudio. 

Explore as várias opções de personalização e veja como é fácil criar vozes dinâmicas e envolventes para seu aplicativo de síntese de voz.
