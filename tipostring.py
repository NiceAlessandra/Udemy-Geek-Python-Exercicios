"""tipo string
E  python um dado é considerado do tipo string
sempre que 
-- estiver entre aspas simples 
' ' --> 'um string' 'a' '234' 'True"
qualquer dado entre aspas simples é uma string]
sempre que 
-- estiver entre aspas duplas
no python não existe diferença 
-- Estiver entre aspas simples triplas '''uma string''' '''123''' '''a'''
"""
# --Estiver entre aspas duplas triplas

"""nome = 'Nice Alessandra'
print (nome)
print(type(nome))

nome = "Gina's Bar"
print (nome)
print(type(nome))

nome = "Angelina \nJolie"
print (nome)
print(type(nome))

nome = aspas triplas Angelina Jolie """
# print (nome)
# print(type(nome))

nome = 'Nice Alessandra'
print (nome.upper())
print (nome.lower())
#o split transforma em uma lista de strings na saida, strings compostas
print (nome.split())
#nome desta operacao slice de string
print (nome[0:6])
print (nome[5:15])

print (nome.split()[0])
#saida Nice
print (nome.split()[1])
#saida Alessandra

#começando do 1o ao ultimo elemento e invertendo a impressao
#metodo super Pythonico - inversao da string
print (nome[::-1])
#saida Lice Alessandra substitue letras
print (nome.replace('N', 'L'))

#palindromo
texto = 'socorram me subino onibus em marrocos'
print(texto)
print (texto[::-1])
#palindromo
nome = 'ana'
print (nome)
print (nome[::-1])
