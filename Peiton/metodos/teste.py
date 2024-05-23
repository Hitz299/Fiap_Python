'''
def erro_entrada(entrada):
    while entrada != 1 and entrada != 2:
        entrada = int(input("Entrada inválida\n"))
    return entrada


escolha = int(input("Digite um valor para realizar sua escolha:\n" +
          "1-> sim\n2-> não\n"))

escolha = erro_entrada(escolha)

if escolha == 1:
    print("Sim")

if escolha == 2:
    print("Não")

'''

def criar_matriz(n_linhas, n_colunas, valor):
    '''
    Função criar_matriz -> cria uma matriz com base no 
    número de linhas e colunas fornecidas por parâmetro
 
    Parâmetros:
    - n_linhas - número de linhas
    - n_colunas - número de colunas
 
    Retorno:
    - matriz - retorna uma matriz com elementos
    inseridos pelo usuário
    '''
 
    #criar uma matriz (lista principal)
    matriz = [] #lista vazia
 
    for i in range(n_linhas):
        #criar a linha i
        linha = []
        for j in range(n_colunas):
            linha.append(valor)
        #adicionando a linha à matriz
        matriz.append(linha)
    return matriz
#principal
M = criar_matriz(3, 5, 0)
M[2][2] = 1000
M[0][2] = 543
print(M)