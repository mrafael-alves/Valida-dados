import requests


class Cep:
    def __init__(self, cep):
        cep = str(cep)
        if self.valida_cep(cep):
            self.cep = cep
        else:
            raise ValueError("CEP inválido.")

    def __str__(self):
        return self.formata_cep()

    def valida_cep(self, cep):
        if len(cep) == 8:
            return True
        else:
            return False

    def formata_cep(self):
        return "{}-{}".format(self.cep[:5], self.cep[5:])

    def endereco_completo(self):
        url = 'https://viacep.com.br/ws/{}/json/'.format(self.cep)
        r = requests.get(url)
        saida = r.json()
        return (
            saida['logradouro'],
            saida['bairro'],
            saida['localidade'],
            saida['uf']
        )
