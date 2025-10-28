from typing import Any
import sqlite3

DB_PATH = 'data/farmacia.db'


class GerenciadorExclusao:
    """
    Classe para gerenciar a exclusão de medicamentos seguindo padrão POO.
    Implementa conexão direta com SQLite para ser autossuficiente.
    """
    
    def __init__(self, db_path: str):
        self.db_path = db_path
    
    def obter_medicamento_por_id(self, med_id: int) -> tuple | None:
        """Busca um medicamento pelo ID no banco de dados."""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM medicamentos WHERE id = ?", (med_id,))
            row = cursor.fetchone()
            conn.close()
            return row
        except Exception as e:
            print(f"Erro ao buscar medicamento: {e}")
            return None
    
    def remover_medicamento_por_id(self, med_id: int) -> bool:
        """Remove um medicamento pelo ID do banco de dados."""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            cursor.execute("DELETE FROM medicamentos WHERE id = ?", (med_id,))
            affected = cursor.rowcount
            conn.commit()
            conn.close()
            return affected > 0
        except Exception as e:
            print(f"Erro ao remover medicamento: {e}")
            return False
    
    def listar_medicamentos_simples(self) -> list:
        """Lista medicamentos de forma simples para seleção."""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            cursor.execute("SELECT id, nome FROM medicamentos ORDER BY id")
            rows = cursor.fetchall()
            conn.close()
            return rows
        except Exception as e:
            print(f"Erro ao listar medicamentos: {e}")
            return []


def excluir_medicamento() -> None:
    """
    Exclui um medicamento do banco (SQLite) utilizando padrão POO.
    Implementação autossuficiente que não depende de modificações em outros arquivos.
    """
    gerenciador = GerenciadorExclusao(DB_PATH)
    
    # Mostrar lista de medicamentos disponíveis
    medicamentos = gerenciador.listar_medicamentos_simples()
    if not medicamentos:
        print("\nNenhum medicamento cadastrado para exclusão.\n")
        return
    
    print("\n===== Medicamentos cadastrados =====")
    for med_id, nome in medicamentos:
        print(f"    ID: {med_id} | Nome: {nome}")
    print("=====================================")

    try:
        id_escolhido: int = int(input("\nDigite o ID do medicamento a excluir: "))
    except ValueError:
        print("Entrada inválida. Digite um número inteiro para o ID.")
        return

    # Buscar o item diretamente no banco para exibir um resumo antes de excluir
    row = gerenciador.obter_medicamento_por_id(id_escolhido)
    if not row:
        print("ID não encontrado.")
        return

    # Mapeia a linha retornada (tuple) para campos nomeados
    # Estrutura esperada: (id, nome, principio_ativo, apresentacao, concentracao, fabricante,
    #                      preco, quantidade_estoque, receita_obrigatoria, data_validade, disponivel_farmacia_popular)
    (
        rid, nome, principio_ativo, apresentacao, concentracao, fabricante,
        preco, quantidade_estoque, receita_obrigatoria, data_validade, disponivel_fp
    ) = row

    print("\nResumo do item selecionado:")
    print(f"  - ID: {rid}")
    print(f"  - Nome: {nome}")
    print(f"  - Princípio Ativo: {principio_ativo}")
    print(f"  - Apresentação: {apresentacao}")
    print(f"  - Concentração: {concentracao}")
    print(f"  - Fabricante: {fabricante}")
    print(f"  - Preço: R$ {float(preco):.2f}")
    print(f"  - Quantidade em Estoque: {quantidade_estoque}")
    print(f"  - Receita Obrigatória: {receita_obrigatoria}")
    print(f"  - Data de Validade: {data_validade}")
    print(f"  - Disponível na Farmácia Popular: {disponivel_fp}")

    confirmar: str = input("\nConfirma a exclusão? (s/n): ").strip().lower()
    if confirmar not in {"s", "sim"}:
        print("\nExclusão cancelada.\n")
        return

    removido = gerenciador.remover_medicamento_por_id(id_escolhido)
    if removido:
        print(f"\nMedicamento removido com sucesso: ID {id_escolhido} - {nome}\n")
    else:
        print("\nNenhum registro foi removido (verifique o ID).\n")

#bloco de teste
'''if __name__ == "__main__":
    # Exemplo rápido para teste manual isolado
    banco_teste: list[dict[str, Any]] = [
        {"id": 1, "nome": "Dipirona"},
        {"id": 2, "nome": "Amoxicilina"},
        {"id": 3, "nome": "Omeprazol"},
    ]
    excluir_medicamento(banco_teste)
    print("\nEstado final do banco (teste):")
    for med in banco_teste:
        print(med)
'''
