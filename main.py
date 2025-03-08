from carro_crud import adicionar_carro, buscar_carros, atualizar_carro, excluir_carro
from db import criar_tabela

def menu():
    print("\nBem-vindo à concessionária!")
    print("1. Adicionar carro")
    print("2. Buscar carros")
    print("3. Atualizar carro")
    print("4. Excluir carro")
    print("5. Sair")
    
    escolha = input("Escolha uma opção: ")

    return escolha

def rodar_programa():
    # Cria a tabela ao iniciar o programa
    criar_tabela()

    while True:
        escolha = menu()

        if escolha == '1':
            marca = input("Marca do carro: ")
            modelo = input("Modelo do carro: ")
            ano = int(input("Ano do carro: "))
            preco = float(input("Preço do carro: "))
            estoque = int(input("Quantidade em estoque: "))
            placa = input("Placa do carro: ")
            adicionar_carro(marca, modelo, ano, preco, estoque, placa)

        elif escolha == '2':
            buscar_carros()

        elif escolha == '3':
            id = int(input("ID do carro a ser atualizado: "))
            marca = input("Nova marca: ")
            modelo = input("Novo modelo: ")
            ano = int(input("Novo ano: "))
            preco = float(input("Novo preço: "))
            estoque = int(input("Novo estoque: "))
            placa = input("Nova placa: ")
            atualizar_carro(id, marca, modelo, ano, preco, estoque, placa)

        elif escolha == '4':
            id = int(input("ID do carro a ser excluído: "))
            excluir_carro(id)

        elif escolha == '5':
            print("Saindo do programa.")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    rodar_programa()
