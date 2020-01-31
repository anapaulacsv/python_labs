from correntista import Correntista

lista_correntista = []

def cadastro():
    
    nome = input("Digite o nome: ")
    cpf = input("Digite o CPF: ")
    saldo = input("Digite o saldo inicial: ")
    lista_correntista.append(Correntista(nome, cpf, saldo))
    print(50*'-')
    print("Cadastrado com Sucesso.")
    print(50*'-')

opcao = 1

while opcao != 0: 
 
    print("----------Banco-----------")
    print("(1) Cadastro")
    print("(2) Auditoria") 
    print("(0) Sair")
    print("----------------------------------------")
    opcao = int(input("Digite o número: "))

    if opcao == 1:
   
        cadastro()

    elif opcao == 2:
    
        pass 





   