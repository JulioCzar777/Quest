carros = ['Fusca', 'Gol', 'Uno', 'Vectra', 'Peugeot']
kmclitro = [7, 10, 12.5, 9, 14.5]
maior = kmclitro[0]
litros = []
consumototal = []
precoplitro = 0
for i in range(len(kmclitro)):
    if kmclitro[i] > maior:
        maior = kmclitro[i]
        posicao = i
for i in range(len(kmclitro)):
    litros.append(1000 / kmclitro[i])
    consumototal.append(litros[i] * 3.5)
print('-=-=-=-=-= COMPARATIVO =-=-=-=-=-')
for i in range(len(carros)):
    print('Veículo: {}'.format(i + 1))
    print('Nome do veículo: {}'.format(carros[i]))
    print('Km com 1 litro: {}'.format(kmclitro[i]))
    print('=' * 6)
print('-=-=-=-=-=-=-=-= RELATÓRIO =-=-=-=-=-=-=-=-=-   ')
print('Nome   /   Consumo com 1L  /Litros   /Preço')
for i in range(len(carros)):
    print('1  -  {}  /  {:.2f}  /  {:.2f}L  /  R${:.2f}'.format(carros[i], kmclitro[i], litros[i], consumototal[i]))
