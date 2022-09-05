

class Telefone:
    def __init__(self, numero):
        numero = str(numero)
        if self.valida_tel(numero):
            self.numero = numero
        else:
            raise ValueError("Telefone inválido.")

    def valida_tel(self, numero):
        if len(numero) == 10 | len(numero) == 11:
            return True
        else:
            raise ValueError("Deve conter 10 ou 11 dígitos.")

    def formata_tel(self):
        return "({}){}-{}".format(
            self.numero[:2],
            self.numero[2:7],
            self.numero[7:]
        )

    def __str__(self):
        return self.formata_tel()


