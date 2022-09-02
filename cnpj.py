from validate_docbr import CNPJ


class Cnpj:
    def __init__(self, cnpj):
        cnpj = str(cnpj)
        if self.valida_cnpj(cnpj):
            self.cnpj = cnpj
        else:
            raise ValueError("CNPJ inválido.")

    def valida_cnpj(self, cnpj):
        if len(cnpj) == 14:
            valido = CNPJ()
            return valido.validate(cnpj)
        else:
            raise ValueError("Deve conter 14 dígitos.")

    def formata_cnpj(self):
        mascara = CNPJ()
        return mascara.mask(self.cnpj)

    def __str__(self):
        return self.formata_cnpj()






