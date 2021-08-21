#nombre = input("Introduce tu nombre: ")
#print(f"Hola {nombre}")

#entero
edad=20

#flotante - decimales
estatura=1.75


#convertir flotante 
edads=str(edad)

print(edad+edad)
print(edads+edads)

print(type(edad))

tuedad= input("introduce tu edad: ")
tuedad=int(tuedad)

if tuedad >= 18 and tuedad < 100:
    print("eres mayor de edad")
elif tuedad >= 100:
    print("¿Eres inmortal?")
elif tuedad <= 0:
    print("No exites")
else:
    print("eres menor de edad")

    for i in range(0,10):
        print(i)