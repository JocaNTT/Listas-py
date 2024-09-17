mes = ['Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

temperaturas = []

for contador in range(12):
    temperatura = float(input(f"Digite a temperatura média de {mes[contador]}: "))
    temperaturas.append(temperatura)

soma_temperaturas = 0

for temp in temperaturas:
    soma_temperaturas += temp

media_ano = soma_temperaturas / 12

print(f"\nMédia anual das temperaturas: {media_ano:.2f}°C\n")

print('<=>'*30)

print(f"\nMeses com temperaturas acima da média anual:")
for contador in range(12):
    if temperaturas[contador] > media_ano:
        print(f"{contador + 1} – {mes[contador]}: {temperaturas[contador]:.2f}°C")
