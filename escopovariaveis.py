"""
Escopo de variaveis
Dois casos de escopo
1o: Escopo das variaveis globais 
 -- Sao reconhecidas, seu escopo compreende todo o programa
2o: Escopo das variaveis locais
 -- Sao reconhecidas, apenas no bloco onde foram declaradas, ou seja
    seu escopo esta limitado ao bloco onde foi declarada
    
    Para declarar variaveis em Python
    nome da variavel = valor da variavel

Python é uma linguagem de  tipagem dinamica
Exemplo em C : int numero = 42
Exempo em java : int numero = 42
Exemplo em python numero = 42
"""
#variavel global
numero = 42
print (numero)
print (type(numero))

# string - reatribuicao
numero = 'Nice'
print (numero)
print (type(numero))

nao_existe = 1
print (nao_existe)

#exemplo de variavel local, criada dentro do bloco
#se nao atender a condicao não existe
numero = 42
#novo = 0
if numero > 10:
    novo = numero + 10 
    print (novo) #variavel novo eh local pois esta declarada dentro do if
    
print(novo)