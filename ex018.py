from math import radians, sin, cos, tan
an = float(input('Digite o angulo que você deseja: '))
seno = sin(radians(an))
cos = cos(radians(an))
tg = tan(radians(an))
print('O ângulo de {} tem: \nSENO: {:.2f}\nCOSSENO: {:.2f}\nTANGENTE: {:.2f}'.format(an,seno,cos,tg))
