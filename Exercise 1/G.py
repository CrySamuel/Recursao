def sequencia_T(n):
    if n == 1:
        return 2
    elif n == 2:
        return 5
    elif n == 3:
        return 3
    else:
        return sequencia_T(n - 1) + 2 * sequencia_T(n - 2) + 3 * sequencia_T(n - 3)
    
n = 3
resultado1 = sequencia_T(n)
print(f"T({n}) resultado = {resultado1}")