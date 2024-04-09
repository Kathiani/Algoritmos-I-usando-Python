#Listas Multidimensionais para a resolução de problemas
#Como implementar um programa que precisa armazenar X notas de Y alunos?
#E que além das notas, seu programa precisa armazenar a quantidade de faltas que o aluno teve mensalmente ao longo de todo ano? E que,
#para cada aluno, nome, RG e data de nascimento também precisam ser guardados? 

def armazenaNota1():
    num_alunos = 1  # Defina o número de alunos que deseja armazenar
    alunos = [None] * num_alunos  # Inicializa a lista com uma quantidade suficiente de elementos
    
    for i in range(num_alunos):
        nome = input("Digite o nome: ")
        rg = input("Digite o rg: ")
        datanasc = input("Data de nascimento: ")
        nota1 = int(input("Digite a nota 1 do aluno: "))  # média do bimestre
        nota2 = int(input("Digite a nota 2 do aluno: "))
        nota3 = int(input("Digite a nota 3 do aluno: "))
        nota4 = int(input("Digite a nota 4 do aluno: "))
        faltas = int(input("Digite as faltas obtidas no ano: "))
             
        aluno = [[nome, rg, datanasc], [nota1, nota2, nota3, nota4], faltas] 
        alunos[i] = aluno  # Atribui o aluno à posição i da lista de alunos
    
        print('RG do aluno:', alunos[0][0][1])




        

def armazenaNotas2():
    alunos = []
    
    for i in range(0, 1):
        nome = (input("Digite o nome: "))
        rg = (input("Digite o rg: "))
        datanasc = (input("Data de nascimento: "))
        nota1 = int(input("Digite a nota 1 do aluno: "))  # média do bimestre
        nota2 = int(input("Digite a nota 2 do aluno: "))
        nota3 = int(input("Digite a nota 3 do aluno: "))
        nota4 = int(input("Digite a nota 4 do aluno: "))
        faltas = int(input("Digite as faltas obtidas no ano: "))
             
        aluno =  [[nome, rg, datanasc], [nota1, nota2, nota3, nota4], faltas]
        alunos.append(aluno)
        print('Nome do primeiro aluno:', aluno[0][0]) 

