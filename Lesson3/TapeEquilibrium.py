# Uma matriz não vazia A que consiste em N números inteiros é fornecida. A matriz A representa números em uma fita.
#
# Qualquer número inteiro P, tal que 0 <P <N, divide esta fita em duas partes não vazias: A [0], A [1], ...,
# A [P - 1] e A [P], A [ P + 1], ..., A [N - 1].
#
# A diferença entre as duas partes é o valor de: | (A [0] + A [1] + ... + A [P - 1]) - (A [P] + A [P + 1] + .. . + A [N - 1]) |
#
# Em outras palavras, é a diferença absoluta entre a soma da primeira parte e a soma da segunda parte.
#
# Por exemplo, considere a matriz A de modo que:
#
#   A [0] = 3
#   A [1] = 1
#   A [2] = 2
#   A [3] = 4
#   A [4] = 3
# Podemos dividir esta fita em quatro lugares:
#
# P = 1, diferença = | 3 - 10 | = 7 # o P é onde a lista vai ser fatiada/cortada
# P = 2, diferença = | 4 - 9 | = 5
# P = 3, diferença = | 6 - 7 | = 1
# P = 4, diferença = | 10 - 3 | = 7
# Escreva uma função:
#
# solução def (A)
#
# que, dada uma matriz não vazia A de N números inteiros, retorna a diferença mínima que pode ser alcançada.
#
# Por exemplo, dado:
#
#   A [0] = 3
#   A [1] = 1
#   A [2] = 2
#   A [3] = 4
#   A [4] = 3
# a função deve retornar 1, conforme explicado acima.
#
# Escreva um algoritmo eficiente para as seguintes suposições:
#
# N é um número inteiro dentro do intervalo [ 2 .. 100.000 ];
# cada elemento da matriz A é um número inteiro dentro do intervalo [ -1.000 .. 1.000 ].

# função abs ela retorna o valor absoluto do número que foi especificado

a = [3,1,2,4,3]
def solution(a):
    corte1 = a[0] # corta a primeira fatia da lista a = [0]
    corte2 = sum(a[1:]) # soma as fatias restantes da lista a partir da posição 1
    diferenca_minima = abs(corte1 - corte2) # tiro o a[0] - a soma da do segundo corte(o que restou da lista)
    for item in range(1, len(a)-1): # pega a partir do primeiro índice, passa por toda a lista e corta novamente o primeiro item da lista
        corte1 += a[item]
        corte2 -= a[item]
        if abs(corte1 - corte2) < diferenca_minima:# a função abs retorna o valor absoluto do número que foi dado, no caso corte1 - corte2
            diferenca_minima = abs(corte1 - corte2)
    return diferenca_minima

print(solution(a))

