
class bibloteca():
  def __init__(self, codigo,titulo,autor,year):
      self.codigo=codigo
      self.titulo=titulo
      self.autor=autor
      self.year=year
  def mostrar_info(self):
      return f"Codigo libro: {self.codigo}- Titulo: {self.titulo}- Autor: {self.autor}- Año de publicacion: {self.year}"
class gestionLibors():
    def __init__(self):
        self.libros={}
    def agregarLibros(self):
        cantidad=int(input("Ingrese la cantidad de libros que se ingresan: "))
        for i in range(cantidad):
            print(f"Libro #{i+1}")
            codigo=input("Ingrese el codigo del libro")
            if codigo in self.libros:
                print("Ese codigo ya le fue agregado a otro libro")
                return

            titulo=input("Ingrese el nombre del titulo del libro: ")
            autor=input("Ingrese el nombre del autor: ")
            year=int(input("Ingrese el año de publicacion : "))
            self.libros[codigo]=bibloteca(codigo,titulo,autor,year)
        print("Se han agregado correctamente los datos")
    def mosstrar(self):
        if not self.libros:
            print("No hay ningun libro registrado")
            return
        print("\n Lista de libros")
        for i,libr in enumerate(self.libros.values(),start=1):
            print(f"{i}. {libr.mostrar_info()}")
        print()
    def eliminar(self):
        codigo_buscado=input("Ingrese el codigo del libro a eliminar: ")
        if codigo_buscado in self.libros:
            del self.libros[codigo_buscado]
            print("Libro eliminado")
        else:
            print("El codigo de libro no encontrado.")

class usuarios():
    def __init__(self, nombre, edad):
        self.nombre=nombre
        self.edad=edad

    def mostrar_infoUsuario(self):
        return f"Nombre: {self.nombre}- Edad: {self.edad}"

class gestionUsuario():
    def __init__(self):
        self.lista_usuario=[]
    def agregarUsuario(self):
        cantidad=int(input("Ingrese la cantidad de usuarios a registrar: "))
        for i in range(cantidad):
            print(f"Usuario #{i+1}")
            nombre=input("Ingrese el nombre del usuario: ")
            edad=int(input("Ingrese la edad del usuario: "))
            self.lista_usuario.append(usuarios(nombre,edad))
            print("Usuario agregado.")
    def mostrar(self):
        if not self.lista_usuario:
            print("No hay usuarios registrados.")
            return
        else:
            print("\n Lista de Usuarios.")
            for i,usua in enumerate(self.lista_usuario,start=1):
                print(f"{i}. {usua.mostrar_infoUsuario()}")
            print()

    def eliminar(self):
        nombre_buscado=input("Ingrese al usuario que se va a eliminar: ")
        for nomb in self.lista_usuario:
            if nomb.nombre.lower()==nombre_buscado.lower():
                self.lista_usuario.remove(nomb)
                print("Usuario eliminado")
                return
        print("Usuario no encontrado")

class Prestamo():
    def __init__(self,usuario,libro,fecha_prestamo):
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
        return f"{self.libro.titulo} a {self.usuario.nombre} | Fecha préstamo: {self.fecha_prestamo.date()} | Estado: {estado}"

class gestionPrestamo():
    def __init__(self):
        self.prestamos=[]

    def prestarLibro(self,usuario,libro,fecha):
        if not libro.disponible:
            raise  ValueError("El libro no se encuentra disponible")
        libro.disponible=False
        prestamo=Prestamo(usuario,libro,fecha)
        self.prestamos.append(prestamo)

    def  devolver(self, codigo_libro,fecha):
        for prestamo in self.prestamos:
            if prestamo.libro.codigo== codigo_libro and prestamo.fecha_devolucion is None:
                prestamo.devolver(fecha)
                return
        raise ValueError("No se encontro el libro")

    def mostrar_prestamos(self):
        if not self.prestamos:
            print("No hay préstamos registrados.")
        else:
            for i, p in enumerate(self.prestamos, start=1):
                print(f"{i}. {p.mostrar_info()}")


from datetime import datetime

gestor_libros = gestionLibors()
gestor_usuarios = gestionUsuario()
gestor_prestamos = gestionPrestamo()

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
                gestor_libros.mosstrar()

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
                gestor_prestamos.prestar_libro(usuario, libro, fecha)
                print("Préstamo realizado.")

            case "7":
                codigo = input("Código del libro: ")
                fecha = datetime.strptime(input("Fecha de devolución (YYYY-MM-DD): "), "%Y-%m-%d")
                gestor_prestamos.devolver_libro(codigo, fecha)
                print("Libro devuelto.")

            case "8":
                gestor_prestamos.mostrar_prestamos()

            case "9":
                print("¡Hasta luego!")
                break

            case _:
                print("Opción inválida.")

    except Exception as e:
        print(f"Error: {e}")
