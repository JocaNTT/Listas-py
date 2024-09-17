itens = []

while True:
    num = int(input("Digite um valor (ou um valor negativo para encerrar): "))
    if num < 0:
        break
    itens.append(num)

print(f"\nLista completa:", itens)

for valor in itens:
    if valor % 2 == 0:
        itens.remove(valor)

print(f"\nLista após remover números pares:", itens)