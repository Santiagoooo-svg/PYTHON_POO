from cosas import *

def main():
    l1 = Libro.libro_planeta("El perfume", Autor("Parik", "PS"), 1980)
    print(l1)
    l1.autor.pseudonimo = l1.autor.pseudonimo.lower()
    print(l1)
    print("-----Herencia-----")
    al2 = Alumno("Jose", 18, "3322232", "ICO", 9)
    al2.nombre = "Pepe"
    print(vars(al2))
main()