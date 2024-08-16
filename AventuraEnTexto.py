opciones = {
    "izquierda":"Te encontrastes con un dragon",
    "derecha":"Encontrastes un tesoro",
"adelante":"Caistes en un pozo"
}

eleccion = input("Estas en un cruze. ¿Quieres ir a a la derecha, izquierda o adelante?: ")

if eleccion in opciones:
    print("Respuesta: ", opciones[eleccion])
else:
    print("opcion equivocada")