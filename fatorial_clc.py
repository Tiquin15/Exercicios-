
"""
Crie um programa que peça um número e calcule o seu fatorial

* for: 1
"""
n = int(input("n: "))
fat = 1
for x in range(1, n + 1):
      fat *= x

print(f"fat({n}) = {fat}")
#for i in range(n):
#fat *= x + 1
#fat = 0

