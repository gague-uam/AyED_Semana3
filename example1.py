# leer x cantidad de edad y calcular la media

import statistics as st

class Edad:
    def __init__(self, edad):
        self.edad = edad

    def calcular_media(self):
        return sum(self.edad) / len(self.edad)
    
    def mostrar_media(self):
        media = self.calcular_media()
        return f"La edad media es: {media:.2f} años"
    
    def calc_media(self):
        return st.mean(self.edad)
    
    
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

    if (not edades):
        print("No se ingresaron edades.")
        return
    
    edad_obj = Edad(edades)
    print(edad_obj.mostrar_media())
    print(f"La media calculada con statistics es: {edad_obj.calc_media():.2f} años")

if __name__ == "__main__":
    main()
