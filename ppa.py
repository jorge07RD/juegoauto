from itertools import permutations, combinations, product

def resolver_objetivo(objetivo, numeros, operaciones, verbose=True):
    """
    Busca combinaciones de números para llegar al objetivo
    Cada número de la lista se usa máximo una vez
    """
    if verbose:
        print(f"🎯 Objetivo: {objetivo}")
        print(f"📊 Números disponibles: {numeros}")
        print(f"➕ Operaciones: {operaciones}\n")
    
    intentos = []
def get_number_productions(numeros):
    return product(numeros, repeat=2)


operaciones = ['2', '1','3']
for ops in permutations(operaciones):  # 2 operaciones
    print(ops)
print("-----"*10)
for ops in product(operaciones, repeat=2):  # 2 operaciones
    print(ops)
    
print("-----"*10)

for ops in combinations(operaciones, 2):  # 2 operaciones
    print(ops)
print("-----"*10)
# Resultado:
# ('+', '+')
# ('+', '-')
# ('+', '*')
# ('-', '+')
# ('-', '-')
# ('-', '*')
# ('*', '+')
# ('*', '-')
# ('*', '*')