def mcm(n):
    """Mínimo común múltiplo del número 'n'.
    """
    assert (type(n) == int) and (n > 1), f'El número debe ser un entero positivo mayor a 1'
        
    divisores = range(2,n+1)
    factores = dict()
    
    for div in divisores:
        
        while n % div == 0:
            if div not in factores:
                factores[div] = 1
            else:
                factores[div] += 1
            n = n/div

    lista_de_factores = [key for key in factores.keys()]
    lista_de_exponentes = [exp for exp in factores.values()]

    return lista_de_factores, lista_de_exponentes

def mcm2(n):
    """Mínimo común múltiplo del número 'n'.
    """
    assert (type(n) == int) and (n > 1), f'El número debe ser un entero positivo mayor a 1'
        
    divisores = range(2,n+1)
    factores = dict()
    
    for div in divisores:
        
        while n % div == 0:
            
            factores[div] = factores.get(div,0) + 1
            n = n/div

    lista_de_factores = [key for key in factores.keys()]
    lista_de_exponentes = [exp for exp in factores.values()]

    return lista_de_factores, lista_de_exponentes
    
print(mcm2(32))
print(mcm2(96))
print(mcm(225688548))