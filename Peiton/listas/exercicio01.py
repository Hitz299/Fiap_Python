'''
    Escreva um programa que crie uma lista de 10 elementos e imprima o maior, 
    o menor e soma de todos os elementos da lista
'''


lista = (3434, 4, 2232, 65, 21, 7, 100, 232, 7, 9)

soma_elementos = 0
elemento_posterior = lista[1]
maior_elemento = lista[0]
menor_elmento = lista[0]

for i in lista:
    soma_elementos += i
    
    if i  > maior_elemento:
        maior_elemento = i
    
    if i < menor_elmento:
        menor_elmento = i
        
    while elemento_posterior <= 10:
        elemento_posterior += 1
    
    
    
print(f"O maior elemneto é {maior_elemento} e o menor é {menor_elmento}")
print(f"\nA soma de todos os elementos de sua lista\n é igual a -> {soma_elementos}")