x = list(map(int, input().split()))
opc = 0
while True:
    opc = input().split()
    if opc[0] == 'exibir':
        x.sort()
        for cont,c in enumerate(x):
            if cont == len(x)-1:
                print(c)
            else:
                print(c, end =' ')
    elif opc[0] == 'adicionar':
        x.append(int(opc[1]))
    elif opc[0] == 'remover':
        if int(opc[1]) in x:
            x.remove(int(opc[1]))
        else:
            print(f'código {int(opc[1])} não encontrado')
    elif opc[0] == 'encerrar':
        x.sort()
        for cont,c in enumerate(x):
            if cont == len(x)-1:
                print(c)
            else:
                print(c, end =' ')
        break
