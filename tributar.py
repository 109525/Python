edad = int(input("Ingrese su edad"))
ingresos = int(input("Registre sus ingresos aquí"))

if edad >= 18 and ingresos >= 2500000: 
    print("Usted debe tributar")
else: print("Usted no debe tributar aún")