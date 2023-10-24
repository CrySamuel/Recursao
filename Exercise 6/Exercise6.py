def pertence_a_W(s):
    if s == "a" or s == "b" or s == "c":
        return True
    if s.startswith("a") and s.endswith("c"):
        return pertence_a_W(s[1:-1])
    return False

cadeias = ["a(b)c", "a(a(b)c)c", "a(abc)c", "a(a(a(a)c)c)c", "a(aacc)c"]

for cadeia in cadeias:
    if pertence_a_W(cadeia):
        print(f'"{cadeia}" pertence a W.')
    else:
        print(f'"{cadeia}" não pertence a W.')
