#Escribe un programa que simule una caja registradora: el usuario ingresa precios de
#productos de a uno. Cuando ingresa 0, el programa se detiene y muestra el total
#acumulado. Nota: utilizá la sentencia break cuando haga falta.

total=0

while True:
  
  precio=float(input('INGRESE EL PRECIO DEL PRODUCTO:'))

  if precio == 0:

    break
  
  total+=precio

print(f'el precio total de los productos es {total}') 