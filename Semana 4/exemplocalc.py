def adicao(x, y):
    return x + y

def subtracao(x, y):
    return x - y

def multiplicacao(x, y):
    return x * y

def divisao(x, y):
    if y == 0:
        return "Erro! Divisão por zero não é permitida."
    else:
        return x / y

def processaescolha(escolha):
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))

    if escolha == '1':
       print(num1, "+", num2, "=", adicao(num1, num2))
    elif escolha == '2':
       print(num1, "-", num2, "=", subtracao(num1, num2))
    elif escolha == '3':
       print(num1, "*", num2, "=", multiplicacao(num1, num2))
    elif escolha == '4':
       print(num1, "/", num2, "=", divisao(num1, num2))


#Função Principal
       #Digite no prompt a chamada para a função >>> calculator()
def calculator():
    print("Selecione a operação:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")

    escolha = input("Digite sua escolha (1/2/3/4): ")
    if escolha != '0':
        processaescolha(escolha)

  
