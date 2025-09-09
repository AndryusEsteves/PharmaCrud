# data/database.py 

# =====================================================================
# SCHEMA OFICIAL (a ser seguido por TODA A EQUIPE)
# ---------------------------------------------------------------------
# Cada medicamento é um dicionário que deve seguir esta estrutura:
# {
#   "id":                            int,    # Identificador único (não se repete)
#   "nome":                          str,    # Ex: "Dipirona 500mg"
#   "principio_ativo":               str,    # Ex: "Dipirona Sódica"
#   "apresentacao":                  str,    # Ex: "comprimido", "cápsula", "xarope"
#   "concentracao":                  str,    # Ex: "500mg", "10mg/ml"
#   "fabricante":                    str,    # Nome do laboratório
#   "preco":                         float,  # Preço de venda (use . como separador, ex: 12.50)
#   "quantidade_estoque":            int,    # Unidades disponíveis no estoque
#   "receita_obrigatoria":           bool,   # True se precisa de receita, False se não
#   "data_validade":                 str,    # Formato "AAAA-MM-DD"
#   "disponivel_farmacia_popular":   bool    # True se faz parte do programa
# }
# =====================================================================

id_atual = 0

medicamentos = medicamentos = [
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
