import random
 


def compara(jogo, sorteado):
    igual = False
    for j in range(len(jogo)):
            if jogo[j] == sorteado:
                igual = True
                break
    return igual


 
def gerador(tipo,numJogos, dezenas): #Função que gera os jogos
    maisSorteadosSena = [4,10,1,38, 41, 56, 10, 53, 5, 40, 22, 32, 44, 58,59, 15, 30, 33, 34, 47, 55, 28, 35, 39, 46, 51, 52, 57, 2, 13, 14, 15, 16, 19, 25, 31, 36, 40, 42]
    maisSorteadosLoto=range(1,25)
    jogo = []
     
    for i in range(numJogos):
        if tipo == 1:
            numeros_aleatorios = random.sample(maisSorteadosSena, dezenas)
        else:
            numeros_aleatorios= random.sample(maisSorteadosLoto,dezenas)    
        numeros_aleatorios.sort() # Organiza os números em ordem crescente
     
        if len(jogo) == 0:
                jogo.append(numeros_aleatorios)
        else:
            if compara(jogo, numeros_aleatorios) == False:
                jogo.append(numeros_aleatorios)
            else:
                while compara(jogo, numeros_aleatorios) == True:
                    if tipo == 1:
                        numeros_aleatorios = random.sample(maisSorteadosSena, dezenas)
                    else:
                        numeros_aleatorios = random.sample(maisSorteadosLoto, dezenas)     
                jogo.append(numeros_aleatorios)
                     
    return jogo

tipo = eval(input('Megasena[1] ou Lotofacil[2]:')) 
num = eval(input('Entre com o número de apostas:'))
dez = eval(input('Entre com o número de dezenas:'))
 
k = gerador(tipo,num, dez)
 
for i in range(num):
    print ('Jogo', i, k[i])