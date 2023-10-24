def sequencia_P(n):
    if n == 1:
        return 1
    else:
        return n**2 * sequencia_P(n - 1) + n - 1
    
n = 10
resultado1 = sequencia_P(n)
print(f"P({n}) = {resultado1}")