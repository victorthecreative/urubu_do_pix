from database import init_db, init_deposit_db
from usuarios import Usuario, Deposito

def cadastrar_usuario():
    """Função para cadastrar um novo usuário."""
    usuario = Usuario()
    print(f'Usuário {usuario.nome} cadastrado com sucesso!')
    print(f'Sua chave é {usuario.chave_aleatoria}')

def fazer_deposito():
    """Função para realizar um depósito."""
    chave_usuario = input("Digite a chave do usuário para fazer um depósito: ")
    deposito = Deposito(chave_usuario)
    print(f'Depósito de R${deposito.valor_deposito} realizado com sucesso!')
    print(f'Código do Depósito: {deposito.codigo_deposito}')

def main():
    init_db()
    init_deposit_db()

    while True:
        print("\nEscolha uma ação:")
        print("1. Criar novo usuário")
        print("2. Fazer um depósito")
        print("3. Sair")
        
        choice = input("> ")

        if choice == "1":
            cadastrar_usuario()
        elif choice == "2":
            fazer_deposito()
        elif choice == "3":
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()
