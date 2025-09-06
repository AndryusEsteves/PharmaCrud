import os #limpa o terminal automaticamente

def show_menu(): #função principal
    while True:
        print("""
---------------------------
        PHARMACRUD
---------------------------              
1 - Cadastrar Medicamento
2 - Consultar Medicamento 
3 - Atualizar Medicamento
4 - Excluir   Medicamento
5 - Sair
---------------------------
              
""")
        opcao = input("Escolha uma opção: ") #input do usuário

        if opcao == "1":
            print("Chamando a função: cadastrar_medicamento()")
            # Futuramente, a linha acima será removida e esta será ativada:
            # cadastrar_medicamento()
        elif opcao == "2":
            print("Chamando a função: listar_medicamentos()")
            # Futuramente:
            # lista_medicamentos()
        elif opcao == "3":
            print("Chamando a função: atualizar_medicamento()")
            # Futuramente:
            # atualizar_medicamento()
        elif opcao == "4":
            print("Chamando a função: excluir_medicamento()")
            # Futuramente:
            # excluir_medicamento
        elif opcao == "5":
            print("Obrigado por usar o PharmaCRUD! Até logo.")
            break
        else:
            print("Opção inválida! Por favor, escolha um número de 1 a 5")
        
        input("\nPressione Enter para voltar ao menu...") # Linha de pausa
