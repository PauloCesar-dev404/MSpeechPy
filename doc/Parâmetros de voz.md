# Resumo Detalhado dos Parâmetros para Conversão de Voz usando a Microsoft Azure Cognitive Services Speech API

### Tabela de `SampleRateHertz`

| **SampleRateHertz** | **Formatos de Áudio**                                          | **Descrição**                                                              |
|---------------------|---------------------------------------------------------------|----------------------------------------------------------------------------|
| 8000                | `riff-8khz-8bit-mono-mulaw`                                    | Formato de áudio de baixa qualidade, tipicamente usado em telefonia.        |
| 16000               | `riff-16khz-16bit-mono-pcm`, `audio-16khz-128kbitrate-mono-mp3` | Qualidade de áudio intermediária, adequada para aplicações de voz gerais.  |
| 24000               | `riff-24khz-16bit-mono-pcm`, `audio-24khz-96kbitrate-mono-mp3`  | Áudio de qualidade média a alta, ideal para aplicações digitais e streaming.|
| 48000               | `riff-48khz-16bit-mono-pcm`, `audio-48khz-192kbitrate-mono-mp3` | Alta qualidade de áudio, adequada para produções de áudio premium e gravações naturais.|

### Descrição dos Formatos

1. **PCM (Pulse Code Modulation)**:
   - **Exemplo**: `riff-16khz-16bit-mono-pcm`
   - Formato não comprimido que proporciona alta precisão e qualidade, amplamente utilizado em gravações de áudio e aplicações onde a fidelidade é essencial.

2. **MP3**:
   - **Exemplo**: `audio-24khz-96kbitrate-mono-mp3`
   - Formato comprimido que equilibra qualidade e tamanho do arquivo. Ideal para streaming e aplicações em que o tamanho do arquivo é uma preocupação.

3. **Mu-Law**:
   - **Exemplo**: `riff-8khz-8bit-mono-mulaw`
   - Formato de compressão de áudio que reduz a largura de banda necessária para transmissão de voz, frequentemente usado em telefonia e comunicação de voz.

### Outros Parâmetros

#### Velocidade de Fala (Rate)
   - **Descrição**: Ajusta a velocidade da fala, expressa em valores relativos (por exemplo, `fast`, `medium`, `slow`) ou em valores absolutos, dependendo da configuração.

#### Volume (Volume)
   - **Descrição**: Ajusta o volume da fala. Os valores típicos incluem:
     - `x-soft` - Extra suave
     - `soft` - Suave
     - `medium` - Médio
     - `loud` - Alto
     - `x-loud` - Extra alto

#### Tom (Pitch)
   - **Descrição**: Ajusta o tom da fala. O intervalo é geralmente de -100% a 100%, com valores mais altos resultando em uma voz mais aguda e valores mais baixos resultando em uma voz mais grave.

#### Ênfase (Emphasis)
   - **Valores**:
     - **`strong`** - Ênfase forte, destacando significativamente o texto.
     - **`moderate`** - Ênfase moderada, destacando o texto claramente, mas de forma equilibrada.
     - **`reduced`** - Ênfase reduzida, onde o texto é pronunciado com menor destaque.

#### Quebra de Frase (Break)
   - **Descrição**: Introduz pausas de duração específica entre palavras. As pausas podem ser especificadas em milissegundos (ms) ou como pausas curtas, médias ou longas.

### Valores Possíveis para `say-as`

- **`digits`** - Trata o texto como uma sequência de dígitos.
- **`date`** - Trata o texto como uma data, com formato especificado.
- **`time`** - Trata o texto como uma hora, com formato especificado.
- **`telephone`** - Trata o texto como um número de telefone.
- **`address`** - Trata o texto como um endereço.
- **`number`** - Trata o texto como um número.
- **`currency`** - Trata o texto como uma quantia monetária.
- **`spell-out`** - Trata o texto como uma sequência de caracteres a ser soletrada.

### Documentação Oficial

Para uma lista completa de regiões disponíveis para o serviço de voz, consulte a [documentação oficial](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/).

