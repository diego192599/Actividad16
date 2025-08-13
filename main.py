
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


