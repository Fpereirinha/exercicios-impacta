alfabet = [['A'], ['B'], ['C'], ['D'], ['E'], ['F'], ['G'], ['H'], ['I'], ['J'], ['K'], ['L'], ['M'], ['N'],
           ['O'], ['P'], ['Q'], ['R'], ['S'], ['T'], ['U'], ['V'], ['W'], ['X'], ['Y'], ['Z']]
x = int(input())
for contador, lista in enumerate(alfabet[:x]):
    for letra in lista:
        print(f'{letra*(contador+1)}')
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

alfabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
x = int(input())
for contador, letra in enumerate(alfabet[:x]):
    print(f'{letra*(contador+1)}')
