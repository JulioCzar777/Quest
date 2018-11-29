p1 = float(input('Digite sua primeira média: '))
p2 = float(input('Digite sua segunda média: '))
p3 = float(input('Digite sua terceira média: '))
media = (p1+p2+p3)/3
if media == 10:
  print('Aprovado com Distinção!')
elif media >= 7:  
  print('Aprovado!')
else:
  print('Reprovado!')  
