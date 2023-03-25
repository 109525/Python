#condicional if 
#Ingresar la edad del usuario, muestre si e smayor de edad.
# nombre = input("ingrese su nombre: ")
# edad = int(input("ingrese su edad: "))
# if edad >= 18:
#     print(nombre, "Eres mayor de edad")
# else:
#     print(nombre, "Eres menor de edad")
    
    
# #elif 
# num1 = int(input("ingrese numero:"))
# num2 = int(input("ingrese numero"))
# if num1>num2:
#     print(num1, "es mayor")
# elif num1<num2:
#     print(num2, "es mayor")
# else:
#     print(f"{num1} y {num2} son iguales")
    
    #CONDICIONAL Y OPERADORES LOGICOS: AND, OR
    #pedir al usuario la edad y a que grupo quiere pertenecer  [adultos/infantes]. si el usuario tiene 18 años o mas y escige adultos muestra "puede ingresar al grupo",de lo contrario "Excede la edad para pertenecer al grupo". si tiene menos de 18 años y escoge infantes, muestre "puede ingresar al grupo de infantes", de lo contrario "no puede ingresar". Si escoge una opcion diferente, debe salir  OPCION NO VALIDA

edad = int(input("ingrese su edad"))
grupo = int(input("ingrese el grupo al que quiere pertenecer: \n 1.Adultos \n 2.infantes"))
    
if edad >= 18 and grupo == 1:
    print("puede ingresar al grupo")
elif edad >= 18 and grupo == 2: 
    print("No puede ingresar al grupo") 
    
elif edad <18 and grupo == 2: 
    print("Puede ingresar al grupo")
        
        