banco = [
    {"nome":"Duna",
     "edicao": 5,
     "autor": "Frank Hebert",
     "isbn": "56764644",
     "editora":"Aleph"
     }
]

print (len(banco))

novo_item = {
    "id": len(banco)+1,
    "nome": "Duna",
    "edicao": 5,
    "autor": "Frank Hebert",
    "isbn": "56764644",
    "editora":"Aleph"
}

novo_item["nome"] = input("Digite o nome do livro: ")
novo_item["edicao"] = int(input("Digite a edição do livro: "))
novo_item["autor"] = input("Digite o autor do livro: ")
novo_item["isbn"] = input("Digite o ISBN do livro: ")
novo_item["editora"] = input("Digite a editora do livro: ")
