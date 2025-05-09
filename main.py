from gestor_equipo import Gestor_equipo
from gestor_fechas import Gestor_fechas

def test():
    gestor_e = Gestor_equipo()
    gestor_f = Gestor_fechas()

    print("1.Registrar datos de todos los equipos")
    print("2.Registrar datos de las fechas de todos los partidos")
    print("3.Ver listado de equipos ingresando el nombre del un equipo")
    print("4.Actualizar la tabla de equipos con los resultados de las fechas disputadas")
    print("5.Ordenar tabla de posiciones")
    print("0.Finalizar")
    opcion = input("Selecciones una de las opciones dadas:")
    while opcion != '0':
        if opcion == '1':
            if gestor_e.leer_archivo('equipos2024.csv'):
                print("Lectura exitosa!")
                gestor_e.mostrar_tabla()
        elif opcion == '2':
            if gestor_f.leer_archivo('fechasFutbol.csv'):
                print("Lectura exitosa!")
        elif opcion == '3':
            nom_aux = input("Nombre de un equipo-->")
            gestor_e.mostrar_tabla_equipos(nom_aux)
        elif opcion == '4':
            id_equipo = input("Identificador del equipo-->")
            nombre = input("Nombre del equipo-->")
            goles_favor = input("Goles a favor-->")
            goles_contra = input("Goles en contra-->")
            dif_goles = input("Diferencia de goles-->")
            puntos = input("Puntos-->")
            gestor_e.actualizar_tabla_equipos(id_equipo,nombre,goles_favor,goles_contra,dif_goles,puntos)
            gestor_e.mostrar_tabla()
        elif opcion == '5':
            gestor_e.ordenar_diferencia_goles()
            gestor_e.mostrar_tabla()
        print("1.Registrar datos de todos los equipos")
        print("2.Registrar datos de las fechas de todos los partidos")
        print("3.Ver listado de equipos ingresando el nombre del un equipo")
        print("4.Actualizar la tabla de equipos con los resultados de las fechas disputadas")
        print("5.Ordenar tabla de posiciones")
        print("0.Finalizar")
        opcion = input("Selecciones una de las opciones dadas:")

if __name__ == '__main__':
    test()