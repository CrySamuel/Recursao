def Sequencia_S(n):
    if n == 1:
        return 10
    else:
        return Sequencia_S(n - 1) + 10

n = 10
resultado1 = Sequencia_S(n)
print(f"P({n}) = {resultado1}")