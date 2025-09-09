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
                print(f"El factorial del número {numero} es de:{factorial(numero)}")
            print()
        case "2":
            print("Suma de los primeros N números naturales")
            numero = int(input("Ingrese el número que se quiera ir sumando: "))
            if numero < 0:
                print("No se admiten número menor a 0")
            else:
                print(f"La suma del número {numero} es de:{suman(numero)}")
            print()
        case "3":
            print("Calcular el n-ésimo número de Fibonacci")
        case "4":
            print("Contar cuantas veces aparece una letra en una palabra")
        case "5":
            print("Invertir una cadena de texto")
        case "6":
            print("Calcular potencia")
            base = int(input("Ingrese el número de la basse: "))
            exponente = int(input("Ingrese el número del exponente: "))
            if base < 0 or exponente < 0:
                print("No se admiten valores negativos")
            else:
                print(f"{potencia(base, exponente)}")
        case "7":
            print("Saliendo del programa, gracias por su preferencia")
            break
        case _:
            print("Valor invalido")