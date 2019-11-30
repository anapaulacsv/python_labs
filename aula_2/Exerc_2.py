#Crie uma função que recebe uma string e a retorna ao contrario (ex: ABC123 -> 321CBA)

def contra(a):
    palavra = ""
    for i in a [:]:
        palavra = i + palavra

    return palavra

print(contra('Bolo'))    