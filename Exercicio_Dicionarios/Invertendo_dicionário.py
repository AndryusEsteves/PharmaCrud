# Invertendo um dicionário.

d = {"a": 1, "b": 2, "c": 3}
inverted_d = {}
for chave, valor in d.items():
    inverted_d[valor] = chave
    
    print(inverted_d)