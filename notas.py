notaDesarrolloSoftware = int(input("Ingrese su nota de desarrollo"))
notamatematicas = int(input("Ingrese su nota de mate..."))
notalogicaProgramacion = int(input("Ingrese su nota de logica"))
promedio = (notamatematicas + notaDesarrolloSoftware + notalogicaProgramacion) / 3 


if promedio >= 3:
    print("Feicidades, aprobaste el curso")
else:
    print("Lo siento, debes esforzarte un poco más")