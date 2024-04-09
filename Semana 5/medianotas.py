def medianotas():

    # Solicita ao usuário para inserir os valores das notas
    N1 = float(input("Digite o valor da primeira nota: "))
    N2 = float(input("Digite o valor da segunda nota: "))

    # Calcula a média ponderada usando a fórmula fornecida
    media = 0.4 * N1 + 0.6 * N2

    # Imprime o resultado
    if media >=5:
     print("A média ponderada é igual a:", media, " e o aluno está Aprovado!!")
    else:
     print("Reprovado!")
