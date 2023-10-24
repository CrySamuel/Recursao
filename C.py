def sequencia_B(n):
    if n == 1:
        return 1
    else:
        return sequencia_B(n - 1) + n ** 2
    
n = 10
resultado1 = sequencia_B(n)
print(f"B({n}) = {resultado1}")