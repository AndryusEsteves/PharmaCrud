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


    