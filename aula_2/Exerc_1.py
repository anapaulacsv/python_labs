#Crie uma função que receba uma lista e retorne uma lista apenas com elementos únicos (remova os duplicados).

def dup(list=[1,1,5,6,6,5,6,2,8]):
    x = []
    for z in list[:]:
        exist = False
        for y in x:
            if z == y:
                exist = True
        if exist == False:
            x.append(z)
    return x

print(dup())