dolarAustraliano = 0.0019
pesoArgentino = 0.27
yen = 0.17

print("Ingrese pesos chilenos: ")
pesoChileno = int(input())

print("En que moneda deseas?")
print("1. Dolar Australiano")
print("2. Peso Argentino")
print("3. Yen")
opcion = int(input())

if opcion == 1 :
    conver = pesoChileno*dolarAustraliano
    print("Los $",pesoChileno," son $AUD",conver,"dolar Australiano")
else:
    if opcion == 2 :
        conver = pesoChileno*pesoArgentino
        print("Los $",pesoChileno," son $ARG",conver,"peso Argentino")
    else:
        if opcion == 3:
            conver = pesoChileno*yen
            print("Los $",pesoChileno," son ¥",conver,"Yen")
