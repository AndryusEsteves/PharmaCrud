import sqlite3
from datetime import date

class Medicamento():
    def __init__(
            self, 
            id, 
            nome, 
            principio_ativo,
            apresentacao, 
            concentracao, 
            fabricante, 
            preco, 
            quantidade_estoque, 
            receita_obrigatoria, 
            data_validade, 
            disponivel_farmacia_popular
        ):
       self.id = id
       self.nome = nome
       self.principio_ativo = principio_ativo
       self.apresentacao = apresentacao
       self.concentracao = concentracao
       self.fabricante = fabricante
       self.preco = preco
       self.quantidade_estoque = quantidade_estoque
       self.receita_obrigatoria = receita_obrigatoria
       self.data_validade = data_validade
       self.disponivel_farmacia_popular = disponivel_farmacia_popular

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
    