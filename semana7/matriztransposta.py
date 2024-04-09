
def mtransposta():
    
    matriz = [
        [1, 2, 7], [3, 4, 8]
    ]
     
    print('Matriz inicial: ', matriz)

    linhas = len(matriz)
    colunas = len(matriz[0])
    print('O número de linhas da matriz transposta é:', linhas)
    print('O número de colunas da matriz transposta é:', colunas)

    for i in range(colunas): #3  #6 vezes de repetição de acordo com a quantidade de elementos
        for j in range(i, linhas):    
            print(matriz[i][j]) #printando valor antes da transposição
            temp = matriz[i][j]  
            matriz[i][j] = matriz[j][i]  
            matriz[j][i] = temp
                     
    print('A seguir matriz transposta:') 
    print(matriz)

   
 

