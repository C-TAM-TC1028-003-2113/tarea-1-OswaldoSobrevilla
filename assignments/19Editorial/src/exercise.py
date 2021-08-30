def main():
    # escribe tu código abajo de esta línea
    palabras = int(input("Dame el número de palabras: "))
    paginas = 1
    if palabras < 475:
        paginas = 1
        costo = (paginas*60)*0.9
        print("El costo de la publicación es:", costo)
    else:
             palabras > 475
             paginas = 2
             costo = (paginas*60)*0.9
             print("El costo de la publicación es:", costo)


if __name__ == '__main__':
    main()
