# Dicionário com listas

dicionario_aluno = {
    "nome": "João",
    "nota": [8, 9, 7],
    "nome": "Maria",
    "nota": [10, 9, 8],
    "nome": "José",
    "nota": [6, 5, 7]
}

media_aluno = [
    sum(nota) / len(nota) for nome, nota in dicionario_aluno.items()    
]