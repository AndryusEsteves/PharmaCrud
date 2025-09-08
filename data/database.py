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

medicamentos = []


