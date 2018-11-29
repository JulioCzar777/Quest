lista = list()
while (True):
    nota = float(input("Digite suas notas: "))
    if (nota == -1):
        break
    lista.append(nota)
t = len(lista)
print(f"A quantidade de valores lidos foi {t}")
print(f"Os valores informados foi {lista}")
inversa = []
c = t - 1
while (c >=0 ):
    inversa.append(lista[c])
    c -= 1
print(f"O inverso dos valores digitados foi {inversa}")
soma = 0
for num in lista:
    soma += num
Media = soma / t
print(f"A Soma de todos os valores digitados foi {soma}")
print(f"O valor da Média final foi {Media:.1f}")
Maiorm = []
menor7 = []
for n in lista:
    if (n > Media):
        Maiorm.append(n)
    if (n < 7):
        menor7.append(n)
print(f"Os valores maiores que a Média é {Maiorm}")
print(f"Os valores menores que 7 foi {menor7}")
print("Fim do Programa :)")
