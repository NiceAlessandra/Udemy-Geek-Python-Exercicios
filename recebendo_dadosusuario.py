"""recebendo dados do usurio"""

#print ('Qual seu nome')
#nome = input() 
nome = input ('Qual o seu nome? ')
"""
Entrada de dados
Todo dados recebidos via input é uma string
textos entre aspas simples, duplas e triplas são strings em Python
aspas simples 'Angelina'
aspas duplas ""Angelina""
Aspas simples triplas '''Angelina'''
"""
# Aspas duplas triplas  """AAAA"""

# Processamento

# saida de dados
#Exemplo de print antigo

#print ('Seja bem vindo! %s' % nome)

#saida - Exemplo de print antigo
# print ('A %s tem %s anos' % (nome, idade))

#print ('Qual a sua idade? ')
#idade = input()
idade = int (input ('Qual a sua idade? '))

#print ('Seja bem vindo {0}'.format (nome))
print (f'Seja bem vindo {nome}')
#print (' A {0} tem {1} anos'. format(nome, idade))
print (f'A {nome} tem {idade} anos')

"""
int idade é um cast
cast é a conversão de um tipo de dado para outro
"""
print (f'A{nome} nasceu em {2022 - idade}') 