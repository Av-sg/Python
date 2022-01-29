print("*********************************************")
print("Tablas de Multiplicar")
print("*********************************************")
numero = int(input("Digite la tabla a multiplicar: "))
limite = 10
contador = 1 
while contador <= limite:
    resultado = contador * numero
    print("{} x {} = {}" .format(numero, contador, resultado))
    contador = contador + 1
