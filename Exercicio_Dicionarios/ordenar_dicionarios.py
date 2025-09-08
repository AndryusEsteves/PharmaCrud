#Ordenando dicionário por valor

pontuacoes = {"João": 50, "Maria": 80, "Pedro": 70}

ordenado = []

itens = list(pontuacoes.items())

while itens:

    maior = itens[0]
    for item in itens:
        if item[1] > maior[1]:
            maior = item
    
    ordenado.append(maior)
    
    itens.remove(maior)

ordenado_dict = dict(ordenado)
print(ordenado_dict)
