def pertence_a_M(n):
    if n == 2 or n == 3:
        return True
    if n < 2:
        return False

    # Recursão
    for x in range(2, n):
        if pertence_a_M(x) and pertence_a_M(n - x):
            return True
    
    return False

numeros = [ 6 , 9 , 16 , 21 , 26 , 54 , 72 , 218]

for numero in numeros:
    if pertence_a_M(numero):
        print(f"{numero} pertence a M.")
    else:
        print(f"{numero} não pertence a M.")
