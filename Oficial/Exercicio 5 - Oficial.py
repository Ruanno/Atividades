min = int(input("Insira quantos minutos voce ficou estacionado: "))

horas = min // 60
if min % 60 > 0:
    horas += 1

valortotal = 0

if horas <= 2:
    valortotal = horas * 8
elif horas <= 4:
    valortotal = 16 + (horas - 2) * 5
elif horas <= 12:
    valortotal = 26 + (horas - 4) * 3
else:
    valortotal = 30

print(f"O valor a ser pago é: R${valortotal:.2f}")