def bonus():
    print('-'*5)
    print('BÔNUS')
    print('-'*5)
x = []
qtd = int(input())
for c in range(qtd):
    canal = input().split(';')
    x.append(canal)
cpremium = float(input())
ccomum = float(input())
bonus()
for item in x:
    print(f'{item[0]}: R$ ',end='')
    if item[3] == 'não':
        print(f'{(float(item[1]) // 1000) * ccomum + float(item[2]):.2f}')
    elif item[3] == 'sim':
        print(f'{(float(item[1]) // 1000) * cpremium + float(item[2]):.2f}')
