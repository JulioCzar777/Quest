precofile5 = 4.9
precofile6 = 5.8
precoalcatra5 = 5.9
precoalcatra6 = 6.8
precopicanha5 = 6.9
precopicanha6 = 7.8
precokg = 0.0
tiposcarne = ["Filé Duplo", "Alcatra","Picanha"]
carneescolhida =""
quantidadecarne = 0.0
formaspagamento = ["Cartão Tabajara","Outros"]
pagamentoescolhido= ""
descontocartao= 0.05
valordesconto = 0.0
print("Tipos de carne disponíveis:")
print(tiposcarne)
while carneescolhida not in tiposcarne:
  carneescolhida = str(input("Qual tipo de carne?"))
while quantidadecarne <=0:
  quantidadecarne = float(input("Quantidade?"))
print("Formas de Pagamento:")
print(formaspagamento)
while pagamentoescolhido not in formaspagamento:
  pagamentoescolhido = str(input("Forma de pagamento escolhida"))
if carneescolhida =="Filé Duplo" and quantidadecarne < 6:
  precokg = precofile5*quantidadecarne
if carneescolhida =="Filé Duplo" and quantidadecarne >= 6:
  precokg = precofile6*quantidadecarne
if carneescolhida =="Alcatra" and quantidadecarne < 6:
  precokg = precoalcatra5*quantidadecarne
if carneescolhida =="Alcatra" and quantidadecarne >= 6:
  precokg = precoalcatra6*quantidadecarne
if carneescolhida =="Picanha" and quantidadecarne < 6:
  precokg = precopicanha5*quantidadecarne
if carneescolhida =="Picanha" and quantidadecarne >= 6:
  precokg = precopicanha6*quantidadecarne
print ("Cupom fiscal")
print("Carne escolhida:{} ".format(carneescolhida))
print("Quantidade:{}Kg".format(quantidadecarne)
print("Preço total:{}R$".format(precokg))
if pagamentoescolhido == "Cartão Tabajara":
  print("Desconto:{}R$".format(descontocartao))
else:
  print(("Desconto:{}R$".format(valordesconto))  
if pagamentoescolhido == "Cartão Tabajara":
  precokg = precokg/descontocartao  
  print("Valor a pagar:{}R$".format(precokg))
else:
  print("Valor a pagar:{}R$".format(precokg))        
