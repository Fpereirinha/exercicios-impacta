soma = 0
x = float(input())
while x != -1:
    soma += x
    x = float(input())
print(f'VC$ {soma:.2f}')
print(f'R$ {soma*2.5:.2f}')