segundos_totales = int(input('ingrese una cant de segundos'))
hora = segundos_totales // 3600
minutos = (segundos_totales%3600)//60
segundos = segundos_totales%60

print (f'{segundos_totales}, segundos son {hora}, {minutos} minutos y {segundos} segundos ')