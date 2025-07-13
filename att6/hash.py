def two_sum(numeros, alvo):
    indice_por_valor = {}  
    for i, valor_atual in enumerate(numeros):
        complemento = alvo - valor_atual
        
        if complemento in indice_por_valor:
            return [indice_por_valor[complemento], i]
        
        indice_por_valor[valor_atual] = i
    
    return []


if __name__ == "__main__":

    numeros = [2, 7, 11, 15]

    alvo = 9

    resultado = two_sum(numeros, alvo)

    print(resultado)  # saída esperada: [0, 1]