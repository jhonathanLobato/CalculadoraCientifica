import inicio

def soma():
    print("***SOMA***")
    numero_um = float(input("Qual o primeiro numero: "))
    numero_dois = float(input("Qual o segundo numero: "))
    resultado_soma = numero_um + numero_dois
    print(f"A soma é igual a {round(resultado_soma, 2)}\n")

    while True:
        user_soma = int(input("Deseja fazer fazer outra operção \n"
                              "1- Sim                           \n"
                              "2- Voltar ao menu                \n"))
        if(user_soma == 1):
            soma()
            break
        elif(user_soma == 2):
            inicio.menu()
            break
        else:
            print("Opção invalida, digite novamente")

def subtracao():
    print("***SUBTRAÇÃO***")
    numero_um = float(input("Qual o primeiro numero: "))
    numero_dois = float(input("Qual o segundo numero: "))
    resultado_subtracao = numero_um - numero_dois
    print(f"A subtração é {round(resultado_subtracao, 2)}")
    while True:
        user_sub = int(input("Deseja fazer fazer outra operção \n"
                              "1- Sim                           \n"
                              "2- Voltar ao menu                \n"))
        if (user_sub == 1):
            subtracao()
            break
        elif (user_sub == 2):
            inicio.menu()
            break
        else:
            print("Opção invalida, digite novamente")

def multiplicacao():
    print("***MULTIPLICAÇÃO***")
    numero_um = float(input("Qual o primeiro numero: "))
    numero_dois = float(input("Qual o segundo numero: "))
    resultado_multi = numero_um * numero_dois
    print(f"A multiplicação é igual a {round(resultado_multi, 2)}")
    while True:
        user_mult = int(input("Deseja fazer fazer outra operção \n"
                              "1- Sim                           \n"
                              "2- Voltar ao menu                \n"))
        if (user_mult == 1):
            multiplicacao()
            break
        elif (user_mult == 2):
            inicio.menu()
            break
        else:
            print("Opção invalida, digite novamente")

def divisao():
    print("***DIVISÃO***")
    numero_um = float(input("Qual o primeiro numero: "))
    numero_dois = float(input("Qual o segundo numero: "))
    resultado_divisao = numero_um / numero_dois
    print(f"O valor da divisão é {round(resultado_divisao, 2)}")
    while True:
        user_dv = int(input("Deseja fazer fazer outra operção \n"
                              "1- Sim                           \n"
                              "2- Voltar ao menu                \n"))
        if (user_dv == 1):
            divisao()
            break
        elif (user_dv == 2):
            inicio.menu()
            break
        else:
            print("Opção invalida, digite novamente")

def fatoracao():
    print("***FATORAÇÃO***")
    num_user = int(input('Digite um número inteiro: '))
    total = 1
    for n in range(num_user):
        total = total * (n + 1)         #Talvez isso seja util
    print(f"O resultado da fatoração é igual a {round(total, 2)}")
    while True:
        user_fto = int(input("Deseja fazer fazer outra operção \n"
                              "1- Sim                           \n"
                              "2- Voltar ao menu                \n"))
        if (user_fto == 1):
            fatoracao()
            break
        elif (user_fto == 2):
            inicio.menu()
            break
        else:
            print("Opção invalida, digite novamente")

def potencia():
    print("***POTENCIAÇÃO***")
    base = float(input("Digite o valor da base: "))
    expoente = int(input("Digite o valor do expoente"))

    resultado = base ** expoente
    print(f"O resultado da potencia de {base} elevado a {expoente} é igual a {resultado}")
    while True:
        user_pt = int(input("Deseja fazer fazer outra operção \n"
                              "1- Sim                           \n"
                              "2- Voltar ao menu                \n"))
        if (user_pt == 1):
            potencia()
            break
        elif (user_pt == 2):
            inicio.menu()
            break
        else:
            print("Opção invalida, digite novamente")
