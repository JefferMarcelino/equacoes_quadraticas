from typing import Counter
from delta import calc_delta
from X12 import calc


print("EQUAÇÕES QUADRÁTICAS SIMPLES")
print("-=" * 15)

a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))

delta = calc_delta(a, b, c)
sol = calc(a, b, c, delta)

order = None

try:
    sol.sort()
    order = True
except AttributeError:
    order = False
    pass

print("-=" * 15)
print(f"∆ = {delta}")
print("Sol: {", end="")
if order:
    counter = 0
    for X in sol:
        if counter == 0:
            print(X, end="; ")
            counter += 1
        else:
            print(X, end="")
            print("}")
else:
    print(sol, end="")
    print("}")
