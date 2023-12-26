#Backtracking

n = 5
c = 4

mov = [[0, 1], [1, 0]]

def evaluarMov(solu, nuevoX, nuevoY):
    return 0 <= nuevoX < n and 0 <= nuevoY < n and solu[nuevoX][nuevoY] == 0

def despacha(pedido, almacen, tipo, solu, visitado, iniX, iniY):
    if all(v == 1 for v in visitado):
        return solu

    for i in range(len(mov)):
        nuevoX = iniX + mov[i][0]
        nuevoY = iniY + mov[i][1]

        if evaluarMov(solu, nuevoX, nuevoY):
            for j in range(len(visitado)):
                if (
                    pedido[j][0] == almacen[nuevoX][nuevoY]
                    and pedido[j][1] == tipo[nuevoX][nuevoY]
                    and visitado[j] == 0
                ):
                    visitado[j] = 1
                    solu[nuevoX][nuevoY] = almacen[nuevoX][nuevoY]

                    result = despacha(pedido, almacen, tipo, solu, visitado, nuevoX, nuevoY)

                    if result is not None:
                        return result

                    visitado[j] = 0
                    solu[nuevoX][nuevoY] = 0

                else:
                    result = despacha(pedido, almacen, tipo, solu, visitado, nuevoX, nuevoY)
                    if result is not None:
                        return result

    return None

pedido = [[5, 'A'], [1, 'V'], [50, 'M'], [8, 'A']]
visitado = [0, 0, 0, 0]

almacen = [
    [20, 10, 10, 25, 10],
    [10, 1, 10, 5, 15],
    [1, 20, 50, 5, 1],
    [25, 10, 8, 5, 15],
    [10, 2, 8, 10, 10]
]

tipo = [
    ['A', 'V', 'A', 'M', 'M'],
    ['A', 'V', 'M', 'A', 'V'],
    ['V', 'M', 'M', 'M', 'A'],
    ['V', 'A', 'A', 'A', 'V'],
    ['M', 'M', 'M', 'M', 'A']
]

solu = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]


result = despacha(pedido, almacen, tipo, solu, visitado, 0, 0)

if result is not None:
    print("\nLas ubicaciones del pedido son las siguientes:")
    for i in range(n):
        for j in range(n):
            if result[i][j] > 0:
                print(f"{result[i][j]}({tipo[i][j]})".rjust(3), end="  ")
            else:
                print(f"{result[i][j]}".rjust(5), end="   ")
        print()
    print("\nSI se puede despachar")
else:
    print("NO se puede despachar")




