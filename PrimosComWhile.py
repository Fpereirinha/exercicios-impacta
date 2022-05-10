n1 = int(input())
n2 = int(input())
div = soma = 0
while n1 <= n2 and n2 <= 5000:
    for c in range(1, n1):
        if n1 % c == 0:
            div += 1
    if div == 1:
        soma += 1
        print(n1)
    div = 0
    n1 += 1
print(f'primos: {soma}')