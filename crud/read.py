from data.database import Estoque

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