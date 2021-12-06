import math
import inicio

def calculo_area():
    while True:
        infoUser = int(input("+-----------------------------+\n"
                             "|       Calculo de area       |\n"
                             "|1- Area do quadrado          |\n"
                             "|2- Area do retangulo         |\n"
                             "|3- Area do triangulo         |\n"
                             "|4- Area do trapezio          |\n"
                             "|5- Area do lozango           |\n"
                             "|6- Area do circulo           |\n"
                             "|7- Sair e volta ao menu      |\n"                         
                             "+-----------------------------+\n"))
        if(infoUser == 1):
            quadrado()
            break
        elif(infoUser == 2):
            retangulo()
            break
        elif(infoUser == 3):
            triangulo()
            break
        elif(infoUser == 4):
            trapezio()
            break
        elif(infoUser == 5):
            lozango()
            break
        elif(infoUser == 6):
            circulo()
            break
        elif(infoUser == 7):
            inicio.menu()
            break
        else:
            print("Você digitou incorretamente, por favor digite o numero corresponte")

def quadrado():
    print("***QUADRADO***")
    base_quadr = float(input("Digite o valor da base: "))
    resultado_quadr = base_quadr ** 2
    print(f"A area do quadrado é {round(resultado_quadr, 2)}²")
    while True:
        user = int(input("Deseja fazer fazer outra operção \n"
                         "1- Sim                           \n"
                         "2- Voltar ao menu                \n"))
        if (user == 1):
            quadrado()
            break
        elif (user == 2):
            inicio.menu()
            break
        else:
            print("Opção invalida, digite novamente")
def retangulo():
    print("***RETANGULO***")
    base_retan = float(input("Digite o valor da base: "))
    altu_retan = float(input("Digite o valor da altura: "))
    resul_retan = base_retan * altu_retan
    print(f"A area do retangulo é {round(resul_retan, 2)}²")
    while True:
        user = int(input("Deseja fazer fazer outra operção \n"
                        "1- Sim                           \n"
                        "2- Voltar ao menu                \n"))
        if (user == 1):
            retangulo()
            break
        elif (user == 2):
            inicio.menu()
            break
        else:
            print("Opção invalida, digite novamente")
def triangulo():
    while True:
        trg_user = int(input("Qual o tipo de triangulo  \n"
                            "1- Triangulo comum         \n"
                            "2- Triangulo equilátero    \n"
                            "3- voltar ao menu          \n"))
        if(trg_user == 1):
            base_trc = float(input("Digite o valor da base: "))
            alt_trc = float(input("Digite o valor da altura: "))
            area_trc = (base_trc * alt_trc) / 2
            print(f"A area é {round(area_trc, 2)}²") # esse

        elif(trg_user == 2):    #Triangulo euilatero
            lado_equi = float(input("Qual o valor do lado do triangulo: "))
            area_equi = ((lado_equi ** 2) * math.sqrt(3) / 4)
            print(f"A area é {round(area_equi, 2)}²")

        elif(trg_user == 3):
            calculo_area()

        else:
            print("Opção invalida, digite uma alternativa correta")
def trapezio():
    print("***TRAPEZIO***")
    base_max = float(input("Digite o valor da base maior: "))
    base_min = float(input("Digite o valor da base menor: "))
    alt_trap = float(input("Digite o valor da altura: "))
    rst_tpz = ((base_max + base_min) * alt_trap) / 2
    print(f"A area do trapezio é igual a {round(rst_tpz, 2)}²")
    while True:
        user = int(input("Deseja fazer fazer outra operção \n"
                         "1- Sim                           \n"
                         "2- Voltar ao menu                \n"))
        if (user == 1):
            trapezio()
            break
        elif (user == 2):
            inicio.menu()
            break
        else:
            print("Opção invalida, digite novamente")
def lozango():
    print("***LOZANGO***")
    dig_max = float(input("Qual a diagonal maior: "))
    dig_min = float(input("Qual a diagonal menor: "))
    rst_loza = (dig_max * dig_min) / 2
    print(f"A area do lozango é igual {round(rst_loza, 2)}²")
    while True:
        user = int(input("Deseja fazer fazer outra operção \n"
                         "1- Sim                           \n"
                         "2- Voltar ao menu                \n"))
        if (user == 1):
            lozango()
            break
        elif (user == 2):
            inicio.menu()
            break
        else:
            print("Opção invalida, digite novamente")
def circulo():
    print("***CIRCULO***")
    raio = float(input("Digite o valor do raio: "))
    area_circulo = math.pi * raio
    print(f"A area do circulo é igual a {round(area_circulo, 2)}²")
    while True:
        user = int(input("Deseja fazer fazer outra operção \n"
                         "1- Sim                           \n"
                         "2- Voltar ao menu                \n"))
        if (user == 1):
            circulo()
            break
        elif (user == 2):
            inicio.menu()
            break
        else:
            print("Opção invalida, digite novamente")

if(__name__ == "__main__"):
    calculo_area()