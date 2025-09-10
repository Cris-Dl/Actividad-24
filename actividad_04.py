def factorial(n):
    if n==1 or n==0:
        return 1
    else:
        return n*factorial(n-1)

def suman(n):
    if n==0:
        return n
    else:
        return n+suman(n-1)

def potencia(n,m):
    if m == 0:
        return 1
    elif m > 0:
        return n * potencia(n, m-1)
def fibonacci(n):
    if n <=1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def contar_letra(palabra, letra):
    palabra = palabra.lower()
    letra = letra.lower()
    if not palabra:
        return 0
    elif palabra[0] == letra:
        return 1 + contar_letra(palabra[1:], letra)
    else:
        return contar_letra(palabra[1:], letra)

def invertir_cadena(cadena):
    if len(cadena) == 0:
        return ""
    else:
        return invertir_cadena(cadena[1:]) + cadena[0]

while True:
    print("---- Menú ----")
    print("1. Factorial de un número")
    print("2. Suma de los primero N números naturales")
    print("3. Calcular el n-ésimo número de Fibonacci")
    print("4. Contar cuantas veces aparece una letra en una palabra")
    print("5. Invertir una cadena de texto")
    print("6. Calcular potencia")
    print("7. Salir")
    menu_option = input("Ingrese el número de la opción que quiera realizar: ")
    print()
    match menu_option:
        case "1":
            print("Factorial de un número")
            numero = int(input("Ingrese el número a operar: "))
            if numero < 0:
                print("No se admiten números menores a 0")
            else:
                print(f"El factorial del número {numero} es de: {factorial(numero)}")
            print()
        case "2":
            print("Suma de los primeros N números naturales")
            numero = int(input("Ingrese el número que se quiera ir sumando: "))
            if numero < 0:
                print("No se admiten número menor a 0")
            else:
                print(f"La suma del número {numero} es de: {suman(numero)}")
            print()
        case "3":
            print("Calcular el n-ésimo número de Fibonacci")
            numero = int(input("Ingrese el número que quiera calcular: "))
            if numero < 0:
                print("No se admiten número negativos")
            else:
                print(f"El termino n del número {numero} es: {fibonacci(numero)}")
            print()
        case "4":
            print("Contar cuantas veces aparece una letra en una palabra")
            palabra = input("Ingrese la palabra a revisar: ")
            letra = input("Ingrese la letra que quiera contar dentro de la palabra: ")
            if not palabra or not letra:
                print("El campo no puedee estar vacio")
            else:
                print(f"La letra {letra} se contó la cantidad de: {contar_letra(palabra, letra)}")
            print()
        case "5":
            print("Invertir una cadena de texto")
            cadena = input("Ingrese la cadena dee texto a revertir el orden: ")
            if not cadena:
                print("El campo no puede estar vacio")
            else:
                print(f"La cadena de texto inveertida es la siguiente: {invertir_cadena(cadena)}")
            print()
        case "6":
            print("Calcular potencia")
            base = int(input("Ingrese el número de la basse: "))
            exponente = int(input("Ingrese el número del exponente: "))
            if base < 0 or exponente < 0:
                print("No se admiten valores negativos")
            else:
                print(f"El resultado de {base} elevado a {exponente} es de: {potencia(base, exponente)}")
            print()
        case "7":
            print("Saliendo del programa, gracias por su preferencia")
            break
        case _:
            print("Valor invalido")