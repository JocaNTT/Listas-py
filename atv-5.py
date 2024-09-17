numeros = []

for contador in range(1,6):
    numero = int(input(f"\nDigite o {contador}º número: "))
    numeros.append(numero)

print(f"\nLista completa:", numeros)

print(f"\nNúmeros divisíveis por 3:")
for num in numeros:
    if num % 3 == 0:
        print(num)