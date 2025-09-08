#Contador de vogais

def contador_vogais():
    texto = input("Digite um texto:")
    vogais = "aeiouAEIOU"
    contador = 0
    
    for letra in texto:
        if letra in vogais:
            contador += 1
    print("Quantidade de vogais:", contador)


contador_vogais()