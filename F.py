def sequencia_W(n):
    if n == 1:
        return 2
    elif n == 2:
        return 5
    else:
        return sequencia_W(n - 1)*sequencia_W(n -2)
    
n = 10
resultado1 = sequencia_W(n)
print(f"W({n}) resultado = {resultado1}")