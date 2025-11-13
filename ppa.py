from itertools import permutations, combinations, product


def get_number_productions(numeros):
    return product(numeros, repeat=2)


def melter_with_operations(number_productions:list, operaciones:str):
    for nums in number_productions:
        fist = nums[0]
        second = operaciones
        third = nums[1]
        yield (fist, second, third)

def extend_operations(operaciones, numeros, expresionlist):
    for expresion in expresionlist:
        # Agregar solo operaciones
        for operacion in operaciones:
            yield expresion + (operacion,)
        
        # Agregar solo números
        for numero in numeros:
            yield expresion + (numero,)



# print("_____"*10)
# print(list(melter_with_operations(get_number_productions(['1', '2']), '+')))
# print("_____"*10)
# print(list(extend_operations(['+'], ['1'], [('1', '+', '1'), ('1', '+', '2'), ('2', '+', '1'), ('2', '+', '2')])))
# print("=================="*10)  


expresionlist = list(get_number_productions(['1','2','+']))
def evaluar_expresion(expresion):
    # evaluar la expresion sin importar el tamaño
    evaluacion = {}
    for exp in expresion:
        # Agrupar números consecutivos (concatenar)
        elementos_procesados = []
        i = 0
        while i < len(exp):
            elemento = str(exp[i])
            # Si es un dígito, seguir concatenando los siguientes dígitos
            if elemento.isdigit():
                numero_concatenado = elemento
                i += 1
                while i < len(exp) and str(exp[i]).isdigit():
                    numero_concatenado += str(exp[i])
                    i += 1
                elementos_procesados.append(numero_concatenado)
            else:
                # Es una operación
                elementos_procesados.append(elemento)
                i += 1
        
        # Construir la expresión con los números concatenados
        expr_str = ' '.join(elementos_procesados)
        try:
            resultado = eval(expr_str)
        except Exception as e:
            print(f"Error al evaluar la expresión {expr_str}: {e}")
            evaluacion[exp] = None
            continue
        evaluacion[exp] = resultado
    return evaluacion
evaluar = evaluar_expresion(expresionlist)

# print(evaluar)

def objetivo_encontrado(evaluacion, objetivo):
    for exp, resultado in evaluacion.items():
        print(exp, resultado)
        if resultado is None:
            continue
        if round(resultado) == objetivo:
            return {'expresion': exp, 'resultado': resultado}
    return False

def recursive_objetivo_encontrado(evaluacion, objetivo, operaciones, numeros):
    encontrad = objetivo_encontrado(evaluacion, objetivo)
    if encontrad:
        return encontrad
    else:
        print(operaciones, numeros, evaluacion)
        expresionlist = list(extend_operations(operaciones, numeros, evaluacion))
        print("Expresion expresionlist:", expresionlist)
        # Agrega operaciones y numeros a la llamada recursiva
        return recursive_objetivo_encontrado(
            evaluar_expresion(expresionlist), 
            objetivo, 
            operaciones,  # ✅ Agregado
            numeros       # ✅ Agregado
        )

encontrado = objetivo_encontrado(evaluar, 3)
print("====="*10)
# print(encontrado)
# for ops in combinations(operaciones, 2):  # 2 operaciones
#     print(ops)
# print("-----"*10)
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
    # numeros_conbinados = get_number_productions(numeros+[operaciones])
    # for operacion in operaciones:
    #     if verbose:
    #         print(f"Generando expresiones con la operación: {operacion}")
    #     for expresion in melter_with_operations(get_number_productions(numeros), operacion):
    #         if verbose:
    #             print(expresion)
    intentos = get_number_productions(numeros+operaciones)

    evaluacion = evaluar_expresion(intentos)
    if verbose:
        print(evaluacion)
    if verbose:
        if verbose:
            print(f"🔍 Evaluación de {(intentos)} expresiones:")
        for exp, resultado in evaluacion.items():
            print(f"   {' '.join(map(str, exp))} = {resultado}")
    # print(operaciones, numeros)
    encontrado = recursive_objetivo_encontrado(evaluacion, objetivo, operaciones, numeros)
    if encontrado:
        if verbose:
            # ✅ Extraer la expresión del diccionario
            expresion = encontrado['expresion']
            resultado = encontrado['resultado']
            print(f"\n✅ ¡Objetivo {objetivo} alcanzado con la expresión: {' '.join(map(str, expresion))} = {resultado}!")
        return encontrado
    
    return None

print("====="*10)
resultado = resolver_objetivo(834, ['7','5'], ['+'], verbose=False)
print(resultado)
print("====="*10)