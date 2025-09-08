# Verificando existência de uma chave.

dicionario_contato = {
    "Nome": "Ana",
    "E-mail": "ana@email.com",
}

if "Telefone" in dicionario_contato:
    print("Telefone:" , dicionario_contato ["Telefone"])
else:
    print("Telefone não está presente.")