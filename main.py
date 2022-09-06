from documento import Documento
from telefone import Telefone


cpf = "01234567890"
obj = Documento.cria_documento(cpf)
print('CPF: {}'.format(obj))

#cnpj = "58632487963521"     # inválido
cnpj = "45651750905709"  # válido
obj = Documento.cria_documento(cnpj)
print('CNPJ: {}'.format(obj))

telefone = '21336865329'
obj = Telefone(telefone)
print('TELEFONE: {}'.format(obj))
