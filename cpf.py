class Cpf:
    def __init__(self, cpf):
        cpf = str(cpf)
        if self.valida_tamanho(cpf):
            self.cpf = cpf
        else:
            raise ValueError("CPF é inválido!")

    def valida_tamanho(self, cpf):
        if len(cpf) == 11:
            return True
        else:
            return False

    def formata_cpf(self):
        return (
            '{}.{}.{}-{}'.format(
                self.cpf[:3],
                self.cpf[3:6],
                self.cpf[6:9],
                self.cpf[9:]
            )
        )

    def __str__(self):
        return self.formata_cpf()
