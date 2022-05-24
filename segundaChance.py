qtd = int(input())
l1 = []
l2 = []
dif = 0
for c in range(qtd*2):
    if c < qtd:
        x = float(input())
        l1.append(x)
    else:
        x = float(input())
        l2.append(x)
for c, item in enumerate(l1):
    if item < 10 and l2[c] == 10:
        dif += 1
print(f'NOTAS ALTERADAS: {dif}')
for c, item in enumerate(l1):
    if item == 10 or l2[c] < 10:
        print(f'-({c+1:0>3}) original: {item:0>4}0 | final: {item:0>4}0')
    else:
        if l2[c] == 10:
            if item+2 >= 10:
                print(f'({c+1:0>3}) original: {item:0>4}0 | final: 10.00')
            else:
                print(f'*({c+1:0>3}) original: {item:0>4}0 | final: {item+2:0>4}0')
