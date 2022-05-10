x = int(input())
y = int(input())
bi = 0
for x in range(x, y+1):
    if x % 4 == 0 and x % 100 != 0 or x % 400 == 0:
        print(x)
        bi += 1
print(f'bissextos: {bi}')