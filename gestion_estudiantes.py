# Gestión de Estudiantes 

# Diccionario para guardar los datos de los estudiantes
estudiantes = {}

# Registrar un nuevo estudiante
def registrar_estudiante():
    id_est = input("Número de identificación: ")
    if id_est in estudiantes:
        print("Estudiante ya registrado.")
        return
    nombre = input("Nombre: ")
    try:
        edad = int(input("Edad: "))
        notas = []
        for i in range(3):
            nota = float(input(f"Nota {i+1}: "))
            notas.append(nota)
        estudiantes[id_est] = {"nombre": nombre, "edad": edad, "notas": notas}
        print("Estudiante registrado correctamente.")
    except ValueError:
        print("Entrada inválida.")

# Consultar datos de un estudiante
def consultar_estudiante():
    id_est = input("ID del estudiante: ")
    if id_est in estudiantes:
        datos = estudiantes[id_est]
        promedio = sum(datos["notas"]) / len(datos["notas"])
        print("Nombre:", datos["nombre"])
        print("Edad:", datos["edad"])
        print("Notas:", datos["notas"])
        print("Promedio:", round(promedio, 2))
    else:
        print("Estudiante no encontrado.")

# Actualizar notas de un estudiante
def actualizar_notas():
    id_est = input("ID del estudiante: ")
    if id_est in estudiantes:
        try:
            nuevas_notas = []
            for i in range(3):
                nota = float(input(f"Nueva nota {i+1}: "))
                nuevas_notas.append(nota)
            estudiantes[id_est]["notas"] = nuevas_notas
            print("Notas actualizadas.")
        except ValueError:
            print("Entrada inválida.")
    else:
        print("Estudiante no encontrado.")

# Eliminar un estudiante
def eliminar_estudiante():
    id_est = input("ID del estudiante a eliminar: ")
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
        print("\nMenú")
        print("1. Registrar estudiante")
        print("2. Consultar estudiante")
        print("3. Actualizar notas")
        print("4. Eliminar estudiante")
        print("5. Ver todos los estudiantes")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_estudiante()
        elif opcion == "2":
            consultar_estudiante()
        elif opcion == "3":
            actualizar_notas()
        elif opcion == "4":
            eliminar_estudiante()
        elif opcion == "5":
            ver_todos()
        elif opcion == "6":
            print("Programa finalizado.")
            break
        else:
            print("Opción no válida.")

# Ejecutar el programa
menu()
