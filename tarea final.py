Nombre: Brayan Stiben Montañez Fonseca
# Grupo: 213022_442
# Programa: FUNDAMENTOS DE PROGRAMACIÓN
# Código Fuente: autoría propia

# Matriz con datos de sesiones
# Formato: [ID Cliente, Duración (segundos), Eventos Clics]

sesiones = [
    [101, 250, 12],
    [102, 45, 2],
    [103, 120, 5],
    [104, 300, 15],
    [105, 80, 1]
]


# Función para clasificar el nivel de compromiso
def clasificar_compromiso(duracion, clics):
    if duracion > 180 and clics > 8:
        return "Alto"

    elif duracion < 60 or clics < 3:
        return "Bajo"

    else:
        return "Medio"


# Generar informe
print("=== INFORME DE COMPROMISO DE SESIONES ===\n")

for sesion in sesiones:
    id_cliente = sesion[0]
    duracion = sesion[1]
    clics = sesion[2]

    clasificacion = clasificar_compromiso(duracion, clics)

    print(f"Cliente ID: {id_cliente} -> Compromiso: {clasificacion}")

