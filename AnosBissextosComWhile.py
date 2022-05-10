inicio = int(input())
fim = int(input())
soma = 0
while 0 <= inicio <= fim <= 9999:
    if inicio % 4 == 0 and inicio % 100 != 0 or inicio % 400 == 0:
        print(inicio)
        soma += 1
    inicio += 1
print(f'bissextos: {soma}')