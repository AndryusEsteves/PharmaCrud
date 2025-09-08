# Projeto CRUD Farmacêutico SoftEX BFD em Python

  Este projeto é uma aplicação de **CRUD** (Create, Read, Update, Delete) desenvolvida em Python, criada para a gestão de um banco de dados de medicamentos. A ferramenta foi concebida como parte do programa **SoftEX BFD**, fornecendo uma solução prática e organizada para o controle de informações farmacêuticas.

---

## 🚀 Funcionalidades

  A aplicação permite que o usuário execute as seguintes operações essenciais para a manutenção de um banco de dados de medicamentos:

* **Adicionar (Create):** Incluir novos registros de medicamentos no sistema, com todas as informações detalhadas.
* **Visualizar (Read):** Consultar dados de um ou mais medicamentos, facilitando a busca e a conferência de informações.
* **Atualizar (Update):** Modificar os dados de um medicamento já existente, garantindo que as informações estejam sempre corretas e atualizadas.
* **Excluir (Delete):** Remover medicamentos do banco de dados de forma definitiva.

---

## 📋 Estrutura do Banco de Dados

  O banco de dados foi projetado para armazenar as informações de maneira completa e eficiente. Cada registro de medicamento é composto pelos seguintes campos:

| Campo                      | Tipo            | Descrição |
|-----------------------------|-----------------|------------|
| **id**                      | `int`      | Um identificador único e obrigatório para cada medicamento, usado para localizá-lo de forma precisa no banco de dados. |
| **nome**                    | `str`             | O nome comercial do medicamento, como "Neosaldina" ou "Buscopan". |
| **principio_ativo**         | `str`             | A substância química principal do remédio, como "Dipirona" ou "Hioscina". É crucial para buscas de equivalentes. |
| **apresentacao**            | `str`             | A forma física do medicamento, como "comprimido", "cápsula" ou "xarope". |
| **concentracao**            | `str`             | A quantidade de princípio ativo por dose. É uma string para manter a unidade de medida (ex: "500mg", "10mg/ml"). |
| **fabricante**              | `str`             | O nome do laboratório que produz o medicamento (ex: "Bayer", "EMS"). |
| **preco**                   | `float`           | O valor de venda do medicamento. Usar um tipo numérico com casas decimais é importante para cálculos de venda. |
| **quantidade_estoque**      | `int`             | O número total de unidades do medicamento disponíveis na farmácia. Essencial para o controle de estoque. |
| **receita_obrigatoria**     | `bool`            | Indica se o medicamento só pode ser vendido com prescrição médica. Use True para sim e False para não. |
| **data_validade**           | `datetime` | A data de validade do produto. É fundamental para a segurança do paciente e para a gestão de estoque. Uma string no formato AAAA-MM-DD é um bom ponto de partida. |
| **disponivel_farmacia_popular** | `bool`       | Um True ou False para indicar se o medicamento faz parte do programa do governo Farmácia Popular, podendo ter um preço subsidiado ou ser distribuído gratuitamente. |