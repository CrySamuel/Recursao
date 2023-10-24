def sequencia_D(n):
    if n == 1:
        return 3
    elif n == 2:
        return 5
    else:
        return (n - 1)*sequencia_D(n - 1) + (n - 2)*sequencia_D(n - 2)
    
n = 20
resultado1 = sequencia_D(n)
print(f"D({n}) resultado = {resultado1}")