# Loop for aninhado para exibir a tabuada de multiplicação

def tabuada():
    for i in range(1, 11):  # Loop externo para iterar sobre os multiplicadores de 1 a 10
        print(f"Tabuada de {i}:")
    
        for j in range(1, 11):  # Loop interno para iterar sobre os números de 1 a 10 para multiplicação
            produto = i * j
            print(f"{i} * {j} = {produto}")
        print()  # Adiciona uma linha em branco após cada tabuada  # comando fora do segundo for
