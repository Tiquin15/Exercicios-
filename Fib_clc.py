"""
Crie um programa que lê um número n e mostra a sequência de Fibonacci até seu n-ésimo termo.

* for: 1
* if: 1
* var: 1
"""



n = int(input("n: "))
y = 1
x = 1
for _ in range(n):
    aux = x
    x = y
    y = x + y
    y = aux + y
    y = x + aux
    print(x)

#aux = y