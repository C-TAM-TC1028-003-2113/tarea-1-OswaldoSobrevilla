def main():
    # escribe tu código abajo de esta línea
    mensajes = float(input("Dame el número de mensajes: "))
    megas = float(input("Dame el número de megas: "))
    minutos = float(input("Dame el número de minutos: "))
    costo = (mensajes * 0.80) + (megas * 0.80) + (minutos * 0.80)
    print("El costo mensual es:", costo)


if __name__ == '__main__':
    main()
