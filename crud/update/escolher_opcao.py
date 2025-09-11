from typing import Any
# from ..data.database import banco as db
from crud.update.achar_indice import achar_valor_por_indice
import crud.update.editar_medicamento as editar_medicamento


def escolher_item(item: dict[str, Any] | None) -> None:
    if item is None:
        print("Nenhum item selecionado para edição.")
        return

    while True:
        opcao: str = input("\n===== Menu de Edição =====\n    "
                           "1 - Editar Nome\n    "
                           "2 - Editar Principio Ativo\n    "
                           "3 - Editar Apresentação\n    "
                           "4 - Editar Concentração\n    "
                           "5 - Editar Fabricante\n    "
                           "6 - Editar Preço\n    "
                           "7 - Editar Quantidade em Estoque\n    "
                           "8 - Editar Receita Obrigatória (True/False)\n    "
                           "9 - Editar Data de Validade (AAAA-MM-DD)\n    "
                           "10 - Editar Disponível na Farmácia Popular (True/False)\n    "
                           "0 - Sair\n    "
                           "=====================================\n\n"
                           "Escolha uma opção: "
                           )

        try:
            match opcao:
                case "1":
                    editar_medicamento.editar_nome(item)
                    break
                case "2":
                    editar_medicamento.editar_principio_ativo(item)
                    break
                case "3":
                    editar_medicamento.editar_apresentacao(item)
                    break
                case "4":
                    editar_medicamento.editar_concentracao(item)
                    break
                case "5":
                    editar_medicamento.editar_fabricante(item)
                    break
                case "6":
                    editar_medicamento.editar_preco(item)
                    break
                case "7":
                    editar_medicamento.editar_quantidade_estoque(item)
                    break
                case "8":
                    editar_medicamento.editar_receita_obrigatoria(item)
                    break
                case "9":
                    editar_medicamento.editar_data_validade(item)
                    break
                case "10":
                    editar_medicamento.editar_disponivel_farmacia_popular(item)
                    break
                case "0":
                    break
                case _:
                    print("Opção inválida")
        except Exception as e:
            print(f"Erro ao editar o item: {e}")


if __name__ == "__main__":

    banco_de_dados: list[dict[str, Any]] = [
        {
            "id": 1,
            "nome": "Dipirona Sódica",
            "principio_ativo": "Dipirona Sódica",
            "apresentacao": "comprimido",
            "concentracao": "500mg",
            "fabricante": "Medley",
            "preco": 5.99,
            "quantidade_estoque": 150,
            "receita_obrigatoria": False,
            "data_validade": "2026-08-10",
            "disponivel_farmacia_popular": False
        },
        {
            "id": 2,
            "nome": "Amoxicilina",
            "principio_ativo": "Amoxicilina",
            "apresentacao": "cápsula",
            "concentracao": "500mg",
            "fabricante": "EMS",
            "preco": 22.50,
            "quantidade_estoque": 80,
            "receita_obrigatoria": True,
            "data_validade": "2027-01-25",
            "disponivel_farmacia_popular": False
        },
        {
            "id": 3,
            "nome": "Omeprazol",
            "principio_ativo": "Omeprazol",
            "apresentacao": "cápsula",
            "concentracao": "20mg",
            "fabricante": "Prati-Donaduzzi",
            "preco": 14.80,
            "quantidade_estoque": 200,
            "receita_obrigatoria": False,
            "data_validade": "2026-11-05",
            "disponivel_farmacia_popular": True
        },
        {
            "id": 4,
            "nome": "Buscopan",
            "principio_ativo": "Butilbrometo de escopolamina",
            "apresentacao": "comprimido revestido",
            "concentracao": "10mg",
            "fabricante": "Boehringer Ingelheim",
            "preco": 18.99,
            "quantidade_estoque": 75,
            "receita_obrigatoria": False,
            "data_validade": "2027-04-15",
            "disponivel_farmacia_popular": False
        },
        {
            "id": 5,
            "nome": "Losartana Potássica",
            "principio_ativo": "Losartana Potássica",
            "apresentacao": "comprimido",
            "concentracao": "50mg",
            "fabricante": "Novartis",
            "preco": 11.25,
            "quantidade_estoque": 120,
            "receita_obrigatoria": True,
            "data_validade": "2026-09-30",
            "disponivel_farmacia_popular": True
        },
        {
            "id": 6,
            "nome": "Neosaldina",
            "principio_ativo": "Dipirona + Isometepteno + Cafeína",
            "apresentacao": "cápsula gelatinosa mole",
            "concentracao": "300mg/30mg/50mg",
            "fabricante": "Takeda",
            "preco": 25.00,
            "quantidade_estoque": 90,
            "receita_obrigatoria": False,
            "data_validade": "2027-03-20",
            "disponivel_farmacia_popular": False
        },
        {
            "id": 7,
            "nome": "Sinvastatina",
            "principio_ativo": "Sinvastatina",
            "apresentacao": "comprimido revestido",
            "concentracao": "20mg",
            "fabricante": "Eurofarma",
            "preco": 17.50,
            "quantidade_estoque": 60,
            "receita_obrigatoria": True,
            "data_validade": "2026-10-18",
            "disponivel_farmacia_popular": True
        },
        {
            "id": 8,
            "nome": "Ibuprofeno",
            "principio_ativo": "Ibuprofeno",
            "apresentacao": "xarope",
            "concentracao": "100mg/5ml",
            "fabricante": "Germed",
            "preco": 9.90,
            "quantidade_estoque": 45,
            "receita_obrigatoria": False,
            "data_validade": "2026-12-01",
            "disponivel_farmacia_popular": False
        },
        {
            "id": 9,
            "nome": "Paracetamol",
            "principio_ativo": "Paracetamol",
            "apresentacao": "gotas",
            "concentracao": "200mg/ml",
            "fabricante": "Neo Química",
            "preco": 6.75,
            "quantidade_estoque": 110,
            "receita_obrigatoria": False,
            "data_validade": "2027-05-22",
            "disponivel_farmacia_popular": False
        },
        {
            "id": 10,
            "nome": "Cloridrato de Fluoxetina",
            "principio_ativo": "Cloridrato de Fluoxetina",
            "apresentacao": "cápsula",
            "concentracao": "20mg",
            "fabricante": "Pfizer",
            "preco": 34.00,
            "quantidade_estoque": 50,
            "receita_obrigatoria": True,
            "data_validade": "2026-07-07",
            "disponivel_farmacia_popular": False
        }
    ]

    # escolher_item(achar_valor_por_indice(banco_de_dados))
    # for medicamento in banco_de_dados:
    #     print(f"{medicamento}\n")
