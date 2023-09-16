diaInicial = input().split()
horaInicial = input().split()
diaFinal = input().split()
horaFinal = input().split()

segundoInicial = int(diaInicial[1]) * 86400 + int(horaInicial[0]) * 3600 + int(horaInicial[2]) * 60 + int(horaInicial[4])
segundoFinal = int(diaFinal[1]) * 86400 + int(horaFinal[0]) * 3600 + int(horaFinal[2]) * 60 + int(horaFinal[4])
duracao = segundoFinal - segundoInicial

dias = duracao // 86400
duracao %= 86400

horas = duracao // 3600
duracao %= 3600

minutos = duracao // 60
duracao %= 60

segundos = duracao  

print(f'{dias} dia(s)')
print(f'{horas} hora(s)')
print(f'{minutos} minuto(s)')
print(f'{segundos} segundo(s)')