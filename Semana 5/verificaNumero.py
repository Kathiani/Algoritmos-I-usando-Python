def verificaNumero():
    # Solicita ao usuário para inserir um número
    numero = float(input("Digite um número: "))

    # Verifica se o número é positivo, negativo ou zero e imprime uma mensagem apropriada
    if numero > 0:
        print("O número é positivo.")
    elif numero < 0:
        print("O número é negativo.")
    else:
        print("O número é zero.")


