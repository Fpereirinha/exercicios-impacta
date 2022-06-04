def exibir(lista):
    lista.sort()
    for cont, c in enumerate(lista):
        if cont == len(lista) - 1:
            print(c)
        else:
            print(c, end=' ')
x = list(map(int, input().split()))
opc = 0
while True:
    opc = input().split()
    if opc[0] == 'exibir' or opc[0] == "encerrar":
        exibir(x)
        if opc[0] == "encerrar":
            break
    elif opc[0] == 'adicionar':
        x.append(int(opc[1]))
    elif opc[0] == 'remover':
        if int(opc[1]) in x:
            x.remove(int(opc[1]))
        else:
            print(f'código {int(opc[1])} não encontrado')
