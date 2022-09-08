import re

padrao = '[0-9][a-z]{2}[0-9]'
texto = '123 1a2 1cc aa1 1bz9'

resposta = re.search(padrao, texto)
print(resposta.group())


padrao = "\w{5,50}@\w{3,10}.\w{2,3}.\w{2,3}"    # \w representa qualquer digito alfabético ou numérico
texto = "aaabbbcc rodrigo123@gmail.com.br"
resposta = re.search(padrao, texto)

print(resposta.group())


padrao_molde = "(xx)aaaa-wwww"
padrao = "[0-9]{2}[0-9]{4,5}[0-9]{4}"
texto = "eu gosto do numero 21264500910"
resposta = re.findall(padrao,texto)

if resposta:
    print(True)
else:
    print(False)

print(resposta)