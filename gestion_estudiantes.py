# Gestión de Estudiantes 

# Diccionario para guardar los datos de los estudiantes
estudiantes = {}

def validacion(texto, tipo_de_dato = str):
    while True:
        try:
            texto_ingresado = tipo_de_dato(input(texto))
            return texto_ingresado
        except ValueError:
            print("Entrada inválida.")

# Registrar un nuevo estudiante
def registrar_estudiante():
    id_est = validacion("Número de identificación: ", int)
    id_est = str(id_est)
    if id_est in estudiantes:
        print("Estudiante ya registrado.")
        return
    nombre = validacion("Nombre: ")
    edad = validacion("Edad: ", int)

    notas = []
    # 0, 1, 2, 3
    for i in range(3):
        nota = validacion(f"Nota: {i+1}", float)
        notas.append(nota)
    estudiantes[id_est] = {"nombre": nombre, "edad": edad, "notas": notas}
    print("Estudiante registrado correctamente.")


# Consultar datos de un estudiante
def consultar_estudiante():
    id_est = str(validacion("ID del estudiante: ", int))
    if id_est in estudiantes:
        datos = estudiantes[id_est]
        promedio = sum(datos["notas"]) / len(datos["notas"])
        print("Nombre:", datos["nombre"])
        print("Edad:", datos["edad"])
        print("Notas:", datos["notas"])
        print("Promedio:", round(promedio, 1))
    else:
        print("Estudiante no encontrado.")

# Actualizar notas de un estudiante
def actualizar_notas():
    id_est = str(validacion("ID del estudiante: ", int))
    if id_est in estudiantes:
        nuevas_notas = []
        for i in range(3):
            nota = validacion(f"Nueva nota {i+1}: ", float)
            nuevas_notas.append(nota)
        estudiantes[id_est]["notas"] = nuevas_notas
        print("Notas actualizadas.")
    else:
        print("Estudiante no encontrado.")

# Eliminar un estudiante
def eliminar_estudiante():
    id_est = validacion("ID del estudiante a eliminar: ", int)
    if id_est in estudiantes:
        del estudiantes[id_est]
        print("Estudiante eliminado.")
    else:
        print("Estudiante no encontrado.")

# Ver todos los estudiantes registrados
def ver_todos():
    if not estudiantes:
        print("No hay estudiantes registrados.")
        return
    for id_est, datos in estudiantes.items():
        promedio = sum(datos["notas"]) / len(datos["notas"])
        print(f"ID: {id_est} | Nombre: {datos['nombre']} | Promedio: {round(promedio, 2)}")

# Menú principal
def menu():
    while True:
        print("\nMenú\n"
            "1. Registrar estudiante \n"\
            "2. Consultar estudiante \n"\
            "3. Actualizar notas\n"\
            "4. Eliminar estudiante \n"\
            "5. Ver todos los estudiantes\n"\
            "6. Salir")
        opcion = validacion("Seleccione una opciòn", int)

        if opcion == 1:
            registrar_estudiante()
        elif opcion == 2:
            consultar_estudiante()
        elif opcion == 3:
            actualizar_notas()
        elif opcion == 4:
            eliminar_estudiante()
        elif opcion == 5:
            ver_todos()
        elif opcion == 6:
            print("Programa finalizado.")
            break
        else:
            print("Opción no válida.")

# Ejecutar el programa
menu()
