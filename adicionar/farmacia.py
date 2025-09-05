import json
import os
from datetime import datetime

ARQUIVO = "medicamentos.json"

def carregar_dados():
    if not os.path.exists(ARQUIVO) or os.path.getsize(ARQUIVO) == 0:
        return []
    try:
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        print("Erro ao carregar os dados. Criando uma nova lista")
        return []

def salvar_dados(medicamentos):
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(medicamentos, f, indent=4, ensure_ascii=False)

def adicionar_medicamento(nome, laboratorio, data_de_validade, quantidade, dosagem, valor):
    try:
        if isinstance(data_de_validade, str):
            data_obj = datetime.strptime(data_de_validade, "%Y-%m-%d")
        elif isinstance(data_de_validade, datetime):
            data_obj = data_de_validade
        else:
            raise ValueError("Data inválida")
        data_str = data_obj.strftime("%Y-%m-%d")
    except ValueError:
        print(f"Data de validade inválida para {nome}. Use YYYY-MM-DD")
        return

    try:
        quantidade = int(quantidade)
        valor = float(valor)
    except ValueError:
        print(f"Quantidade ou valor inválido para {nome}.")
        return

    medicamento = {
        "nome": nome,
        "laboratorio": laboratorio,
        "data_de_validade": data_str,
        "quantidade": quantidade,
        "dosagem": dosagem,
        "valor": valor
    }

    medicamentos = carregar_dados()
    medicamentos.append(medicamento)
    salvar_dados(medicamentos)
    print(f"Medicamento '{nome}' adicionado com sucesso!")

# --- Lista de medicamentos para cadastro inicial ---
novos_medicamentos = [
    ("Paracetamol", "Laboratório XYZ", "2025-12-31", 10, "500mg", 12.50),
    ("Ibuprofeno", "Laboratório ABC", "2024-10-15", 20, "200mg", 8.75),
    ("Amoxicilina", "Laboratório DEF", "2025-05-20", 15, "500mg", 20.0)
]

for med in novos_medicamentos:
    adicionar_medicamento(*med)
