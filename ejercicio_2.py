# Ejercicio 2 (18 puntos): Los tramos impositivos para la declaración de la renta en un determinado país son los siguientes: (IMAGEN ADJUNTA). 

def main():
    renta_anual = int(input("Ingrese su renta anual: €"))

    if (renta_anual < 10000):
        impuesto = (renta_anual * 5) / 100
    elif (renta_anual > 10000 and renta_anual < 20000):
        impuesto = (renta_anual * 15) / 100
    elif (renta_anual > 20000 and renta_anual < 35000):
        impuesto = (renta_anual * 20) / 100
    elif (renta_anual > 35000 and renta_anual < 60000):
        impuesto = (renta_anual * 30) / 100
    else:
        impuesto = (renta_anual * 45) / 100

    print(f"El monto que le toca pagar es de €{impuesto}")


if __name__ == '__main__':
    main()
    
'''
¯\_( ͡° ͜ʖ ͡°)_/¯ Matias Moreno Barrios
'''