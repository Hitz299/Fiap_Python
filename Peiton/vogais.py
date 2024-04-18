'''
Escreva um programa que leia 5 nomes e exiba os nome que começam com vogal
'''

nomes = ("Renato", "kleber", "Estela", "Pedro", "Aroldo", "Renan", "Uesley")

vogais = ('A', 'E', 'I', 'O', 'U')

for nome in nomes:
    for i in vogais:
        if i == nome[0]:
            print(nome, end=' ')
         
    
    
