import sqlite3
from data.models import Medicamento

class Estoque():
    def __init__(self,db_file):
        self.db_file = db_file
    
    def listar_todos_medicamentos(self):
        # 1. Conectar ao banco
        # 2. Executar o SQL
        # 3. Pegar os resultados
        # 4. Transformar em objetos
        # 5. Fechar a conexão
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM medicamentos")
        resultados_brutos = cursor.fetchall()
        lista_de_medicamentos = []
        for linha in resultados_brutos:
            novo_medicamento = Medicamento(*linha)
            lista_de_medicamentos.append(novo_medicamento)

        conn.close()
        return lista_de_medicamentos
    
    def adicionar_medicamento(self, med):
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO medicamentos 
        (nome, principio_ativo, apresentacao, concentracao, fabricante, preco, quantidade_estoque, receita_obrigatoria, data_validade, disponivel_farmacia_popular)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        med.nome,
        med.principio_ativo,
        med.apresentacao,
        med.concentracao,
        med.fabricante,
        med.preco,
        med.quantidade_estoque,
        med.receita_obrigatoria,
        med.data_validade,
        med.disponivel_farmacia_popular
    ))

    
        conn.commit()
        conn.close()
    
    def remover_medicamento_por_id(self, med_id: int) -> bool:
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM medicamentos WHERE id = ?", (med_id,))
        affected = cursor.rowcount
        conn.commit()
        conn.close()
        return affected > 0

banco_de_dados = []