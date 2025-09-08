def calculadora ():
    num1 = float(input("Digite o primeiro numero desejado : "))
    num2 = float(input("Digite o segundo numero desejado : "))
    operador = input("Escolha uma operaçao: +, *, -, /")
    if operador == "+":
        print (" O resultador da operação é :", num1 + num2)
    elif operador == "*":
        print ("O resultador da operação é :", num1 * num2)
    elif operador == "-":
        print ("O resultado da operação é :", num1 - num2)
    elif operador == "/":
        if num2 != 0:
            print(" O resultador da operação é :", num1 / num2) 
        else:
            print (" O numero não poder ser divido por 0")
    else:
        print("Operador inválido.")

calculadora()