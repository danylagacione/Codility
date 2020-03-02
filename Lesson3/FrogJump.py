# Um sapo pequeno quer chegar ao outro lado da estrada.
# O sapo está atualmente localizado na posição X e deseja chegar a uma posição maior ou igual a Y.
# O sapo pequeno sempre pula uma distância fixa, D.
#
# Conte o número mínimo de saltos que o sapo pequeno deve realizar para atingir seu objetivo.
#
# Escreva uma função:
#
# solução def (X, Y, D)
#
# que, dados três números inteiros X, Y e D, retorne o número mínimo de saltos da posição X para uma posição igual ou superior a Y.
#
# Por exemplo, dado:
#
#   X = 10
#   Y = 85
#   D = 30
# a função deve retornar 3, porque o sapo será posicionado da seguinte maneira:
#
# após o primeiro salto, na posição 10 + 30 = 40
# após o segundo salto, na posição 10 + 30 + 30 = 70
# após o terceiro salto, na posição 10 + 30 + 30 + 30 = 100
# Escreva um algoritmo eficiente para as seguintes suposições:
#
# X, Y e D são inteiros dentro do intervalo [ 1 .. 1.000.000.000 ];
# X ≤ Y.
# x = posição inicial
# y = posição que deseja chegar ou posição maior
# d = distância fixa que o sapo pula
#   X = 10
#   Y = 85
#   D = 30

# def solution(x, y, d):
#     if  ( x == y): # se a posição inicial for igual a que deseja chegar ele não pula
#       pulos = 0
#     elif (y - x) / d == 0:
#       pulos = y - x % d
#     else:
#       pulos = ((y - x) / d) + 1 # soma + 1 para ele pular
#     return pulos
#
# print (solution(10,85,30))

def solution(x, y, d):
  # if x == y: # esse if é desnecessário, pois ele não precisa verificar se está no mesmo lugar
  #   pulo = 0
  #   return pulo
  diferenca = y - x
  pulos = diferenca // d
  if diferenca % d != 0:
    return pulos + 1
  return pulos

print (solution(10,85,30))