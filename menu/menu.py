from crud.read import exibir_lista_medicamento
import crud.update as editar_medicamento
import os  # limpa o terminal automaticamente
import time
from colorama import init, Fore, Style
from data.models import Medicamento
from data.database import banco_de_dados
from crud.read import exibir_lista_medicamento_simples
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
            exibir_lista_medicamento()
        elif opcao == "3":
            # Nome da função que combinamos
            print(f"\n{Fore.CYAN}Chamando a função: escolher_opcao()")
            menu_editar()
        elif opcao == "4":
            print(f"\n{Fore.CYAN}Chamando a função: excluir_medicamento()")
        elif opcao == "5":
            print(f"\n{Fore.CYAN}Obrigado por usar o PharmaCRUD! Até logo.")
            break
        else:
            print(
                f"\n{Fore.RED}Opção inválida! Por favor, escolha um número de 1 a 5.")

        # 6. Pausa para o usuário
        input("\nPressione Enter para voltar ao menu...")


def menu_editar() -> None:
    item = exibir_lista_medicamento_simples(banco_de_dados)
    if item is None:
        print("Nenhum item selecionado para edição.")
        return

    while True:
        opcao: str = input("\n===== Menu de Edição =====\n    "
                           "1 - Editar Nome\n    "
                           "2 - Editar Principio Ativo\n    "
                           "3 - Editar Apresentação\n    "
                           "4 - Editar Concentração\n    "
                           "5 - Editar Fabricante\n    "
                           "6 - Editar Preço\n    "
                           "7 - Editar Quantidade em Estoque\n    "
                           "8 - Editar Receita Obrigatória (True/False)\n    "
                           "9 - Editar Data de Validade (AAAA-MM-DD)\n    "
                           "10 - Editar Disponível na Farmácia Popular (True/False)\n    "
                           "0 - Sair\n    "
                           "=====================================\n\n"
                           "Escolha uma opção: "
                           )

        try:
            match opcao:
                case "1":
                    editar_medicamento.editar_nome(item)
                    break
                case "2":
                    editar_medicamento.editar_principio_ativo(item)
                    break
                case "3":
                    editar_medicamento.editar_apresentacao(item)
                    break
                case "4":
                    editar_medicamento.editar_concentracao(item)
                    break
                case "5":
                    editar_medicamento.editar_fabricante(item)
                    break
                case "6":
                    editar_medicamento.editar_preco(item)
                    break
                case "7":
                    editar_medicamento.editar_quantidade_estoque(item)
                    break
                case "8":
                    editar_medicamento.editar_receita_obrigatoria(item)
                    break
                case "9":
                    editar_medicamento.editar_data_validade(item)
                    break
                case "10":
                    editar_medicamento.editar_disponivel_farmacia_popular(item)
                    break
                case "0":
                    break
                case _:
                    print("Opção inválida")
        except Exception as e:
            print(f"Erro ao editar o item: {e}")
