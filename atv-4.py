numeros = []

for contador in range(1,11):
    numero = int(input(f"Digite o {contador}º número inteiro: "))
    numeros.append(numero)

posicao = []
for contador in range(10):
    if numeros[contador] == 3:
        posicao.append(contador)

if posicao:
    print(f"\nO número 3 foi encontrado nas posições:", posicao)
else:
    print(f"\nO número 3 não foi encontrado na lista.")