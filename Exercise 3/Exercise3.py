def pertence_a_T(n):
    if n == 2:
        return True

    if n > 2 and n % 2 == 1:
        return pertence_a_T(n - 3)

    if n > 2 and n % 2 == 0:
        return pertence_a_T(n // 2)

    return False

numero = int(input("Digite o número:"))

if pertence_a_T(numero):
    print(f"{numero} pertence a T")
else:
    print(f"{numero} não pertence a T")
    
# Os testes foram feito com os numeros 6, 7, 19, 12