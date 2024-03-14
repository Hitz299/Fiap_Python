
'''
#Exercício 3

altura = float(input("Digite sua altura: "))
peso = float (input("Digite seu peso: "))

imc = peso/(altura * altura)

print(imc)
if (imc < 26.00):
    print(f"Seu imc é {imc: .2f} \n Você está no peso normal")
elif (imc > 26 and imc <= 30):
    print(f"Seu imc é {imc: .2f} Você está obeso")
else:
    print(f"Seu imc é {imc: .2f} Você está com obesidade morbida")
''' 
    
print('Exercício 4')

#print(pow(3,3))

altura = float(input("Digite sua altura: "))
peso = float (input("Digite seu peso: "))

imc = peso/(altura * altura)

sexo = input('Digite seu sexo: ')

print(imc)

if (sexo == "masculino" or sexo == "Masculino" or sexo == "MASCULINO"):
    if (imc < 20.00):
        print(f"Seu imc é {imc: .2f} \n Você está abaixo do peso")
    elif (imc >= 20 and imc <= 24.99):
        print(f"Seu imc é {imc: .2f} Você está no peso normal")
    elif imc >= 25.00 and imc <= 29.99:
        print(f"Seu imc é {imc: .2f} Você está com obesidade leve")
    elif imc >= 30.00 and imc <= 39.99:
        print(f"Seu imc é {imc: .2f} Você está com obesidade moredarada")
    elif imc >= 40.00:
        print(f"Seu imc é {imc: .2f} Você está com obesidade morbida, gordão")
        
if (sexo == "feminino" or sexo == "Feminino" or sexo == "FEMININO"):
    if (imc < 19.00):
        print(f"Seu imc é {imc: .2f} \n Você está abaixo do peso")
    elif (imc >= 19.00 and imc <= 23.99):
        print(f"Seu imc é {imc: .2f} Você está no peso normal")
    elif imc >= 24.00 and imc <= 28.99:
        print(f"Seu imc é {imc: .2f} Você está com obesidade leve")
    elif imc >= 29.00 and imc <= 38.99:
        print(f"Seu imc é {imc: .2f} Você está com obesidade moredarada")
    elif imc >= 39.00:
        print(f"Seu imc é {imc: .2f} Você está com obesidade morbida, gordão")