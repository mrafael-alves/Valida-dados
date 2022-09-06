from validate_docbr import CPF

# Concrete Creator de Fatory Documento
class Cpf:
    def __init__(self, cpf):
        cpf = str(cpf)
        if self.valida_cpf(cpf):
            self.cpf = cpf
        else:
            raise ValueError("CPF inválido.")

    def valida_cpf(self, cpf):
            valido = CPF()
            return valido.validate(cpf)

    def formata_cpf(self):
        mascara = CPF()
        return mascara.mask(self.cpf)

    def __str__(self):
        return self.formata_cpf()