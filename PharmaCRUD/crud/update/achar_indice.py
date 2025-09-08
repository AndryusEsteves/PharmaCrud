from typing import Any


def achar_valor_por_indice(lista: list[dict[str, Any]]) -> dict[str, Any] | None:
    try:
        print("===== Medicamentos cadastrados =====")
        for medicamento in lista:
            print(f"    ID: {medicamento['id']} | Nome: {medicamento['nome']}")
        print("=====================================")

        id_editar: int = int(input("\nDigite o ID do medicamento a editar: "))
        if not 0 <= id_editar <= len(lista):
            raise IndexError("ID inválido. Tente novamente.")
    except IndexError as err:
        print(err)
    else:
        return (lista[id_editar - 1])
