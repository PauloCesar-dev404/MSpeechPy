# Resumo detalhado dos parâmetros para conversão de voz usando a Microsoft Azure Cognitive Services Speech API


### Tabela de `SampleRateHertz`

| **SampleRateHertz** | **Formatos de Áudio**                                  | **Descrição**                                                              |
|---------------------|--------------------------------------------------------|----------------------------------------------------------------------------|
| 8000                | `riff-8khz-8bit-mono-mulaw`                            | Formato de áudio de baixa qualidade (telefone).                            |
| 16000               | `riff-16khz-16bit-mono-pcm`, `audio-16khz-128kbitrate-mono-mp3` | Qualidade de áudio intermediária, usada para propósitos comuns de voz.     |
| 24000               | `riff-24khz-16bit-mono-pcm`, `audio-24khz-96kbitrate-mono-mp3`  | Áudio de qualidade média a alta, com uso em aplicações digitais.           |
| 48000               | `riff-48khz-16bit-mono-pcm`, `audio-48khz-192kbitrate-mono-mp3` | Alta qualidade de áudio, adequada para vozes naturais em áudio premium.    |

### Descrição dos Formatos:

1. **PCM (Pulse Code Modulation)**:
   - **Exemplo**: `riff-16khz-16bit-mono-pcm`
   - Formato PCM em 16-bit mono, usado amplamente em gravação de voz e aplicações de áudio de qualidade.
   - Alta precisão, usado para voz e áudio de maior fidelidade.

2. **MP3**:
   - **Exemplo**: `audio-24khz-96kbitrate-mono-mp3`
   - Formato comprimido de áudio, adequado para streaming e aplicações em que é necessário um equilíbrio entre qualidade e tamanho do arquivo.

3. **Mu-Law**:
   - **Exemplo**: `riff-8khz-8bit-mono-mulaw`
   - Formato de áudio de baixa qualidade, geralmente usado em comunicações de voz como telefonia.

### Outros Parâmetros

#### Velocidade de Fala (Rate)
   - Ajusta a velocidade da fala. Pode ser definido em valores relativos ou absolutos, dependendo da implementação.

#### Volume (Volume)
   - Ajusta o volume da fala. Valores comuns incluem: `x-soft`, `soft`, `medium`, `loud`, `x-loud`.

#### Tom (Pitch)
   - Ajusta o tom da fala. O intervalo é geralmente de -100% a 100%, onde valores mais altos tornam a voz mais aguda e valores mais baixos a tornam mais grave.

#### Ênfase (Emphasis)
   - **`strong`** - Ênfase forte, destacando significativamente o texto.
   - **`moderate`** - Ênfase moderada, destacando o texto de forma clara, mas não excessiva.
   - **`reduced`** - Ênfase reduzida, onde o texto é pronunciado com menor destaque.

#### Quebra de Frase (Break)
   - Introduz pausas de duração específica entre palavras. Pode ser especificado em milissegundos (ms) ou como pausas curtas, médias ou longas.

### Valores Possíveis para `say-as`

- **`digits`** - Trata o texto como uma sequência de dígitos.
- **`date`** - Trata o texto como uma data, com formato especificado.
- **`time`** - Trata o texto como uma hora, com formato especificado.
- **`telephone`** - Trata o texto como um número de telefone.
- **`address`** - Trata o texto como um endereço.
- **`number`** - Trata o texto como um número.
- **`currency`** - Trata o texto como uma quantia monetária.
- **`spell-out`** - Trata o texto como uma sequência de caracteres a ser soletrada.

### documentação oficial

Para uma lista completa de regiões disponíveis para o serviço de voz, consulte o [link da documentação oficial](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/)

