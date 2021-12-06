import math
import inicio

def log():
    print("***LOGARITMO***")
    base = float(input("Qual a base: "))
    expo = float(input("Qual o expoente: "))
    result_log = math.log(expo, base)
    print(f"O resultado do log é {round(result_log, 3)}")
    inicio.menu()

def seno():
    print("***SENO***")
    cateto_oposto = float(input("Qual o valor do cateto: "))
    hipote = float(input("Qual o valor da hipotenusa: "))
    resultado_seno = cateto_oposto / hipote
    print(f"O valor do seno é {round(resultado_seno, 2)}")
    inicio.menu()

def cos():
    print("***COSSENO***")
    cateto_adja = float(input("Digite o valor do cateto adjacente: "))
    hipote = float(input("Digite o valor da hipotenusa: "))
    res_cosseno = cateto_adja / hipote
    print(f"O valor é igual a {round(res_cosseno, 2)}")
    inicio.menu()

def tan():
    print("***TANGENTE***")
    cateto_oposto = float(input("Digite o valor do cateto oposto: "))
    cateto_adja = float(input("Digite o valor do cateto adjacente: "))
    res_tan = cateto_oposto / cateto_adja
    print(f"O valor é {round(res_tan, 2)}")
    inicio.menu()
