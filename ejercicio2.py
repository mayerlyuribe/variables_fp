import math

print ("vamos a calcular la distancia entre dos puntos en un plano.")

x1 = int(input("ingrese la coordenada x del primer punto: "))
y1 = int(input("ingrese la coordenada y del primer punto: "))
print("------------------------------------------------")
x2 = int(input("ingrese la coordenada x del segundo punto: "))
y2 = int(input("ingrese la coordenada y del segundo punto: "))

distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print("la distancia entre los dos puntos es: ", distancia)