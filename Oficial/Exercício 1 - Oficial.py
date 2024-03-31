num1 = int(input('Insira um número de 0 ao 9999 que irei fazer a soma dos: '))

import sys
if num1 > 9999 or num1 < 0:
    print('O número inserido é inválido')
    sys.exit()

soma = 0
soma += num1 % 10
num1 //= 10
soma += num1 % 10
num1 //= 10
soma += num1 % 10
num1 //= 10
soma += num1 % 10

print(f'A soma dos números foi : {soma}')