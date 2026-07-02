p = int(input("p = "))
q = int(input("q = "))

n = p * q
phi = (p - 1) * (q - 1)

e = int(input("e = "))

d = 1
while (d * e) % phi != 1:
    d += 1

print(f"\nn = {n}")
print(f"φ(n) = {phi}")
print(f"Открытый ключ: {{e, n}} = {{{e}, {n}}}")
print(f"Закрытый ключ: {{d, n}} = {{{d}, {n}}}")
