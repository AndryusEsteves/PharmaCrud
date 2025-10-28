from datetime import date
from decimal import Decimal


class Medicamento():

    _id_counter = 0

    def __init__(self, nome: str, principio_ativo: str, apresentacao: str,
                 concentracao: str, fabricante: str, preco: Decimal,
                 quantidade_estoque: int, receita_obrigatoria: bool,
                 data_validade: str, disponivel_farmacia_popular: bool):

        Medicamento._id_counter += 1
        self.id = Medicamento._id_counter
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

    def __repr__(self) -> str:
        return (f"Remedio(id={self.id}, nome={self.nome}, principio_ativo={self.principio_ativo}, "
                f"apresentacao={self.apresentacao}, concentracao={self.concentracao}, "
                f"fabricante={self.fabricante}, preco={self.preco}, "
                f"quantidade_estoque={self.quantidade_estoque}, "
                f"receita_obrigatoria={self.receita_obrigatoria}, "
                f"data_validade={self.data_validade}, "
                f"disponivel_farmacia_popular={self.disponivel_farmacia_popular})")

    def __str__(self) -> str:
        receita = "Sim" if self.receita_obrigatoria else "Não"
        farmacia_popular = "Sim" if self.disponivel_farmacia_popular else "Não"

        return (f"""
------------------------------------
{self.nome} ({self.principio_ativo})
------------------------------------
Apresentação: {self.apresentacao}
Concentração: {self.concentracao}
Fabricante: {self.fabricante}
Validade: {self.data_validade}
Preço: R${self.preco:.2f}
Estoque: {self.quantidade_estoque}
Receita Obrigatória: {receita}
Farmácia Popular: {farmacia_popular}
------------------------------------\n
""")
