import math
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
h = math.hypot(co,ca)
print('A hipotenusa do triângulo é {:.2f}'.format(h))
