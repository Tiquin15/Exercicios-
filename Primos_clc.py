"""
Crie um programa que mostre uma lista com todos os primos de 1 até n, onde
n é um valor fornecido pelo usuário.

O exercício possui algumas dicas de implementação na forma de comentários.

* for: 2
"""

# Acrescentamos os novos primos à lista de primos.
# Assumimos que o número é primo e tentamos encontrar o divisor.
# Um número não pode ser primo se for divisível por outro primo.

n = int(input("n: "))
primos = [2, 3]
nums = range(2, n + 1)

for x in nums:
  é_primo = True

  for p in primos:
   
    if x % p == 0:
      é_primo = False
   
  if é_primo:
      primos.append(x)

print(primos)


#nums = range(n)
#nums = range(2, n)