"""
Crie um programa que peça um número no terminal e conte a quantidade de 
zeros à esquerda do mesmo.

* while: 1
* str: 1
"""

number = input("n: ")

n = 0
while number.startswith("0"):
    while number[0] == "0":
        n += 1
        number = number[1:]
   

         
print(f"número de zeros = {n}")
#number = int(number)
#while number == "0": 