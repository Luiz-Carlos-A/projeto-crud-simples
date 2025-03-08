from db import conectar_db

def adicionar_carro(marca, modelo, ano, preco, estoque, placa):
    conn = conectar_db()
    cursor = conn.cursor()

    cursor.execute('''
    INSERT INTO carros (marca, modelo, ano, preco, estoque, placa)
    VALUES (?, ?, ?, ?, ?, ?)
    ''', (marca, modelo, ano, preco, estoque, placa))

    conn.commit()
    conn.close()
    print(f"Carro {marca} {modelo} adicionado com sucesso!")

def buscar_carros():
    conn = conectar_db()
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM carros')
    carros = cursor.fetchall()

    if carros:
        for carro in carros:
            print(f"ID: {carro[0]}, Marca: {carro[1]}, Modelo: {carro[2]}, Ano: {carro[3]}, Preço: {carro[4]}, Estoque: {carro[5]}, Placa: {carro[6]}")
    else:
        print("Nenhum carro encontrado.")
    
    conn.close()

def atualizar_carro(id, marca, modelo, ano, preco, estoque, placa):
    conn = conectar_db()
    cursor = conn.cursor()

    cursor.execute('''
    UPDATE carros
    SET marca = ?, modelo = ?, ano = ?, preco = ?, estoque = ?, placa = ?
    WHERE id = ?
    ''', (marca, modelo, ano, preco, estoque, placa, id))

    conn.commit()

    if cursor.rowcount > 0:
        print(f"Carro ID {id} atualizado com sucesso!")
    else:
        print(f"Carro ID {id} não encontrado.")

    conn.close()

def excluir_carro(id):
    conn = conectar_db()
    cursor = conn.cursor()

    cursor.execute('DELETE FROM carros WHERE id = ?', (id,))
    conn.commit()

    if cursor.rowcount > 0:
        print(f"Carro ID {id} excluído com sucesso!")
    else:
        print(f"Carro ID {id} não encontrado.")

    conn.close()
