"""
ENUNCIADO:
Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os valores
pares e os valores ímpares digitados, respectivamente.
Ao final, mostre o conteúdo das três listas geradas.
"""

num = list()
pares = list()
ímpares = list()

while True:
 num.append(int(input('Digite um número: ')))

 resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
 if resp == 'N':
 break

for valor in num:
 if valor % 2 == 0:
 pares.append(valor)
 else:
 ímpares.append(valor)

print('-=' * 30)
print(f'A lista completa é {num}')
print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {ímpares}')