import re


class Telefone:
    def __init__(self, numero):
        numero = str(numero)

        if self.valida_tel(numero):
            self.numero = numero
        else:
            raise ValueError("Telefone inválido.")

    def __str__(self):
        return self.formata_tel()

    def valida_tel(self, numero):
        # Formato: iii (ddd) xxxx - wwwww
        padrao = "([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
        busca = re.findall(padrao, numero)
        if busca:
            return True
        else:
            return False

    def formata_tel(self):
        padrao = "([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
        busca = re.search(padrao, self.numero)
        return "+{}({}){}-{}".format(
            busca.group(1),
            busca.group(2),
            busca.group(3),
            busca.group(4)
        )