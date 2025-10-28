import sqlite3


conn = sqlite3.connect("data/farmacia.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS medicamentos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    principio_ativo TEXT,
    apresentacao TEXT,
    concentracao TEXT,
    fabricante TEXT,
    preco REAL,
    quantidade_estoque INTEGER,
    receita_obrigatoria BOOLEAN,
    data_validade TEXT,
    disponivel_farmacia_popular BOOLEAN
)
""")

conn.commit()
conn.close()

print("✅ Banco de dados 'farmacia.db' criado com sucesso dentro da pasta data/")
