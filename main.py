
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

