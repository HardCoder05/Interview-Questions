#Dynamic Programming

def minDesperdicio(capacidad, pesos):
    n = len(pesos)
    dp = [[0] * (capacidad + 1) for _ in range(n + 1)]

    # Caso base: Para 0 productos, el desperdicio es igual a la capacidad del contenedor
    for j in range(capacidad + 1):
        dp[0][j] = j

    for i in range(1, n + 1):
        for j in range(capacidad + 1):
            if pesos[i - 1] <= j:
                dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - pesos[i - 1]])
            else:
                dp[i][j] = dp[i - 1][j]

    for i in range(n + 1):
        for j in range(capacidad + 1):
            print(f"{dp[i][j]:2}", end=" ")
        print()

    ganancia, encontre = 0, False
    for j in range(capacidad, -1, -1):
        for i in range(n, -1, -1):
            if dp[i][j] == 0:
                ganancia = j
                encontre = True
                break
        if encontre:
            break

    print(f"\nEl contenedor mas grande con el desperdicio igual a 0 sera de {ganancia} Toneladas.")

    return dp[n][capacidad]

def main():
    capacidad = 20
    n = 4
    pesos = [3, 4, 8, 10]

    desperdicio = minDesperdicio(capacidad, pesos)
    print(f"\nEl desperdicio de usar un contenedor de {capacidad} Toneladas sera {desperdicio} Toneladas.")

if __name__ == "__main__":
    main()



