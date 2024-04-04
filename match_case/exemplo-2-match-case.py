
print(f"Digite o dia da semana em que as vendas foram realizadas"+
      "\nSegunda, Terça e quarta -> comissão = 20%"+
      "\nQuinta e Sexta -> comissão = 15%"+
      "\nSábado e Domingo -> comissão = 10%\n")

periodo = input("Digite o  dia: ")
comissao_percentual: int

match periodo:
    case "Segunda" | "Terça" | "Quarta":
        comissao_percentual = 0.20
        print("\nComissão = 20%")
    case "Quinta" | "Sexta":
        comissao_percentual = 0.15
        print("\nComissão = 15%")
    case "Sábado" | "Domingo":
        comissao_percentual = 0.10
        print("\nComissão = 10%")
    case _:
        print(f"\nTá chapando?")
    