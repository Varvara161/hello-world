g = int(input("g = "))
p = int(input("p = "))
a = int(input("a = "))
b = int(input("b = "))

A = pow(g, a, p)
B = pow(g, b, p)
K = pow(g, a * b, p)

print(f"\nA = {A}")
print(f"B = {B}")
print(f"Общий ключ K = {K}")
print(f"Проверка: {pow(B, a, p)} = {pow(A, b, p)} = {K}")
