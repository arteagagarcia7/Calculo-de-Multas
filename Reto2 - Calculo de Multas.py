print("Por favor digite los siguientes valores sin puntos o comas y seguidos con un espacio el uno del otro: ")
print("la Distancia Recorrida, la velocidad en la que recorrió dicho tramo y el tiempo que tardo.")

Distancia, Velocidadpermitida, Tiempo = input().split()
Distancia = float(Distancia)
Velocidadpermitida = float(Velocidadpermitida)
Tiempo = float(Tiempo)

Velocidadaproximada = (Distancia / 1000) / (Tiempo / 3600)
Velocidadporcentaje = (((Velocidadaproximada - Velocidadpermitida)*100)/Velocidadpermitida)

if(Distancia < 0 or Velocidadpermitida < 0 or Tiempo <0):
    print ("Error, los valores ingresados son incorrectos")
elif (Velocidadaproximada < Velocidadpermitida):
    print ("OK, no tiene multas")
elif(Velocidadporcentaje < (0.2 * Velocidadpermitida)):
    print ("Usted supero el limite de la velocidad permitida en más de un 20%, tiene una multa.")
elif(Velocidadporcentaje >= (0.2 * Velocidadpermitida)):
    print ("Usted supero el limite de la velocidad permitida en menos de un 20%, debe realizar un Curso de Sensibilización9165")