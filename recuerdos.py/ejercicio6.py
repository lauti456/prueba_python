#Modifica el ejercicio 4 para que, en lugar de imprimir los números, genere dos listas:
#una con los múltiplos de 5 y otra con el resto de los números. Imprimí ambas listas al
#finalizar.

n=int(input('ingrese un numero hastal el que contar'))

list5=[]
listO=[]

for i in range(1,n+1):
  
  if i%5==0:
   list5.append(i)

  else:
   
   listO.append(i)

   continue 

print(f'los multiplos de 5 son {list5}')
print(f'los no multiplos de 5 son {listO}')

