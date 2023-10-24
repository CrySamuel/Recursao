def pertence_a_S(s):
    if s == "a" or s == "b":
        return True
    if s.startswith("a") and pertence_a_S(s[1:]):
        return True
    if s.endswith("b") and pertence_a_S(s[:-1]):
        return True
    return False

cadeias = ["a", "ab", "aba", "aaab", "bbbbb"]

for cadeia in cadeias:
    if pertence_a_S(cadeia):
        print(f'"{cadeia}" pertence a S.')
    else:
        print(f'"{cadeia}" não pertence a S.')
