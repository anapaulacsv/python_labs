#Parametros definidos com o formato **paramentro recebem um dicionario com todas as definições por 
#keywords passadas como argumento na chamada função.

def func_var_keyword(param, **keywords):
    print("param:", param)
    for kw in keywords:
        print(kw,":", keywords[kw])

func_var_keyword("test",
    keyword_a="Value A",
    keyword_b="Value B",
    keyword_c="Value C")

#Retorna um dicionario