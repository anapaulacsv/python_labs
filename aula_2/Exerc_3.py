#Gerar uma lista que retorne outra lista com a quantidade de itens conforme digitado na entrada.

def lista(x):
    w = []
    
    for i in range(x):
        w.append(list(range(x)))
        
    return w 

print(lista(int (input("Informe o numero de grupo e seu tamanho: "))))



