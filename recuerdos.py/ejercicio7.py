p=input('escriba una oracion:')
palabras = p.split()

palabras_largas=[]
for i in palabras:
    if len(i) > 3:
        palabras_largas.append(i)
oracion = " ".join(palabras_largas)
print(f'oracion final:{oracion}')
