# Projeto CRUD Famaceutico SoftEX BFD em python

## Campos do Banco de Dados para um Remédio

| Campo                      | Tipo            | Explicação |
|-----------------------------|-----------------|------------|
| **id**                      | int ou str      | Um identificador único e obrigatório para cada medicamento, usado para localizá-lo de forma precisa no banco de dados. |
| **nome**                    | str             | O nome comercial do medicamento, como "Neosaldina" ou "Buscopan". |
| **principio_ativo**         | str             | A substância química principal do remédio, como "Dipirona" ou "Hioscina". É crucial para buscas de equivalentes. |
| **apresentacao**            | str             | A forma física do medicamento, como "comprimido", "cápsula" ou "xarope". |
| **concentracao**            | str             | A quantidade de princípio ativo por dose. É uma string para manter a unidade de medida (ex: "500mg", "10mg/ml"). |
| **fabricante**              | str             | O nome do laboratório que produz o medicamento (ex: "Bayer", "EMS"). |
| **preco**                   | float           | O valor de venda do medicamento. Usar um tipo numérico com casas decimais é importante para cálculos de venda. |
| **quantidade_estoque**      | int             | O número total de unidades do medicamento disponíveis na farmácia. Essencial para o controle de estoque. |
| **receita_obrigatoria**     | bool            | Indica se o medicamento só pode ser vendido com prescrição médica. Use True para sim e False para não. |
| **data_validade**           | str ou datetime | A data de validade do produto. É fundamental para a segurança do paciente e para a gestão de estoque. Uma string no formato AAAA-MM-DD é um bom ponto de partida. |
| **disponivel_farmacia_popular** | bool       | Um True ou False para indicar se o medicamento faz parte do programa do governo Farmácia Popular, podendo ter um preço subsidiado ou ser distribuído gratuitamente. |
