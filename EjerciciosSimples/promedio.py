nota1 = float(input("Ingrese nota 1: ")) # tambien se puede ocupar con int 
if nota1 > 0 and nota1<=7:
    nota2 = float(input("Ingrese nota 2: "))
    if nota2 > 0 and nota2 <=7:
        nota3 = float(input("Ingrese nota 3: "))
        if nota3 >0 and nota3 <=7:
            promedio = (nota1+nota2+nota3) /3

            print("Su promedio es: ",promedio)

            if promedio >= 4.0:
                print("Aprobado")
            else:
                print("Reprobado")
        else:
            print("Nota 3 no es válida")
    else:
        print("Nota 2 no es válida")
else:
    print("Nota 1 no es válida")







