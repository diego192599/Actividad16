class bibloteca():
    def __init__(self,titulo,autor,year,codigo):
        self.titulo=titulo
        self.autor=autor
        self.year=year
        self.codigo=codigo

    def mostrar_info(self):
        return f"Titulo del libro: {self.titulo}- Autor del libro: {self.autor}- Año de publicacion: {self.year}- Codigo del libro: {self.codigo}"
class gestionLibors():
    def __init__(self):
        self.listaLibros=[]

    def agregarLibro(self):
        try:
            cantidad=int(input("Ingrese la cantidad de libros que seran registrados: "))
            for i in range(cantidad):
                print(f"Libro #{i+1}")
                titulo=input("Ingrese el titulo del libro: ")
                autor=input("Ingrese el nombre del autor del dicho libro: ")
                year=int(input("Ingrese el año de publicacion del libro: "))
                codigo=input("Ingrese el codigo del libro: ")



