hora_inicial, minuto_inicial = (input('Momento Inicial: ')).split(':')
hora_final, minuto_final = (input('Momento de Chegada: ')).split(':')
segundos_parados = int(input('segundos parados para descanso: '))
litros_combustivel = float(input('Número de litros de combustível gasto (em litros): '))
preco_litro_combustivel = float(input('Preço do litro de combustível (em R$): '))
distancia_percorrida = float(input('Distância percorrida (em Km): '))

#CONVERSÃO DAS VARIAVEIS PARA INTEIRO!!!
hora_inicial = int(hora_inicial)
minuto_inicial = int(minuto_inicial)
hora_final = int(hora_final)
minuto_final = int(minuto_final)
tempo_viagem = ((hora_inicial * 3600)-(hora_final * 3600))-((minuto_inicial * 60)-(minuto_final * 60))
tempo_viagem_com_descanso = tempo_viagem + segundos_parados
#OK

velocidade_media_global = distancia_percorrida / (tempo_viagem_com_descanso / 3600)
velocidade_media_movimento = distancia_percorrida / ((tempo_viagem + segundos_parados) / 3600)

velocidade_media_global = distancia_percorrida / (tempo_viagem / 3600)
velocidade_media_movimento = distancia_percorrida / ((tempo_viagem + segundos_parados) / 3600)
print(f'O tempo de viagem foi: {tempo_viagem_com_descanso} segundos')

print(f'a velocidade média (Km/h) global foi {velocidade_media_global} e a velocidade média em movimento (Km/h) foi {velocidade_media_movimento}')



