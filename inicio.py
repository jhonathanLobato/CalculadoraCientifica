import geometriaEspacial
import geometriaPlana
import operacao_Basica
import trigonometria

def menu():
    while True:
        infoUsuario = int(input("+----------------------------------------+\n"
                                "|        Calculadora Cientifica          |\n"
                                "|  *Qual operação você deseja executar*  |\n"
                                "|1- Adição                               |\n"
                                "|2- Subtração                            |\n"
                                "|3- Multiplicação                        |\n"
                                "|4- Divisão                              |\n"
                                "|5- Fatoração                            |\n"
                                "|6- Potenciação                          |\n"
                                "|7- Seno                                 |\n"
                                "|8- Cosseno                              |\n"
                                "|9- Tangente                             |\n"
                                "|10- Logaritmo                           |\n"
                                "|11- Calculo da geometria plana          |\n"
                                "|12- Calculo da geometria espacial       |\n"
                                "|13- Finalizar                           |\n"
                                "+----------------------------------------+\n"))
        if(infoUsuario == 1):
            operacao_Basica.soma()
            break
        elif(infoUsuario == 2):
            operacao_Basica.subtracao()
            break
        elif(infoUsuario == 3):
            operacao_Basica.multiplicacao()
            break
        elif(infoUsuario == 4):
            operacao_Basica.divisao()
            break
        elif (infoUsuario == 5):
            operacao_Basica.fatoracao()
            break
        elif (infoUsuario == 6):
            operacao_Basica.potencia()
            break
        elif (infoUsuario == 7):
            trigonometria.seno()
            break
        elif (infoUsuario == 8):
            trigonometria.cos()
            break
        elif (infoUsuario == 9):
            trigonometria.tan()
            break
        elif (infoUsuario == 10):
            trigonometria.log()
            break
        elif (infoUsuario == 11):
            geometriaPlana.calculo_area()
            break
        elif(infoUsuario == 12):
            geometriaEspacial.calculo_area()
            break
        elif(infoUsuario == 13):
            break
        else:
            print("Opcao errada, digite novamente!!!\n")

if(__name__ == "__main__"):
    menu()
