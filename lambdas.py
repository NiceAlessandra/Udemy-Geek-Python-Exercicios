""" 
Utilizando lambdas
Conhecidas por expressoes sem nome, 
funcoes anonimas

def soma (a, b):
    return a+b
"""
# exemplo de funcao em python
'''
def funcao (x):
    return 3 + x + 1 

print (funcao (4))
print (funcao (7))

#exemplo de expressao lambda

lambda x: 3 * x + 1 

#como utilizar a expressao lambda
#cnao é uma forma digma de se utilizar o lambda -->> riar uma variavel recebendo uma expressao lambda
calc = lambda x: 3 * x + 1

print (calc(4))
print (calc(7))
'''
# podemos ter expressoes lambda com multiplas entradas
'''
nome_completo = lambda nome, sobrenome: nome.strip().title() +' '+ sobrenome.strip().title()

print (nome_completo (' angelina ', 'JOLIE'))
print (nome_completo (' FELICITY    ', '   jones  '))
'''

# em funcoes python podemos ter nenhuma ou varias entradas em lambdas tambem 


#lambda sem nehuma entrada
'''
amar = lambda: 'como nao amar python? '

uma = lambda x: 3 * x  + 1 

duas = lambda x, y: (x * y ) ** 0.5

tres  = lambda x, y, z: 3/ (1 / x + 1 / y + 1 / z)

# n = lambda x1, x2, xn; <expressao>

print (amar())
print (uma(6))
print (duas(5, 7))
print (tres(3, 6, 9))

#outro exemplo
autores = ['Isaac Asinov', 'Ray C. Bradbury', 'Clarice Lispector', 'Machado de Assis', 
            'Oscar Wilde', 'Nice  Alessandra Montarroyos']

print (autores)

autores.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].lower())

print (autores)

'''
# funcao quadratica
# f(x) = a * x ** 2 + b * x + c
# definindo a funcao 

def geradora_funcao_quadratica (a, b, c):
    """Retorna a funcao f(x) = a * x ** 2 + b * x + c"""
    return lambda x: a * x ** 2 + b * x + c

teste = geradora_funcao_quadratica (2, 3, -5)

print (teste(0))
print (teste(1))
print (teste(2))

print (geradora_funcao_quadratica(3, 0, 1)(2))

