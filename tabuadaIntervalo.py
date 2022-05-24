x = int(input())
y = int(input())
if x <= y:
    for c in range(x,y+1):
        for x in range(10):
            print(f'{c} x {x+1} = {c * (x+1)}')
        print('----------')
else:
    print('Nenhuma tabuada no intervalo!')
