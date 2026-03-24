#ingresar palabras desde el teclado hasta ingresar la palabra FIN. Imprimir
#aquellas que empiecen y terminen con la misma letra

while True:
      palabra=input('ingrese una palabra:')

      if palabra=='FIN':
        break 
      if palabra[0]==palabra[-1]:
                
         print(palabra)