from vehiculo import Vehiculo
from automovil import Automovil
from automovil_particular import AutomovilParticular
from automovil_carga import AutomovilCarga
from bicicletas import Bicicleta
from motocicletas import Motocicletas
import csv

class Vehiculoscsv: 
    def __init__(self,nombre_archivo = 'practicas_python/modulo4/consolidacion/csv/archivo.csv'):
        self.nombre_archivo = nombre_archivo
        self.vehiculo_particular = []
        self.vehiculo_carga = []
        self.bicicletas = []
        self.motocicletas = []
    
       
    def guardar_datos_csv(self,objeto):
        try:
            with open(self.nombre_archivo, mode = 'a', newline= '') as file:
                dato = [(objeto.__class__, objeto.__dict__)] 
                archivo_csv = csv.writer(file)
                archivo_csv.writerow(dato)
                return print('Archivo guardado')
        
        except FileNotFoundError:
            print('Archivo no entonctrado')       
        
    def leer_archivo(self): #revisar esta parte 
        try:
            with open(self.nombre_archivo, mode="r", newline="") as file:
                lector = csv.reader(file)
                for fila in lector:
                    if 'motocicletas.Motocicletas' in fila:                      
                        self.motocicletas.append(fila) 
                    # if i[0] == 'Motocicletas':
                    #     moto = fila
                    #     self.motocicletas.append(moto) 
                    # if i[0] == 'AutomovilParticular':
                    #     particular = fila
                    #     self.vehiculo_particular.append(particular)
                    # if i[0] == 'AutomovilCarga':
                    #     carga = fila
                    #     self.vehiculo_carga.append(carga)
                    # if i[0] == 'Bicicleta':
                    #     bici = fila
                    #     self.bicicletas.append(bici)
                            
        except FileNotFoundError:
            print('El archivo no fue encontrado')

    def mostrar_datos(self):
        print('Vehículos Particulares:')
        for vehiculo in self.vehiculo_particular:
            print(vehiculo)
        print('Vehículos de Carga:')
        for vehiculo in self.vehiculo_carga:
            print(vehiculo)
        print('Bicicletas:')
        for bici in self.bicicletas:
            print(bici)
        print('Motocicletas:')
        for moto in self.motocicletas:
            print(moto)

gestor = Vehiculoscsv()    
# # archivo = 'practicas_python/modulo4/consolidacion/csv/archivo.csv'         
# particular = AutomovilParticular('Ford', 'Fiesta', 4, 180, 500, 5)
# carga = AutomovilCarga('Daft Trucks', 'G 38', 10, 120, 1000, 20000)
# bicicleta = Bicicleta('Shimano', 'MT Ranger', 2, 'Carrera')
# motocicleta = Motocicletas('BMW', 'F800s', 2, 'Deportiva', '2T','Doble Viga', 21)

# lista_objeto = [particular,carga,bicicleta,motocicleta]

# for lista in lista_objeto:
#     gestor.guardar_datos_csv(lista)

# # guardar_datos_csv('practicas_python/modulo4/consolidacion/csv/archivo.csv')
gestor.leer_archivo()
gestor.mostrar_datos()