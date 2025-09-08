# Mesclando dois dicionários.

def unir_dicionarios (d1, d2):
    
    resultado = d1.copy ()
    resultado.update(d2)
    return resultado

dicionario1 = {"a": 1, "b": 2}
dicionario2 = {"b": 3, "c": 4}
resultado = unir_dicionarios(dicionario1, dicionario2)

print(resultado)