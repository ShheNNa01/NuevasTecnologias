
#5)	Elabore un programa para determinar el funcionamiento optimo de las 407 cabinas de metro cable, registrando un puntaje que se clasifica de la siguiente forma si tiene 2 puntos está con un funcionamiento defectuoso, si tiene 3 puntos el funcionamiento es moderado y si tiene 4 puntos el funcionamiento es óptimo.

import random

# Función para clasificar el funcionamiento de la cabina según el puntaje
def clasificar_funcionamiento(puntaje):
    if puntaje == 2:
        return "Funcionamiento defectuoso"
    elif puntaje == 3:
        return "Funcionamiento moderado"
    elif puntaje == 4:
        return "Funcionamiento óptimo"
    else:
        return "Puntaje inválido"  # Esto solamente para puntajes validos dentro del rango determinado

# Lista para almacenar los datos de las cabinas
listado_cabinas = []

# Clasifiquemos segun puntaje las cabinas.
for cabina_id in range(1, 408):
    puntaje = random.choice([2, 3, 4])  # Puntaje aleatorio de entre 2, 3 y 4
    funcionamiento = clasificar_funcionamiento(puntaje)
    
    # Agregar daros
    listado_cabinas.append((cabina_id, puntaje, funcionamiento))

# Mostrar el resultado en pantalla
print(f"{'Cabina ID':<10} {'Puntaje':<7} {'Funcionamiento':<25}")
print("=" * 42)
for cabina in listado_cabinas:
    cabina_id, puntaje, funcionamiento = cabina
    print(f"{cabina_id:<10} {puntaje:<7} {funcionamiento:<25}")
