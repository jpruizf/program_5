class Fecha:
    __fecha_partido:str
    __id_equipo_local:int
    __id_equipo_visitante:int
    __cantidad_goles_local:int
    __cantidad_goles_visitante:int

    def __init__(self,fecha_partido,id_equipo_local,id_equipo_visitante,cantidad_goles_local,cantidad_goles_visitante):
        self.__fecha_partido = fecha_partido
        self.__id_equipo_local = id_equipo_local
        self.__id_equipo_visitante = id_equipo_visitante
        self.__cantidad_goles_local = cantidad_goles_local
        self.__cantidad_goles_visitante = cantidad_goles_visitante
    
    def get_fecha_partido(self):
        return self.__fecha_partido
    
    def get_id_equipo_local(self):
        return self.__id_equipo_local
    
    def get_id_equipo_visitante(self):
        return self.__id_equipo_visitante
    
    def get_cantidad_goles_local(self):
        return self.__cantidad_goles_local
    
    def get_cantidad_goles_visitante(self):
        return self.__cantidad_goles_visitante
    
    def __str__(self):
        return f"Fecha del partido:{self.get_fecha_partido()}/Identificador del equipo local:{self.get_id_equipo_local()}/Identificador del equipo visitante:{self.get_cantidad_goles_visitante()}/Cantidad de goles del equipo local:{self.get_cantidad_goles_local()}/Cantidad del equipo visitante:{self.get_cantidad_goles_visitante()}"