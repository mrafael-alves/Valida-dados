import re


class Telefone:
    def __init__(self, numero):
        numero = str(numero)

        if self.valida_tel(numero):
            self.numero = numero
        else:
            raise ValueError("Telefone inválido.")

    def valida_tel(self, numero):
        padrao = "[0-9]{2}[0-9]{4,5}[0-9]{4}"
        busca = re.search(padrao, numero)
        if busca:
            return True
        else:
            return False

    def formata_tel(self):
        if len(self.numero) == 11:
            return '({}){}-{}'.format(
                self.numero[:2],
                self.numero[2:7],
                self.numero[7:]
            )
        else:
            return '({}){}-{}'.format(
                self.numero[:2],
                self.numero[2:6],
                self.numero[6:]
            )

    def __str__(self):
        return self.formata_tel()