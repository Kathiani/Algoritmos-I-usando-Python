
def usandowhile():
# Definindo uma variável de controle
    contador = 1

# Usando a estrutura while para imprimir números de 1 a 5 #Aqui dependendo da necessidade pode-se configurar para nenhuma iteração é executada, por exemplo, contador > 5
    while contador <= 5:
        print("contador assumindo o valor de: ***" , contador)
        contador += 1  # incrementando contador



def usandowhile_combrake():
# Definindo uma variável de controle
    contador = 1

    while contador <= 5:
        print("contador assumindo o valor de: ***" , contador)
        contador += 1  # incrementando contador
        break          # fluxo continua no próximo bloco não identado
    print("contador assumindo o valor de: ***" , contador)

    
    
def usandowhile_comcontinue():
# Definindo uma variável de controle
    contador = 1

    while contador <= 5:
        print("contador assumindo o valor de: ***" , contador)        
        contador += 2  # incrementando contador
        continue      # ignora o resto do código dentro do loop e avança para a próxima iteração do loop
        contador += 2


         
def usandowhile_compass():
# Definindo uma variável de controle
    contador = 1

    while contador <= 10:
        print("contador assumindo o valor de: ***" , contador)        
        contador += 1  # incrementando contador
        pass     # não executa tarefa apenas compõe uma função em caso de necessidade apenas de sua chamada no código (por exemplo, para implementtação posterior),
        contador += 2  # incrementando contador
         
