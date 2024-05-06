def menu():
    print('*-* Menu *-*')
    print("1 - Adição")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    opcao = int(input("Esocolha a opreção: "))
    opcao = entrada_invalida(opcao)
    return opcao
  
def entrada_invalida(opcao):
     while opcao < 1 or opcao > 4:
        opcao = int(input("entrada inválida: "))
     return opcao

def entrada_dados():
    print("*-* Entrada de dados *-*")
    numero = int(input("Número: "))
    return numero

def adicao(num1, num2):
    print("*-* Adição *-*")
    result = num1 + num2
    return result

def subtracao(num1, num2):
    print("*-* Subtração *-*")
    result = num1 - num2
    return result

def multiplicacao(num1, num2):
    print("*-* Multiplicação *-*")
    result = num1 * num2
    return result

def divisao(num1, num2):
    print("*-* Divisão *-*")
    result = num1 - num2
    return result

def imprimir(result):
    print("*-* Imprimir *-*")
    print(f"Resultado: {result}")

def controlador(opcao, n1, n2):
    print("*-* Controlador *-*")
    match opcao:
        case 1 : result = adicao(n1, n2)
        case 2 : result = subtracao(n1, n2)
        case 3 : result = multiplicacao(n1, n2)
        case 4 : result = divisao(n1, n2)
    return result

# Principal
x = menu()
n1 = entrada_dados()
n2 = entrada_dados()
result = controlador(x, n1, n2)
imprimir(result)
