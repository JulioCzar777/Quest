print('-=' * 13)
print(' SUPERMERCADO TABAJARA')
print(' Carnes: File Duplo, Alcatra e Picnha')
print(' Formas De Pagamento: Cartão Tabajara, Dinheiro, Outros')
print('-=' * 13)
tipo = str(input('Qual o seu tipo de carne? ')).strip().upper()
quantidade = int(input('Qual a quantidade de carne? '))
tpagamento = str(input('Qual o tipo de pagamento? '))
if tipo == 'FILE DUPLO':
  if quantidade < 5:
        total = quantidade * 4.90
  else:
        total = quantidade * 5.90
if tipo == 'ALCATRA':
  if quantidade < 5:
        total = quantidade * 5.90
  else:
    total = quantidade * 6.80
if tipo == 'PICANHA':
    if quantidade < 5:
        total = quantidade * 6.90
    else:
        total = quantidade * 7.80
print('-=' * 13)
print('      CUPOM FISCAL')
print(f'Tipo de carne: {tipo}')
print(f'Quantidade de carne: {quantidade}')
print('Total sem desconto: {:.2f}'.format(total))
print(f'Tipo de pagamento: {tpagamento}')
tpagamento = tpagamento.upper()
if tpagamento in 'CARTAO TABAJARA CARTÃO TABAJARA CARTAOTABAJARACARTÃOTABAJARA':
    print(f'Valor do desconto: R${total * 0.05:.2f}')
else:
    print('Valor do desconto: R$0.00')
print('Total a pagar: R${:.2f}'.format(total - (total * 0.05)))
print('-=' * 13)
