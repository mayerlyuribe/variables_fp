print(""" 
0. Kilómetro a metro
1. Centímetro a metro
2. Kilómetro por hora a millas por hora
3. Nota en Educatic a nota en Canvas
4. Nota en Educatic a nota en Canvas
5. Mililitro a centímetro cúbico
6. Dólar (USA) a peso colombiano
7. Peso colombiano a dólar (USA)
8. Libra a kilogramo
9. Minuto luz a kilómetro
""")

lista  = [1000, 0.01, 0.62, 20, 0.05, 1, 3847.10, 0.00026, 0.45, 17987539.67 ]

operación = input("ingrese el número correspondiente a la operación que desea realizar: ")
operación = int(operación)

if operación >=0 and operación <=9:
    valor = input("ingrese el valor que desea covertir: ")
    valor = float(valor)
    resultado = valor * lista[operación]
    print("el resultado es: ", resultado)
else:
    print("operación inálida :(")