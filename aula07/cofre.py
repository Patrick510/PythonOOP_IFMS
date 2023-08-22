class SecretString:
    """Uma maneira não muito segura de armazenar uma string secreta."""
 
    def __init__(self, string_normal, senha):
        self.__string_normal = string_normal
        self.__senha = senha
 
    def descriptografar(self, senha):
        """Somente mostra a string se a senha estiver correta."""
        if senha == self.__senha:
            return self.__string_normal
        else:
            return ""