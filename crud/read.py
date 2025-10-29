from data.database import Estoque
from data.models import Medicamento

DB_PATH = 'data/farmacia.db' #importa banco de dados

def exibir_lista_medicamento():
    estoque = Estoque(DB_PATH)

    lista_medicamentos = estoque.listar_todos_medicamentos()
    print(f"\n--- Lista de Medicamentos no Estoque ---")
    if not lista_medicamentos:
        print(f"Nenhum medicamento cadastrado")
    else:
        for med in lista_medicamentos:
            print(f"""
                ==============================================================
                ID: {med.id} 
                Nome: {med.nome}
                Principio Ativo: {med.principio_ativo}
                Apresentação: {med.apresentacao}
                Concentração: {med.concentracao}
                Fabricante: {med.fabricante}
                Preço: R$ {med.preco:.2f}
                Qtd Estoque: {med.quantidade_estoque}
                Receita Obrigatória?: {med.receita_obrigatoria}
                Validade: {med.data_validade}
                Disponível Farmacia Popular: {med.disponivel_farmacia_popular}
                ==============================================================
            """)

def exibir_lista_medicamento_simples(lista: list[Medicamento]) -> Medicamento | None:
    try:
        print("===== Medicamentos cadastrados =====")
        for medicamento in lista:
            print(f"    ID: {medicamento.id} | Nome: {medicamento.nome}")
        print("=====================================")

        id_editar: int = int(input("\nDigite o ID do medicamento a editar: "))
        if not 0 <= id_editar <= len(lista):
            raise IndexError("ID inválido. Tente novamente.")
    except IndexError as err:
        print(err)
    else:
        return (lista[id_editar - 1])