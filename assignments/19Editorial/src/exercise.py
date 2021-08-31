def main():
    # escribe tu código abajo de esta línea
    palabras = float(input("Dame el número de palabras: "))
    b = (palabras//475)*60
    c = palabras%475
    if 1<=c:
        d=60
    x = (b+d)
    total = (x-(x*10/100))
    print("El costo de la publicación es:", total)

if __name__ == '__main__':
    main()
