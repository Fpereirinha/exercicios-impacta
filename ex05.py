trabalho = float(input())
prova = float(input())
media = (trabalho + prova) / 2
if media >= 6.0:
    print('aprovado')
elif (trabalho + 10) / 2 >= 6:
    print('talvez com a sub')
else:
    print('reprovado')