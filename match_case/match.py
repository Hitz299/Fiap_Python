'''
Estruturas condicionais

match-case
 Aplicado a Strings, caracteres, inteiros
- Usado quando conhecemos as possibilidades de teste




if var_teste == 1 or var_teste == 2 or var_teste == 3...


match var_teste:
       case 1:
       case 2:
       case 3:


Sintaxe:

match var_teste:
    case 1:
        "comandos de bloco 1"
        break  
    case 2:
        comandos de bloco 2
    case 3:
        comandos de bloco 3
    case 4:
        comandos de bloco 4  
    case _:
        comandos de bloco default <opcional>
        
        
        
linguagem = input("Digite qual linguagem de programação você tem interesse em aprender: ")

match linguagem:
        case "javascript":
            print(f"{linguagem} é uma ótima opção para se aprender, " +
                  "principalmente para desenvolvimento web")
        case "c#":
            print(f"{linguagem} é uma ótima opção para se aprender," +
                  "principalmente para desenvolvimento back-end")
        # Default
        case _:
            print("Entrada inválida")
            
print("Agpra vai  estudar essa porra de linguagem")

'''