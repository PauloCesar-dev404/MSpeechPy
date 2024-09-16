class MSpeechPyExeptions(Exception):
    def __init__(self, message: str):
        super().__init__(message)

    def __str__(self):
        """
        Retorna a representação em string da exceção.

        Returns:
            str: Mensagem de erro formatada com detalhes adicionais, se presentes.
        """

        return super().__str__()


######## AUTH ERROS

class AuthError(MSpeechPyExeptions):
    def __init__(self, message: str):
        super().__init__(message)

    def __str__(self):
        """
        Retorna a representação em string da exceção.

        Returns:
            str: Mensagem de erro formatada com detalhes adicionais, se presentes.
        """

        return super().__str__()


class NotSectionActive(MSpeechPyExeptions):
    """quando o usuario não tem uma seção ativa..."""

    def __init__(self, message: str):
        super().__init__(message)

    def __str__(self):
        """
        Retorna a representação em string da exceção.

        Returns:
            str: Mensagem de erro formatada com detalhes adicionais, se presentes.
        """

        return super().__str__()


### network

class NetworkError(MSpeechPyExeptions):
    """rede."""

    def __init__(self, message: str):
        super().__init__(message)

    def __str__(self):
        """
        Retorna a representação em string da exceção.

        Returns:
            str: Mensagem de erro formatada com detalhes adicionais, se presentes.
        """

        return super().__str__()

class MaxrequestsError(MSpeechPyExeptions):
    """rede."""

    def __init__(self, message: str):
        super().__init__(message)

    def __str__(self):
        """
        Retorna a representação em string da exceção.

        Returns:
            str: Mensagem de erro formatada com detalhes adicionais, se presentes.
        """

        return super().__str__()
