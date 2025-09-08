from typing import Any


def excluir_medicamento(lista: list[dict[str, Any]] | None = None) -> None:
    """
    Exclui um medicamento da lista informada. Se nenhuma lista for passada,
    tenta utilizar a lista global do banco de dados.
    """
    if lista is None:
        try:
            from data.database import medicamentos as lista
        except Exception:
            print("Banco de dados não encontrado. Forneça uma lista válida.")
            return

    if not isinstance(lista, list):
        print("Estrutura de dados inválida. Esperada uma lista de dicionários.")
        return

    if not lista:
        print("\nNenhum medicamento para excluir.\n")
        return

    print("===== Medicamentos cadastrados =====")
    for medicamento in lista:
        print(f"    ID: {medicamento['id']} | Nome: {medicamento['nome']}")
    print("=====================================")

    try:
        id_escolhido: int = int(input("\nDigite o ID do medicamento a excluir: "))
        if not 1 <= id_escolhido <= len(lista):
            raise IndexError("ID inválido. Tente novamente.")
    except ValueError:
        print("Entrada inválida. Digite um número inteiro para o ID.")
        return
    except IndexError as err:
        print(err)
        return

    indice = id_escolhido - 1

    item = lista[indice]
    print("\nResumo do item selecionado:")
    for chave, valor in item.items():
        print(f"  - {chave}: {valor}")

    confirmar: str = input("\nConfirma a exclusão? (s/n): ").strip().lower()
    if confirmar not in {"s", "sim"}:
        print("\nExclusão cancelada.\n")
        return

    try:
        removido = lista.pop(indice)
        print(f"\nMedicamento removido com sucesso: ID {removido['id']} - {removido['nome']}\n")
    except Exception as e:
        print(f"Erro ao excluir o medicamento: {e}")

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
