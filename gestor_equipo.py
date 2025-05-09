from clase_equipo import Equipo
from tabulate import tabulate
import csv
class Gestor_equipo:
    equipos:list

    def __init__(self):
        self.equipos = []

    def leer_archivo(self, archivo):
        with open(archivo,"r",encoding="utf-8") as file:
            lector = csv.reader(file,delimiter=",")
            lista_equipos = []
            for i in lector:
                id_equipo = i[0]
                nombre = i[1]
                goles_favor = i[2]
                goles_contra = i[3]
                dif_goles = i[4]
                puntos = i[5]
                datos_equipos = Equipo(id_equipo,nombre,goles_favor,goles_contra,dif_goles,puntos)
                lista_equipos.append(datos_equipos)
            self.equipos = lista_equipos
        return self.equipos
    
    def mostrar_tabla_equipos(self,aux_nom):
        campos = ["Identificador del equipo","Nombre","Goles a favor","Goles en contra","Diferencia de goles","Puntos"]
        print("|".join(campos))
        print("-"*(len("|".join(campos))+ len(campos)-1))
        for equipo in self.equipos:
            print("|".join(map(str, equipo)))
    
    def actualizar_tabla_equipos(self,id_equipo,nombre,goles_favor,goles_contra,dif_goles,puntos):
        equipo_actualizado = False
        for i in self.equipos:
            if len(i) >= 6 and i[0] == id_equipo:
                i[1] = nombre
                i[2] = goles_favor
                i[3] = goles_contra
                i[4] = dif_goles
                i[5] = puntos
                equipo_actualizado = True
                break
        if not equipo_actualizado:
            nuevo_datos_tabla = [id_equipo,nombre,goles_favor,goles_contra,dif_goles,puntos]
            self.equipos.append(nuevo_datos_tabla)
        return self.equipos
    
    def ordenar_diferencia_goles(self):
        self.equipos.sort(key=lambda x: x._Equipo__diferencia_goles)
        return self.equipos

    def mostrar_tabla(self):
        campos = ["Identificador del equipo","Nombre","Goles a favor","Goles en contra","Diferencia de goles","Puntos"]
        print(tabulate(self.equipos, headers=campos, tablefmt="grid"))