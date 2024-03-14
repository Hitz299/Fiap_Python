
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

