#### Configuração Inicial

Antes de começar a utilizar a biblioteca `MSpeechPy`, você precisa configurar uma instância do cliente.

**Criação da Instância do Cliente**

   Em seu script Python, importe a classe `SpeechpyClient` e crie uma instância do cliente:

   ```python
from MSpeechPy import SpeechpyClient

client = SpeechpyClient()
```

**Autenticação**

Na primeira execução do código, será solicitado que você entre no site de autenticação e conceda permissão ao `Microsoft Azure Cross-platform Command Line Interface`. Siga as instruções abaixo:

   - **Abra o link fornecido** em seu console para autenticação.
   - **Digite o código** exibido no console no site de autenticação.
   - **Conclua o processo de autenticação** com sua conta Microsoft.

Após a autenticação bem-sucedida,sua aplicação estará autorizado a interagir com a API de Sitesi de Voz da Microsoft usando a `MSpeechPy`.

## obter tokens de seção 
caso voc queria moitorar os seus tokens de seçã utilizize a funcao `authenticate`
onde ela sempre retrna seu token de seçãoo atual


```python
from MSpeechPy import authenticate
```

