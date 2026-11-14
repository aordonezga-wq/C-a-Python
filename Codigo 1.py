contador = 0
numero = input()
numeroi = int(numero)
while numeroi != 0:
    if numeroi > 0:
        contador += 1
    numero = input()
    numeroi = int(numero)
print(contador)