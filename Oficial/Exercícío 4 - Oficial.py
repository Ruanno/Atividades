dia_inic = int(input("Dia inicial: "))
mes_inic = int(input("Mês inicial: "))
dia_final = int(input("Dia final: "))
mes_final = int(input("Mês final: "))

if (mes_inic < mes_final) or (mes_inic == mes_final and dia_inic <= dia_final):
    dias_por_mes = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    dias_decorridos_inicial = sum(dias_por_mes[:mes_inic]) + dia_inic
    dias_decorridos_final = sum(dias_por_mes[:mes_final]) + dia_final
    dias_passados = dias_decorridos_final - dias_decorridos_inicial
    print("Dias decorridos entre as datas:", dias_passados, "dias")
else:
    print("A data inicial é maior que a data final.")