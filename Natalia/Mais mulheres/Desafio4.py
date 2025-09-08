refeicoes = []

while True:
    print("\n1 - Adicionar alimento")
    print("2 - Ver total de calorias")
    print("3 - Ver histórico")
    print("4 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        nome = input("Nome do alimento: ")
        calorias = int(input("Calorias: "))
        refeicoes.append((nome, calorias))
        print("Alimento adicionado!")

    elif opcao == "2":
        total = sum(c for _, c in refeicoes)
        print(f"Total de calorias: {total}")

    elif opcao == "3":
        for nome, cal in refeicoes:
            print(f"{nome} - {cal} cal")

    elif opcao == "4":
        print("Tchau!")
        break

    else:
        print("Opção inválida.")