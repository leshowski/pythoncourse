try:
    archivo = open("lpc.txt")
    print(archivo.read())
    archivo.close()
except Exception as e:
    print("El error es: %s" %e)