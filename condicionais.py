"""estruturas condicionais
if,else, elif

"""
#novo bloco se inicia com 2 pontos e indentação 4 esapços
idade = 18

if idade < 18:
    print ('Menor de idade')
#elif para o que serve?    
elif idade == 18:
    print ('Tem 18 anos')
elif idade == 26:
    print ('Tem 26 anos')
else:
    print ('Maior de Idade')

""" isso não é legal:
if idade < 18:
    print ('Menor de Idade')

if idade == 18:
    print ('Tem 18 anos')
    
if idade == 26:
    print ('Tem 26 anos')

if idade > 18:
    print ('Maior de idade')"""