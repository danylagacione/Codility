
# É fornecida uma matriz A que consiste em N números inteiros diferentes.
# A matriz contém números inteiros no intervalo [1 .. (N + 1)], o que significa que exatamente um elemento está ausente.
#
# Seu objetivo é encontrar esse elemento que está faltando.
#
# Escreva uma função:
#
# solução def (A)
#
# que, dada uma matriz A, retorna o valor do elemento ausente.
#
# Por exemplo, dada a matriz A de modo que:
#Intervalo [1 .. (N + 1)]
#
#   A [0] = 2
#   A [1] = 3
#   A [2] = 1
#   A [3] = 5
# a função deve retornar 4, pois é o elemento que falta.
#
# Escreva um algoritmo eficiente para as seguintes suposições:
#
# N é um número inteiro dentro do intervalo [ 0 .. 100.000 ];
# os elementos de A são todos distintos;
# cada elemento da matriz A é um número inteiro dentro do intervalo [1 .. (N + 1)].
# Encontrar o elemento que falta em uma determinada permutação.
#soma (A) e N (N + 1) / 2  ou ((N + 1)*(N + 2))/2

A = [2,3,1,5]
def solution (A : list):
    lista = set(A)
    N = len(lista)
    for i in range(N):
        total1 = ((N + 1) * (N+2))
        div = total1 // 2
        total = div[i]
    return total

print(solution(A))