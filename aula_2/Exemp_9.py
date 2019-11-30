#Funções variádicas 
#Funções podem ser definidas de modo a aceitar um numero arbitrario de argumentos.

def func_variadic(param, *args):
    print("param:", param)
    for arg in args:
        print(arg)

func_variadic("test","More","and","more","arguments")