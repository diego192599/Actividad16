from datetime import datetime

class Biblioteca:
    def __init__(self, codigo, titulo, autor, year):
        self.codigo = codigo
        self.titulo = titulo
        self.autor = autor
        self.year = year
        self.disponible = True  # atributo para saber si está disponible

    def mostrar_info(self):
        return f"Código: {self.codigo} - Título: {self.titulo} - Autor: {self.autor} - Año: {self.year} - Disponible: {'Sí' if self.disponible else 'No'}"


class GestionLibros:
    def __init__(self):
        self.libros = {}

    def agregarLibros(self):
        cantidad = int(input("Ingrese la cantidad de libros que se ingresan: "))
        for i in range(cantidad):
            print(f"\nLibro #{i+1}")
            codigo = input("Ingrese el código del libro: ")
            if codigo in self.libros:
                print("Ese código ya fue registrado.")
                continue
            titulo = input("Ingrese el título del libro: ")
            autor = input("Ingrese el autor del libro: ")
            year = int(input("Ingrese el año de publicación: "))
            self.libros[codigo] = Biblioteca(codigo, titulo, autor, year)
        print("Se han agregado correctamente los datos.")

    def mostrar(self):
        if not self.libros:
            print("No hay libros registrados.")
            return
        print("\nLista de libros:")
        for i, libro in enumerate(self.libros.values(), start=1):
            print(f"{i}. {libro.mostrar_info()}")

    def eliminar(self):
        codigo = input("Ingrese el código del libro a eliminar: ")
        if codigo in self.libros:
            del self.libros[codigo]
            print("Libro eliminado.")
        else:
            print("El código no fue encontrado.")


class Usuario:
    def __init__(self, carnet, nombre, edad):
        self.carnet = carnet
        self.nombre = nombre
        self.edad = edad

    def mostrar_info(self):
        return f"Carnet: {self.carnet} - Nombre: {self.nombre} - Edad: {self.edad}"


class GestionUsuarios:
    def __init__(self):
        self.lista_usuario = []

    def agregarUsuario(self):
        cantidad = int(input("Ingrese la cantidad de usuarios a registrar: "))
        for i in range(cantidad):
            print(f"\nUsuario #{i+1}")
            carnet = input("Ingrese el carnet del usuario: ")
            nombre = input("Ingrese el nombre del usuario: ")
            edad = int(input("Ingrese la edad del usuario: "))
            self.lista_usuario.append(Usuario(carnet, nombre, edad))
            print("Usuario agregado correctamente.")

    def mostrar(self):
        if not self.lista_usuario:
            print("No hay usuarios registrados.")
            return
        print("\nLista de usuarios:")
        for i, usuario in enumerate(self.lista_usuario, start=1):
            print(f"{i}. {usuario.mostrar_info()}")

    def eliminar(self):
        carnet = input("Ingrese el carnet del usuario a eliminar: ")
        for usuario in self.lista_usuario:
            if usuario.carnet == carnet:
                self.lista_usuario.remove(usuario)
                print("Usuario eliminado.")
                return
        print("Usuario no encontrado.")


class Prestamo:
    def __init__(self, usuario, libro, fecha_prestamo):
        self.usuario = usuario
        self.libro = libro
        self.fecha_prestamo = fecha_prestamo
        self.fecha_devolucion = None

    def devolver(self, fecha_devolucion):
        if fecha_devolucion < self.fecha_prestamo:
            raise ValueError("La fecha de devolución no puede ser anterior a la fecha de préstamo.")
        self.fecha_devolucion = fecha_devolucion
        self.libro.disponible = True

    def mostrar_info(self):
        estado = "Devuelto" if self.fecha_devolucion else "Prestado"
        return f"{self.libro.titulo} a {self.usuario.nombre} | Préstamo: {self.fecha_prestamo.date()} | Estado: {estado}"


class GestionPrestamos:
    def __init__(self):
        self.prestamos = []

    def prestarLibro(self, usuario, libro, fecha):
        if not libro.disponible:
            raise ValueError("El libro no se encuentra disponible.")
        libro.disponible = False
        self.prestamos.append(Prestamo(usuario, libro, fecha))

    def devolver(self, codigo_libro, fecha):
        for prestamo in self.prestamos:
            if prestamo.libro.codigo == codigo_libro and prestamo.fecha_devolucion is None:
                prestamo.devolver(fecha)
                return
        raise ValueError("No se encontró el préstamo del libro especificado.")

    def mostrar_prestamos(self):
        if not self.prestamos:
            print("No hay préstamos registrados.")
            return
        for i, prestamo in enumerate(self.prestamos, start=1):
            print(f"{i}. {prestamo.mostrar_info()}")

gestor_libros = GestionLibros()
gestor_usuarios = GestionUsuarios()
gestor_prestamos = GestionPrestamos()

while True:
    print("\n--- Menú Biblioteca ---")
    print("1. Agregar libros")
    print("2. Mostrar libros")
    print("3. Eliminar libro")
    print("4. Agregar usuarios")
    print("5. Mostrar usuarios")
    print("6. Prestar libro")
    print("7. Devolver libro")
    print("8. Mostrar préstamos")
    print("9. Salir")

    opcion = input("Seleccione una opción: ")

    try:
        match opcion:
            case "1":
                gestor_libros.agregarLibros()

            case "2":
                gestor_libros.mostrar()

            case "3":
                gestor_libros.eliminar()

            case "4":
                gestor_usuarios.agregarUsuario()

            case "5":
                gestor_usuarios.mostrar()

            case "6":
                carnet = input("Carnet del usuario: ")
                codigo = input("Código del libro: ")
                fecha = datetime.strptime(input("Fecha de préstamo (YYYY-MM-DD): "), "%Y-%m-%d")
                usuario = next((u for u in gestor_usuarios.lista_usuario if u.carnet == carnet), None)
                libro = gestor_libros.libros.get(codigo)
                if not usuario or not libro:
                    raise ValueError("Usuario o libro no encontrado.")
                gestor_prestamos.prestarLibro(usuario, libro, fecha)
                print("Préstamo realizado correctamente.")

            case "7":
                codigo = input("Código del libro: ")
                fecha = datetime.strptime(input("Fecha de devolución (YYYY-MM-DD): "), "%Y-%m-%d")
                gestor_prestamos.devolver(codigo, fecha)
                print("Libro devuelto correctamente.")

            case "8":
                gestor_prestamos.mostrar_prestamos()

            case "9":
                print("¡Hasta luego!")
                break

            case _:
                print("Opción inválida.")

    except Exception as e:
        print(f"Error: {e}")
