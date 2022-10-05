# Ejercicio 3 (18 puntos): Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que el usuario escriba “salir” que terminará.

def main():
    cadena = input("Ingrese una cadena de texto: ")
    echo = cadena.split("salir")[0]

    print(echo)
    
    return echo

if __name__ == '__main__':
    main()
    
'''
¯\_( ͡° ͜ʖ ͡°)_/¯ Matias Moreno Barrios
'''