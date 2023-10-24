def progressao_geometrica(a, r, n):
    return a * (r ** (n - 1))

a = 2  # Termo inicial
r = 3  # Razão
n = 4  # Termo desejado
resultado = progressao_geometrica(a, r, n)
print(f"PG({a}, {r}, {n}) = {resultado}")
