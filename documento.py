from cpf import Cpf
from cnpj import Cnpj

# Factory Method
class Documento:
     @staticmethod
     def cria_documento(documento):
        documento = str(documento)

        if len(documento) == 11:
            return Cpf(documento)
        if len(documento) == 14:
            return Cnpj(documento)
        else:
            raise ValueError("Quantidade dígitos inválido.")