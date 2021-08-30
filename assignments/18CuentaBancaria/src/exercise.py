def main():
    # escribe tu código abajo de esta línea
    saldoanterior = float(input("Dame el saldo del mes anterior: "))
    ingresos = float(input("Dame los ingresos: "))
    egresos = float(input("Dame los egresos: "))
    numerocheques = int(input("Dame el número de cheques: "))
    saldofinal = (saldoanterior+ingresos-egresos-numerocheques*13)*(0.925)
    print("El saldo final de la cuenta es:", saldofinal)


if __name__ == '__main__':
    main()
