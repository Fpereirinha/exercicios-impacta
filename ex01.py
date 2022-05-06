x = float(input())
y = float(input())
print(f'{x*y:.2f}')
print(f'{(x*y) * (1 - (.1 + (.01*y))):.2f}')