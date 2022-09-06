from validate_docbr import CNPJ

# Concrete Creator de Fatory Documento
class Cnpj:
    def __init__(self, cnpj):
        cnpj = str(cnpj)
        if self.valida_cnpj(cnpj):
            self.cnpj = cnpj
        else:
            raise ValueError("CNPJ inválido.")

    def valida_cnpj(self, cnpj):
            valido = CNPJ()
            return valido.validate(cnpj)

    def formata_cnpj(self):
        objeto = CNPJ()
        return objeto.mask(self.cnpj)

    def __str__(self):
        return self.formata_cnpj()



