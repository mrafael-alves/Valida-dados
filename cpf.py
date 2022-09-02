from validate_docbr import CPF

class Cpf:
    def __init__(self, cpf):
        cpf = str(cpf)
        if self.valida_cpf(cpf):
            self.cpf = cpf
        else:
            raise ValueError("CPF é inválido!")

    def valida_cpf(self, cpf):
        if len(cpf) == 11:
            valido = CPF()
            return valido.validate(cpf)
        else:
            raise ValueError('Quantidade de dígitos é inválida.')

    def formata_cpf(self):
        mascara = CPF()
        return mascara.mask(self.cpf)

    def __str__(self):
        return self.formata_cpf()
