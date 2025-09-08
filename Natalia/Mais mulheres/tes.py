# DESAFIO 4 - Sistema Alimentar

# Lista que armazenará os alimentos do dia
refeicoes = []

while True:
    print("\n=== MENU ===")
    print("1 - Adicionar alimento (nome, calorias)")
    print("2 - Registrar refeições do dia")
    print("3 - Ver total de calorias consumidas")
    print("4 - Ver histórico alimentar")
    print("5 - Sair")

    escolha = input("Escolha uma opção (1-5): ")

    if escolha == "1":
        nome = input("Nome do alimento: ")
        calorias = int(input("Calorias: "))
        refeicoes.append({"alimento": nome, "calorias": calorias})
        print(" Alimento adicionado com sucesso!")

    elif escolha == "2":
        if refeicoes:
            print("\n Refeições registradas hoje:")
            for item in refeicoes:
                print(f" {item['alimento']} - {item['calorias']} cal")
        else:
            print(" Nenhuma refeição registrada ainda.")

    elif escolha == "3":
        total = sum(item["calorias"] for item in refeicoes)
        print(f"\n Total de calorias consumidas: {total} cal")

    elif escolha == "4":
        print("\n Histórico alimentar:")
        for i, item in enumerate(refeicoes, start=1):
            print(f"{i}. {item['alimento']} - {item['calorias']} cal")

    elif escolha == "5":
        print(" Saindo do sistema. Até logo!")
        break

    else:
        print(" Opção inválida. Tente novamente.")
