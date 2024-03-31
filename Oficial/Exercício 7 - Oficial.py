import math
import sys

a = float(input('Insira o comprimento do lado(a) de um triângulo: '))
b = float(input('Insira o comprimento do lado(b) de um triângulo: '))
c = float(input('Insira o comprimento do lado(c) de um triângulo: '))

#Verificador:
if a + b < c and a + c < b and b + c < a:
    print ('Os ângulos informados não formam um triângulo')
    sys.exit()

angulo_1 = math.degrees(math.acos((b**2 + c**2 - a**2)/(2*b*c)))
angulo_2 = math.degrees(math.acos((a**2 + c**2 - b**2)/(2*a*c)))
angulo_3 = 180 - angulo_1 - angulo_2

#A soma dos ângulos tem que dar 180 graus, me deixa.
print('O triângulo possui os respectivos lados: ')
print(f'{round(angulo_1, 2)}°')
print(f'{round(angulo_2, 2)}°')
print(f'{round(angulo_3, 2)}°')
print(70*'-')

if a == b and b == c:
    print('Triângulo Equilátero,')
elif a == b or b == c or a == c:
    print('Triângulo Isósceles,')
else:
    print('Triângulo Escaleno,')

if angulo_1 > 90 or angulo_2 > 90 or angulo_3 > 90:
    print('Ângulo obtuso.')
elif angulo_1 == 90 or angulo_2 == 90 or angulo_3 == 90:
    print('Ângulo retângular.')
else:
    print('Ângulo agudo.')