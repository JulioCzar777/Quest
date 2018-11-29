tipo = str(input('Qual o seu tipo de carne? '))
quantidade = int(input('Qual a quantidade de carne? '))
tpagamento = str(input('Qual o tipo de pagamento? '))
lista1 = []
lista2 = []
lista3 = []
if tipo == 'File Duplo':
    if quantidade < 5:
        total = quantidade * 4.90
    else:
        total = quantidade * 5.90
if tipo == 'Alcatra':
    if quantidade < 5:
        total = quantidade * 5.90
    else:
        total = quantidade * 6.80
if tipo == 'Picanha':
    if quantidade < 5:
        total = quantidade * 6.90
    else:
        total = quantidade * 7.80
print('-=' * 13)
print('CUPOM FISCAL')
print(f'Tipo de carne: {tipo}')
print(f'Quantidade de carne: {quantidade}')
print(f'Total sem desconto: {total}')
print(f'Tipo de pagamento: {tpagamento}')
if tpagamento in 'Cartao Tabajara':
    print(f'Valor do desconto: R${total * 0.05:.2f}')
else:
    print('Valor do desconto: R$0.00')
print('Total a pagar: R${:.2f}'.format(total - (total * 0.05)))
print('-=' * 13)
