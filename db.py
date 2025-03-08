import sqlite3

def conectar_db():
    # Conecta ao banco de dados (ou cria um novo se não existir)
    conn = sqlite3.connect('concessionaria.db')
    return conn

def criar_tabela():
    conn = conectar_db()
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS carros (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        marca TEXT NOT NULL,
        modelo TEXT NOT NULL,
        ano INTEGER NOT NULL,
        preco REAL NOT NULL,
        estoque INTEGER NOT NULL,
        placa TEXT NOT NULL UNIQUE
    )
    ''')

    conn.commit()
    conn.close()

# Chama a criação da tabela ao iniciar o programa
if __name__ == "__main__":
    criar_tabela()
    print("Tabela criada ou já existente.")
