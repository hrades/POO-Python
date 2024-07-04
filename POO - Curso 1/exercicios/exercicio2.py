idade = int(input('Digite sua idade: '))

if idade%2 == 0:
    print(f'A sua idade é um número par')
else:
    print(f'A sua idade é um número ímpar')
    
if idade<=12:
    print('Você é uma criança')
elif idade<=18:
    print('Você é um adolescente')
elif idade<60:
    print('Você é um adulto')
else:
    print('Você é um idoso')