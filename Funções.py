def eh_primo(n):
    if n >= 2:
        for c in range(2, n):
            if n % c == 0:
                return False
        return True
    else:
        raise ValueError('Número deve ser maior ou igual a 2.')

def conta_primos(s):
    lista = dict()
    for item in s:
        if eh_primo(item):
            atual = lista.get(item, 0)
            lista[item] = atual + 1
    return dict(lista)

def lista_primos(n):
    return sorted([numero for numero in range(2, n) if eh_primo(numero)])

def eh_armstrong(n):
    if n >= 0:
        n_str = str(n)
        tamanho = len(n_str)
        sum_n = 0
        for c in range(tamanho):
            sum_n += int(n_str[c]) ** tamanho
    else:
        raise ValueError('Número deve ser maior ou igual a 0 !')
    return sum_n == n

def eh_quase_armstrong(n):
    if n>= 0:
        n_str = str(n)
        tamanho = len(n_str)
        sum_n = 0
        for c in range(tamanho):
            sum_n += int(n_str[c]) ** tamanho
    else:
        raise ValueError('Número deve ser maior ou igual a 0 !')
    return sum_n == n+1 or sum_n == n-1

def lista_armstrong(n):
    arms = []
    if n >= 0:
        for c in range(n):
            if eh_armstrong(c):
                arms.append(c)
    else:
        raise ValueError('Número deve ser maior ou igual a 0 !')
    return sorted(arms)

def eh_perfeito(n):
    if n >= 2:
        divisores = [numero for numero in range(1, n) if n % numero == 0]
    else:
        raise ValueError('Numero deve ser maior ou igual a 2 !')
    return sum(divisores) == n

def lista_perfeitos(n):
    if n >= 2:
        lista = [numero for numero in range(2,n) if eh_perfeito(numero)]
    else:
        raise ValueError('O número deve ser maior ou igual a 2 !')
    return sorted(lista)
