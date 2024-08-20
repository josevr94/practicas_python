# sobre escribiendo el archivo (se sobre escribe por el metodo w)
with open("file/ejemplo.txt", 'w') as archivo:
    archivo.write("Hola desde santiago de chile\n")
    archivo.write("Esta es una linea nueva\n")
    archivo.write("aqui estuvo jose")
    
#leer archivo y mostrar el archivo en la consola 
with open("file/ejemplo.txt", "r") as lectura:
    contenido = lectura.read()
    print(contenido)    
    
# usando el metdo A 
with open("file/ejemplo.txt", "a") as  f:
    f.write("\nEsta es una nueva linea al fina del archivo") 
    
#leemos el archivo    
with open("file/ejemplo.txt", "r") as lectura:
    contenido = lectura.read()
    print(contenido)       