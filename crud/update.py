from data.models import Medicamento
from decimal import Decimal


def editar_nome(item: Medicamento) -> None:
    novo_nome = input("\nDigite o novo nome: ")
    item.nome = novo_nome
    return print(f"\nNome atualizado para: {item.nome}\n")


def editar_principio_ativo(item: Medicamento) -> None:
    item.principio_ativo = input("\nDigite o novo princípio ativo: ")
    return print(f"\nPrincípio ativo atualizado para: {item.principio_ativo}\n")


def editar_apresentacao(item: Medicamento) -> None:
    item.apresentacao = input("\nDigite a nova apresentação: ")
    return print(f"\nApresentação atualizada para: {item.apresentacao}\n")


def editar_concentracao(item: Medicamento) -> None:
    item.concentracao = input("\nDigite a nova concentração: ")
    return print(f"\nConcentração atualizada para: {item.concentracao}\n")


def editar_fabricante(item: Medicamento) -> None:
    item.fabricante = input("\nDigite o novo fabricante: ")
    return print(f"\nFabricante atualizado para: {item.fabricante}\n")


def editar_preco(item: Medicamento) -> None:
    item.preco = Decimal(input("\nDigite o novo preço: "))
    return print(f"\nPreço atualizado para: {item.preco}\n")


def editar_quantidade_estoque(item: Medicamento) -> None:
    item.quantidade_estoque = int(
        input("\nDigite a nova quantidade em estoque: "))
    return print(
        f"\nQuantidade em estoque atualizada para: {item.quantidade_estoque}\n")


def editar_receita_obrigatoria(item: Medicamento) -> None:
    item.receita_obrigatoria = input(
        "\nDigite se a receita é obrigatória (True/False): ").strip().lower() == 'true'
    return print(
        f"\nReceita obrigatória atualizada para: {item.receita_obrigatoria}\n")


def editar_data_validade(item: Medicamento) -> None:
    item.data_validade = input(
        "\nDigite a nova data de validade (AAAA-MM-DD): ")
    return print(f"\nData de validade atualizada para: {item.data_validade}\n")


def editar_disponivel_farmacia_popular(item: Medicamento) -> None:
    item.disponivel_farmacia_popular = input(
        "\nDigite se está disponível na Farmácia Popular (True/False): ").strip().lower() == 'true'
    return print(
        f"\nDisponível na Farmácia Popular atualizado para: {item.disponivel_farmacia_popular}\n")
