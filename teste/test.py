numero = int(input ("Digite um numero : "))
if numero % 2 ==0 :
    print( " O numero é par")
else :
   print ("O numero é ímpar")
    
    #nota

nota = float(input("Digite a nota : "))
if nota >= 7:
    print ("Aprovado")
elif nota >= 5 and nota <= 6.9:
    print  ("Recuperação")
else : 
    print  ("Reprovado")
    
    
idade = float (input("Digite a idade : "))
if idade <= 12 :
    print ("Criança")
elif idade >= 13 and idade <= 17 :
    print ("Adolescente")
elif idade >= 18 and idade <= 64:
    print ("Adulto")
else:
    print ("Idoso")
    

for i in range (1, 11):
    print (i)
    
    