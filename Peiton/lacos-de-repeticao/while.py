i = int(input("Início: "))
f = int(input("Fim: "))

if (i < f):
    while i < f:
        print(f"O valor atual de i: {i}")
        i += 1
        print(f"O fim é: {f}")
        
elif (i > f):
    while i > f:
         print(f"O valor atual de i: {i}")
         i -= 1
         print(f"O fim é: {f}")