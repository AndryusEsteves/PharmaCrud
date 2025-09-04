# PharmaCrud
Projeto CRUD Famaceutico SoftEX BFD em python


Campos do Banco de Dados para um Remédio
id

Tipo: int ou str

Explicação: Um identificador único e obrigatório para cada medicamento, usado para localizá-lo de forma precisa no banco de dados.

nome

Tipo: str

Explicação: O nome comercial do medicamento, como "Neosaldina" ou "Buscopan".

principio_ativo

Tipo: str

Explicação: A substância química principal do remédio, como "Dipirona" ou "Hioscina". É crucial para buscas de equivalentes.

apresentacao

Tipo: str

Explicação: A forma física do medicamento, como "comprimido", "cápsula" ou "xarope".

concentracao

Tipo: str

Explicação: A quantidade de princípio ativo por dose. É uma string para manter a unidade de medida (ex: "500mg", "10mg/ml").

fabricante

Tipo: str

Explicação: O nome do laboratório que produz o medicamento (ex: "Bayer", "EMS").

preco

Tipo: float

Explicação: O valor de venda do medicamento. Usar um tipo numérico com casas decimais é importante para cálculos de venda.

quantidade_estoque

Tipo: int

Explicação: O número total de unidades do medicamento disponíveis na farmácia. Essencial para o controle de estoque.

receita_obrigatoria

Tipo: bool

Explicação: Indica se o medicamento só pode ser vendido com prescrição médica. Use True para sim e False para não.

data_validade

Tipo: str ou datetime

Explicação: A data de validade do produto. É fundamental para a segurança do paciente e para a gestão de estoque. Uma string no formato AAAA-MM-DD é um bom ponto de partida.

disponivel_farmacia_popular

Tipo: bool

Explicação: Um True ou False para indicar se o medicamento faz parte do programa do governo Farmácia Popular, podendo ter um preço subsidiado ou ser distribuído gratuitamente.