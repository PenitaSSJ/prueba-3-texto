with open ("elpepe.txt") as texto:
    texto = texto.read()

cantidad_letras = len(texto.replace(' ',''))
cantidad_espacios = texto.count(' ')

print("El texto tiene: ",cantidad_letras)
print("La cantiada de espacios que tiene: ",cantidad_espacios)
# N es igual a que escriba el texto debajo no alao
with open("cantidadde.txt","w") as texto1:
    texto1.write("La cantidad de letras que tiene el texto son: {}\n".format(cantidad_letras))
    texto1.write("La cantidad de espacios que tiene el texto son: {}".format(cantidad_espacios))
    

    
print (texto)