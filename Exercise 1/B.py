def sequencia_A(n):
    if n == 1:
        return 2
    else:
        return sequencia_A(n - 1) ** -1

n = 10 
resultado = sequencia_A(n)
print(f"A({n}) = {resultado}")
