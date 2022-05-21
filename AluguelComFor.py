valordiv = int(input())
mensal = int(input())
for c, x in enumerate(range(valordiv, 0, -mensal)):
    print(f'pagamento: {c+1}')
    print(f'antes = {x}')
    if x - mensal >= 0:
        print(f'depois = {x - mensal}')
    else:
        print(f'depois = 0')
    print('-' * 5)
