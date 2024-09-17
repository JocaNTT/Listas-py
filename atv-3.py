numeros = []

for i in range(1,7):
    num = float(input(f"\nDigite o número quaquer {i}: "))
    numeros.append(num)

print(f"\nLista de números:", numeros)

pos1 = int(input(f"\nEscolha a primeira posição (1 a 6): ")) - 1
pos2 = int(input("Escolha a segunda posição (1 a 6): ")) - 1

num1 = numeros[pos1]
num2 = numeros[pos2]

mult = num1 * num2
som = num1 + num2
sub = num1 - num2
div = num1 / num2 if num2 != 0 else "Não funciona"
potnc = num1 ** num2

print(f"\nOperações entre os números nas posições {pos1 + 1} e {pos2 + 1}:")
print(f"Produto: {mult}")
print(f"Soma: {som}")
print(f"Diferença: {sub}")
print(f"Divisão: {div}")
print(f"Potenciação: {potnc}")