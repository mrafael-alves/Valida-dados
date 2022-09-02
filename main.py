from cpf import Cpf
from cnpj import Cnpj

cpf = "01234567890"
obj = Cpf(cpf)
print(obj)

#cnpj = "58632487963521" # inválido
cnpj = "45651750905709" # válido
obj = Cnpj(cnpj)
print(cnpj)
