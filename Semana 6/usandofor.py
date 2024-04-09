def soma_elementos_emlista():
    lista = [1, 4, 3, 4, 5]
    soma = 0
        
    for i in lista:  #A variável i é uma variável temporária que assume o valor de cada elemento da lista em cada iteração do loop for
        soma += i    #Acumulando valor para realizar a soma
    return soma

    print("A soma dos elementos da lista é:", resultado)


def soma_elementos_impares():
    soma = 0
    
    for x in range(1, 100):  #leitura: para x que assume os valores do intervalo de 1 a 100 em cada iteração #A palavra reservada range é pra uma sequência de números
        if x % 2 != 0:
            soma = soma + x
        
    print("O valor da soma dos elementos é: ", soma)
    


def soma_elementos_comstep():
    soma = 0
    
    for x in range(1, 100, 2):  #leitura: para x que assume os valores do intervalo de 1 a 100 em cada iteração #A palavra reservada range é pra uma sequência de números
            soma = soma + x
        
    print("O valor da soma dos elementos é: ", soma)
    

