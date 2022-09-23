from cep import Cep

cep = 70835060
obj = Cep(cep)
print(obj)
print(obj.endereco_completo())
endereco, bairro, cidade, uf = obj.endereco_completo()
print(
    f'Endereço: {endereco}\nBairro: {bairro}\nCidade/UF: {cidade}/{uf}'
)


