from clase_fecha import Fecha
import csv

class Gestor_fechas:
    fechas:list

    def __init__(self):
        self.fechas = []
    def leer_archivo(self, archivo):
        with open(archivo,"r",encoding="utf-8") as file:
            lector = csv.reader(file,delimiter=",")
            for i in lector:
                fecha_partido = i[0]
                id_equipo_local = i[1]
                id_equipo_visitante = i[2]
                cantidad_goles_local = i[3]
                cantidad_goles_visitante = i[4]
                datos_fecha = Fecha(fecha_partido,id_equipo_local,id_equipo_visitante,cantidad_goles_local,cantidad_goles_visitante)
                self.fechas.append(datos_fecha)
                return self.fechas
    
    def get_listado_fechas(self):
        for i in self.fechas:
            print(i)