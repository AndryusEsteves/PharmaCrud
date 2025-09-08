# Contando frequência de palavras

palavras_dicionario = [
    "maçã",
    "banana",
    "maçã",
    "laranja",
    "banana",
    "maçã"
]

frequencia = {}

for palavra in palavras_dicionario:
    if palavra in frequencia:
        frequencia[palavra] += 1
    else:
        frequencia[palavra] = 1

print(frequencia)