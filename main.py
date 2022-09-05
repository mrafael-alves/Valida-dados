from cpf import Cpf
from cnpj import Cnpj
from telefone import Telefone

cpf = "01234567890"
obj = Cpf(cpf)
print('CPF: {}'.format(obj))

#cnpj = "58632487963521" # inválido
cnpj = "45651750905709" # válido
obj = Cnpj(cnpj)
print('CNPJ: {}'.format(obj))

telefone = '2133685798'
obj = Telefone(telefone)
print('TELEFONE: {}'.format(obj))


