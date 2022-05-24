x = soma = cont = 0
lista = []
while x >= 0:
    x = int(input())
    if x > 0:
        soma += x
        cont += 1
        lista.append(x)
print(f'MEDIA: {soma / cont:.2f}')
for item in lista:
    if item < soma / cont:
        print(item)
