""" 
Estrutura lógicas and or not is

Operadores unários ex not
Operadores binários and, or, is

Para i and, ambos os valores precisam ser True
Para o or, um ou outro valor precisa ser true
Para o not, o valor do boleano é invertido, true é false ser for false vira true
Para o is o valor e comparado com um segundo valor, utilizado para compararacao
"""

ativo = True
logado = False
'''
if ativo or logado:
    print ('Bem vindo usuario')
else:
    print ('Voce precisa ativas sua conta. Por favor, cheque seu e.mail')
'''
if not ativo:
    print('Voce precisa ativar a sua conta, Por favor, cheque seu e.mail')
else:
    print ('Bem vindo usuario')

print (not True)
print (not False)

if ativo is True:
    print('Voce precisa ativar a sua conta')
else:
    print('Bem vindo usuario')

if ativo:
    print('Bem vindo usuario')
else:
    print('Voce precisa ativa sua conta')

print (ativo is True)
