import math
import inicio

def calculo_area():
    while True:
        infoUser = int(input("+--------------------------------+\n"
                             "|   Calculo geometria espacial   |\n"
                             "|1- Cilindro                     |\n"
                             "|2- Cone                         |\n"
                             "|3- Esfera                       |\n"
                             "|4- Sair e voltar ao menu        |\n"
                             "+--------------------------------+\n"))
        if(infoUser == 1):
            cilindro()
            break
        elif(infoUser == 2):
            cone()
            break
        elif(infoUser == 3):
            esfera()
            break
        elif(infoUser == 4):
            inicio.menu()
            break
        else:
            print("Opção invalida")

def cilindro():
    while True:
        print("***CILINDRO***")
        cilindro = int(input("1- Area das bases \n"
                             "2- Area lateral   \n"
                             "3- Volume         \n"
                             "4- Voltar         \n"))
        if (cilindro == 1):
            raio = float(input("Qual o valor do raio: "))
            res_cil = math.pi * (raio ** 2)
            print(f"A area das bases é igual a {round(res_cil, 2)}")
            calculo_area()
            break
        elif (cilindro == 2):
            raio = float(input("Digite o valor do raio: "))
            alt_cil = float(input("Digite a altura: "))
            rsl_cld = (2 * math.pi) * (raio * alt_cil)
            print(f"A area lateral é {round(rsl_cld, 2)}")
            calculo_area()
            break
        elif (cilindro == 3):
            raio = float(input("Digite o valor do raio: "))
            alt_cil = float(input("Digite a altura: "))
            volume = math.pi * raio * alt_cil
            print(f"O volume do cilindro é {round(volume, 2)}³")
            calculo_area()
            break
        elif (cilindro == 4):
            calculo_area()
            break
        else:
            print("Opção invalida")
            break

def cone():
    while True:
        print("***CONE***")
        cone = int(input("1- Area da base   \n"
                         "2- Area lateral   \n"
                         "3- Volume         \n"
                         "4- area total     \n"
                         "5- Voltar         \n"))
        if(cone == 1):
            raio = float(input("Qual o raio da base: "))
            rst_cone = math.pi * raio
            print(f"A area da base é {round(rst_cone, 2)}")
            calculo_area()
            break
        elif(cone == 2):
            raio = float(input("Qual o raio da base: "))
            gera = float(input("Qual a geratriz do cone: "))
            rst_lateral = math.pi * raio * gera
            print(f"A area lateral é {round(rst_lateral, 2)}")
            calculo_area()
            break
        elif(cone == 3):
            altura = float(input("Qual a altura do cone: "))
            base_area = float(input("Qual a area da base do cone: "))
            rst_vol = (base_area * altura) / 3
            print(f"O volume do cone é {round(rst_vol, 2)}³")
            calculo_area()
            break
        else:
            print("Opção invalida, digite novamente")
            break

def esfera():
    while True:
        print("***ESFERA***")
        esfera = int(input("1- Area total   \n"
                           "2- Volume       \n"
                           "3- Voltar       \n"))
        if(esfera == 1):
            raio = float(input("Digite o valor do raio: "))
            rsl_area = (4 * math.pi * (raio ** (1/2)))
            print(f"O valor da area é {round(rsl_area, 2)}")
            calculo_area()
            break
        elif(esfera == 2):
            raio = float(input("Digite o raio da esfera: "))
            rsultado_volume = ((4 * math.pi) * raio ** (1/3)) / 3
            print(f"O volume é igual a {round(rsultado_volume, 2)}³")
            calculo_area()
            break
        elif(esfera == 3):
            calculo_area()
            break
        else:
            print("Opção invalida!!")
            break

if(__name__ == "__main__"):
    calculo_area()