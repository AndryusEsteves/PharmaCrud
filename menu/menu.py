import os #limpa o terminal automaticamente
import time
from crud.update import escolher_opcao
from colorama import init, Fore, Style
init(autoreset=True)

def show_menu():
    while True:
        # 1. Limpa a tela 
        os.system('cls' if os.name == 'nt' else 'clear')

        # 2. Define a largura e formata os textos para o "Box Art"
        largura = 50
        titulo_texto = "P H A R M A C R U D"
        titulo_centralizado = titulo_texto.center(largura - 2)
        
        opcao1 = "1 - Cadastrar Medicamento".ljust(largura - 2)
        opcao2 = "2 - Consultar Medicamento".ljust(largura - 2)
        opcao3 = "3 - Atualizar Medicamento".ljust(largura - 2)
        opcao4 = "4 - Excluir   Medicamento".ljust(largura - 2)
        opcao5 = "5 - Sair".ljust(largura - 2)

        # 2. Imprime o menu com a lógica de cores
        print(f"{Fore.BLUE}+{'-' * (largura - 2)}+")
        # A linha do título vira um "sanduíche": Molde Verde -> Texto Branco -> Molde Verde
        print(f"{Fore.BLUE}|{Fore.BLUE}{titulo_centralizado}{Fore.BLUE}|")
        print(f"{Fore.BLUE}+{'=' * (largura - 2)}+")
        
        # As linhas das opções seguem a mesma lógica do "sanduíche"
        print(f"{Fore.BLUE}|{Fore.WHITE}{opcao1}{Fore.BLUE}|")
        print(f"{Fore.BLUE}|{Fore.WHITE}{opcao2}{Fore.BLUE}|")
        print(f"{Fore.BLUE}|{Fore.WHITE}{opcao3}{Fore.BLUE}|")
        print(f"{Fore.BLUE}|{Fore.WHITE}{opcao4}{Fore.BLUE}|")
        print(f"{Fore.BLUE}|{Fore.WHITE}{opcao5}{Fore.BLUE}|")
        
        print(f"{Fore.BLUE}+{'-' * (largura - 2)}+")

        # 4. Pede a opção ao usuário (colorido)
        opcao = input(Fore.YELLOW + "\nEscolha uma opção: ")

        # 5. Lógica de decisão (com prints coloridos para feedback)
        if opcao == "1":
            print(f"\n{Fore.CYAN}Chamando a função: cadastrar_medicamento()")
        elif opcao == "2":
            print(f"\n{Fore.CYAN}Chamando a função: listar_medicamentos()")
        elif opcao == "3":
            print(f"\n{Fore.CYAN}Chamando a função: escolher_opcao()") # Nome da função que combinamos
            escolher_opcao()
        elif opcao == "4":
            print(f"\n{Fore.CYAN}Chamando a função: excluir_medicamento()")
        elif opcao == "5":
            print(f"\n{Fore.CYAN}Obrigado por usar o PharmaCRUD! Até logo.")
            break
        else:
            print(f"\n{Fore.RED}Opção inválida! Por favor, escolha um número de 1 a 5.")
        
        # 6. Pausa para o usuário 
        input("\nPressione Enter para voltar ao menu...")
