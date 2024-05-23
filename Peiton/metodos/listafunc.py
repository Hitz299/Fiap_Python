def tamanho_lista():
    print('**- Tamanho da LISTA -**')
    print('------------------------')
    tamanho = int(input('Tamanho: '))
    return tamanho
 
def criar_lista(tamanho):
    print(f'**- Criando uma LISTA com {tamanho} elementos -**')
    print('--------------------------------------------------')
    lista = [] #criando uma lista vazia
    i = 0
    while i < tamanho:
        num = int(input('Números: '))
        lista.append(num)
        i+=1
    return lista    
 
def imprimir(lista):
    print('**- Imprimindo a LISTA -**')
    print('--------------------------')
    for n in lista:
        print(f'Elemento: {n}')
 
#criar uma função para somar todos os elementos
# da lista
def somatorio(lista):
    print('**- Somatório -**')
    print('-----------------')
    soma = 0 #variavel acumuladora
    #percorre a lista (elemento por elemento)
    for n in lista:
        soma+=n #acumula a soma
    return soma
 
#criar uma função que verifique o número ocorrências
# de determinado número em uma lista
def verificar_ocorrencias(n, lista):
    print('**- Verificar Ocorrências -**')
    print('-----------------------------')
    cont = 0
    for i in lista:
        if i == n:
            cont+=1
    return cont
 
#Principal
tamanho = tamanho_lista()
lista = criar_lista(tamanho)
imprimir(lista)
print(f'Soma: {somatorio(lista)}')
n = int(input('Número: '))
print(f'Ocorrências de {n} na lista: {verificar_ocorrencias(n, lista)}')