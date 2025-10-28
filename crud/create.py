from data.models import Medicamento
from data.database import Estoque
from datetime import datetime

DB_PATH = "data/farmacia.db"  # Caminho do banco SQLite

def adicionar_medicamento():
    print("\n--- Cadastro de Novo Medicamento ---")

    nome = input("Nome do medicamento: ")
    principio_ativo = input("Princípio ativo: ")
    apresentacao = input("Apresentação (ex: comprimido, xarope): ")
    concentracao = input("Concentração (ex: 500mg, 20ml): ")
    fabricante = input("Fabricante: ")

    preco = float(input("Preço (use ponto ou vírgula): ").replace(",", "."))
    quantidade_estoque = int(input("Quantidade em estoque: "))

    receita_obrigatoria = input("Receita obrigatória? (s/n): ").strip().lower() == "s"
    validade_input = input("Data de validade (dd/mm/aaaa): ")
    data_validade = datetime.strptime(validade_input, "%d/%m/%Y").strftime("%Y-%m-%d")

    disponivel_fp = input("Disponível na Farmácia Popular? (s/n): ").strip().lower() == "s"

    novo_medicamento = Medicamento(
        id=None,  # o banco deve gerar automaticamente
        nome=nome,
        principio_ativo=principio_ativo,
        apresentacao=apresentacao,
        concentracao=concentracao,
        fabricante=fabricante,
        preco=preco,
        quantidade_estoque=quantidade_estoque,
        receita_obrigatoria=receita_obrigatoria,
        data_validade=data_validade,
        disponivel_farmacia_popular=disponivel_fp
    )

    # Aqui o Estoque precisa saber onde está o banco (.db)
    estoque = Estoque("data/farmacia.db")
    estoque.adicionar_medicamento(novo_medicamento)

    print(f"\n✅ Medicamento '{nome}' adicionado com sucesso!\n")


if __name__ == "__main__":
    adicionar_medicamento()