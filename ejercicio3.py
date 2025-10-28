text1 = "Mezclar con amor infinito tres kilos de papas criollas bien peladas, dos cebollas cabezonas picadas finamente y un manojo generoso de cilantro fresco"
text2 = "Hoy conquistaremos el mundo entero con valentía inquebrantable, pero primero necesitamos conseguir al menos tres tazas grandes de café bien cargado"
text3 = "Aquí yace en paz eterna quien tristemente olvidó cerrar un paréntesis crucial en el código de producción justo antes del fin de semana largo"

print("\n-------- slicings positivos --------")

print("1.", text1[:44])
print("2.", text3[12:98])
print("3.", text2[87:97])
print("4.", text2[123:])
print("5.", text1[75:100])

print("\n-------- slicings negativos --------")

print("6.", text3[-50:-1])
print("7.", text2[-63:-31])
print("8.", text1[-130:-70])
print("9.", text3[-65:-50])
print("10.", text2[-40:])