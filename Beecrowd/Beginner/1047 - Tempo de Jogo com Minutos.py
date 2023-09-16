horaInicial, minInicial, horaFinal, minFinal = map(int, input().split())
tempoInicial = horaInicial * 60 + minInicial
tempoFinal = horaFinal * 60 + minFinal
diferenca = tempoFinal - tempoInicial

if diferenca <= 0:
    diferenca += 24 * 60

horas = diferenca // 60
minutos = diferenca % 60

print(f"O JOGO DUROU {horas} HORA(S) E {minutos} MINUTO(S)")