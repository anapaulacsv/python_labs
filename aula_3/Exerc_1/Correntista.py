# Projeto Orientação de objetos

#Criar uma classe correntista com os seguintes atributos:
    #Nome do correntista;
    #Saldo em conta;
    #Histórico de saque e depositos

#Deve possuir as seguintes capacidades:
    #Fazer deposito 
    #Fazer saque 
    #A classe dever ser iterável, a iteração deve ocorrer sobre o histórico de saques e depósitos para, 
#por exemplo, permitir imprimir todo o histórico.

class Correntista:
    def __init__(self,nome,saldo):
        self.__nome = nome
        self.__saldo = saldo
        self.__index = 0
        self.__historico = []

    def saque(self,valor):
        if (valor > self.__saldo):
            print("Saldo insuficiente!") 
        else:     
            self.__saldo -= valor 
            self.__historico.append(-valor)
            self.__index += 1


    def deposito(self,valor):
        self.__saldo += valor  
        self.__historico.append(valor) 
        self.__index += 1

    def saldo(self):
        return self.__saldo  

    def nome(self):
        return self.__nome    

    def __iter__(self):
        return self 

    def __next__(self): 
        if self.__index == 0:
            raise StopIteration
        self.__index = self.__index - 1   
        return self.__historico[self.__index]

    def __str__(self):
        return f"Correntista: {self.__nome}\nSaldo: {self.__saldo}"

c = Correntista("Maria", 500.00)

print(c)

print(c.nome())
print(c.saldo())
c.deposito(25.50)
print(c.saldo())
c.saque(50.0)
c.saque(5000.0)
print(c.saldo())
print("------ Histórico ------")

for hist in c:
   print(hist)

