
i = 1
f = int(input("Número final: "))

if (f > 0):
    while i <= f: 
        if(i % 2 == 0):
            print(f"{i} é par")
        elif (i % 2 == 1):
            print(f"{i} é impar")
        i += 1

else:
    print("Entrada inválida")