import example1 as lebronjames

def main():
    edades = [3, 5, 6, 7, 8]
    lebronjames.edades = edades
    edad_obj = lebronjames.Edad(edades)
    print(edad_obj.mostrar_media())

if __name__ == "__main__":
    main()