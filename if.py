#condicional if 
#Ingresar la edad del usuario, muestre si e smayor de edad.
nombre = input("ingrese su nombre: ")
edad = int(input("ingrese su edad: "))
if edad >= 18:
    print(nombre, "Eres mayor de edad")
else:
    print(nombre, "Eres menor de edad")
    
    
#elif 
num1 = int(input("ingrese numero:"))
num2 = int(input("ingrese numero"))
if num1>num2:
    print(num1, "es mayor")
elif num1<num2:
    print(num2, "es mayor")
else:
    print(f"{num1} y {num2} son iguales")

    