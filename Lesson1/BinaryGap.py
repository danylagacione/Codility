# Um espaço binário dentro de um número inteiro positivo N é qualquer sequência máxima de zeros consecutivos
# que está rodeado por 1 dos dois lados na representação binária de N.
#
# Por exemplo, o número 9 tem representação binária 1001 e contém uma lacuna binária de comprimento 2.
# O número 529 tem representação binária 1000010001 e contém duas lacunas binárias:
# um de comprimento 4 e um de comprimento 3.
# O número 20 tem representação binária 10100 e contém um espaço binário de comprimento 1.
# O número 15 tem representação binária 1111 e não possui lacunas binárias.
# O número 32 tem representação binária 100000 e não possui lacunas binárias.
#
# Escreva uma função:
#
# solução def (N)
#
# que, dado um número inteiro positivo N, retorna o comprimento de seu maior intervalo binário.
# A função deve retornar 0 se N não contiver um espaço binário.
#
# Exemplo, dado N = 1041, a função deve retornar 5,
# porque N tem representação binária 10000010001 e, portanto, seu maior intervalo binário tem o comprimento 5.
#
# Dado N = 32, a função deve retornar 0, porque N tem representação binária '100000'
# e, portanto, sem lacunas binárias.

def solution(N):
    N = (bin(N))
    N = (N[2:])
    N = str(N)
    N = N.strip('0').split('1')
    N = len(max(N))
    return N

print(solution(32))
print(bin(32)[2:])
