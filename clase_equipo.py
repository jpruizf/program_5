class Equipo:
    __id:int
    __nombre:str
    __goles_favor:int
    __goles_contra:int
    __diferencia_goles:int
    __puntos:int

    def __init__(self,ids,nombre,goles_favor,goles_contra,diferencia_goles,puntos):
        self.__id = ids
        self.__nombre = nombre
        self.__goles_favor = goles_favor
        self.__goles_contra = goles_contra
        self.__diferencia_goles = diferencia_goles
        self.__puntos = puntos
    
    def get_id(self):
        return self.__id
    
    def get_nombre(self):
        return self.__nombre
    
    def get_goles_favor(self):
        return self.__goles_favor
    
    def get_goles_contra(self):
        return self.__goles_contra
    
    def get_diferencia_goles(self):
        return self.__diferencia_goles
    
    def get_puntos(self):
        return self.__puntos
    
    def __str__(self):
        return f"Identificador:{self.get_id()}/Nombre del equipo:{self.get_nombre()}/Goles a favor:{self.get_goles_favor()}/Goles en contra:{self.get_goles_contra()}/Diferencia de goles:{self.get_diferencia_goles()}/Total de puntos:{self.get_puntos()}"