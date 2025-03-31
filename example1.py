# leer x cantidad de edad y calcular la media

class Edad:
    def __init__(self, edad):
        self.edad = edad

    def calcular_media(self):
        return sum(self.edad) / len(self.edad)
    
    def mostrar_media(self):
        media = self.calcular_media()
        return f"La edad media es: {media:.2f} años"
    
def main():
    edades = []
    cantidad = int(input("Ingrese la cantidad de edades a procesar: "))

    while True:
        try:
            edad = int(input("Ingrese una edad (O - 1 para terminar): "))
            if edad == -1:
                break
            edades.append(edad)
        except ValueError:
            print("Por favor, ingrese un número entero válido.")
    
    edad_obj = Edad(edades)
    print(edad_obj.mostrar_media())

if __name__ == "__main__":
    main()
