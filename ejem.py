class Libro:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn

    def mostrar_informacion(self):
        return f"Titulo: {self.titulo}, Autor: {self.autor}, ISBN: {self.isbn}"

class Biblioteca:
    def __init__(self):
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def mostrar_libros(self):
        for libro in self.libros:
            print(libro.mostrar_informacion())

# Creando algunos libros
libro1 = Libro("Cien Años de Soledad", "Gabriel García Márquez", "123456789")
libro2 = Libro("El Principito", "Antoine de Saint-Exupéry", "987654321")

# Creando una biblioteca y agregando libros a ella
biblioteca = Biblioteca()
biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)

# Mostrando los libros en la biblioteca
# biblioteca.mostrar_libros()