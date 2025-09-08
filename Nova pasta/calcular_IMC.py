nome = input ('Digite o seu nome:')
idade =int (input("Digite a sua idade:"))
altura = float (input ('Digite a sua altura (em metros) :'))
peso = float (input ('Digite seu peso (em kg): '))

imc = peso / (altura *altura)

print ( "Olá, " + nome + "! Você tem "+ str(idade) + " anos.")
print ("Seu IMC é: " + str (imc))