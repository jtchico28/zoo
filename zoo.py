"""
1. Calcular precio y tipo en funcion de la edad y guardarlo en algun sitio para luego... OK

2. Pedir la edad -> OK
    Validar que sea entero positivo -> OK
    Pedir edades hasta que se introduzca ""

3. Calcular el precio total del grupo

4. mostrar el precio total y el desglose por tipo de entrada

"""

precioTotal = 0
grupoPersonas = []


catalogo_entradas = {
    "GRATUITA": {"precio": 0, "e_umbral": 3},
    "NINYOS": {"precio": 14, "e_umbral": 13}, 
    "ADULTOS": {"precio": 23, "e_umbral": 65},
    "JUBILADOS": {"precio": 18, "e_umbral": float('inf')}
}

factura = {
    "GRATUITA": 0,
    "NINYOS": 0,
    "ADULTOS": 0,
    "JUBILADOS": 0
}


def calculoPrecioYTipoBillete(edad: int):
    # TODO: Poner esta funcion de forma que los indices encajen con el
    precio = 0
    tipo = 0

    for tipo in catalogo_entradas:
        if edad < catalogo_entradas[tipo]["e_umbral"]:
            precio = catalogo_entradas[tipo]["precio"]
            break         

    return precio, tipo

def validaEnteroPositivo(dato: str):
    """
    Debe devolver True si dato es entero mayor o igual que cero
                  False en otro caso
    """
    res = False
    try:
        int(dato)
        res = True
    except ValueError:
        res = False
    return res


"""
Bucle de peticion de edades, para cada edad debe imprimir precio y tipo
y acabar cuando se introduzca ""
"""
while True:
    edad = input("Cuantos años tienes: ")
    if edad == "":
        break
    elif validaEnteroPositivo(edad):
        grupoPersonas.append(calculoPrecioYTipoBillete(int(edad)))

# grupoPersonas = [(0, 0), (23, 2), (23, 2), (18, 3), (18, 3)]

num_entradas = len(grupoPersonas)


for precio, tipo in grupoPersonas:
    precioTotal = precioTotal + precio
    factura[tipo] += 1


for clave in factura:
    print(f"{factura[clave]:2d} entradas {clave.lower()}: {factura[clave] * catalogo_entradas[clave]["precio"]:6.2f} €")


print("-" * 25)

print(f"Numero de entradas: {num_entradas:03d}")
print(f"Total a pagar.....: {precioTotal:.2f} €")