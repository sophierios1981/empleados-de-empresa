from itertools import groupby

def ordenar_empleados(empleados):
    empleados_ordenados= sorted(empleados,key=lambda emp: (emp['rendimiento'], -emp['edad']), reverse=True )
    return empleados_ordenados

def agrupar_empleados_por_pais(empleados_ordenados):
    empleados_agrupados = {pais: list(grupo_empleados) for pais, grupo_empleados in groupby(empleados_ordenados,key=lambda emp:emp['pais'])}
    return empleados_agrupados

def mostrar_empleados_agrupados(empleados_agrupados):
    for pais, grupo_empleados in empleados_agrupados.items():
        print(f'\nPais: {pais}')
        for empleado in grupo_empleados:
          print(empleado)
          
          
empleados = [
    {'nombre': 'Juan', 'edad': 30, 'rendimiento': 8.5, 'pais': 'España'},
    {'nombre': 'María', 'edad': 25, 'rendimiento': 9.0, 'pais': 'México'},
    {'nombre': 'Pedro', 'edad': 35, 'rendimiento': 7.5, 'pais': 'España'},
    {'nombre': 'Ana', 'edad': 28, 'rendimiento': 9.2, 'pais': 'Colombia'}
]

empleados_ordenados = ordenar_empleados(empleados)
empleados_agrupados = agrupar_empleados_por_pais(empleados_ordenados)
mostrar_empleados_agrupados(empleados_agrupados)