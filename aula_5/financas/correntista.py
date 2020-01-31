
class Correntista:

    def __init__(self,nome,cpf,saldo,auditor):
        self.__nome = nome
        self.__cpf = cpf 
        self.__saldo = saldo

        auditor.auditar(cpf,'Deposito',saldo)    

    def deposita(self,valor,auditor):
        if not isinstance(valor,float):
            raise TypeError("Valor incorreto.")
        if valor <= 0.0: 
            raise ValueError("Valor do deposito não pode ser menor ou igual a zero.")
        self.__saldo += valor  
        auditor.auditar(self.__cpf,'Deposito',valor) 

    def saldo(self):
        return self.__saldo  

    def nome(self):
        return self.__nome    

    def cpf(self):
        return self.__cpf         

    def __str__(self):
        return f"Correntista: {self.__nome}\nSaldo: {self.__saldo}"

    def saque(self,valor,auditor):
        if not isinstance(valor,float):
            raise TypeError("Valor incorreto.")
        if valor <= 0.0: 
            raise ValueError("Valor do saque não pode ser menor ou igual a zero.")
        if (valor > self.__saldo):
            raise ValueError("Saldo insuficiente!") 
        else:     
            self.__saldo -= valor

            auditor.auditar(self.__cpf,'Saque',valor)    
