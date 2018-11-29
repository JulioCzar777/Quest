Lista = [ 
    "Telefonou para a vítima?[S/N]" ,
    "Esteve no local do crime?[S/N]" ,
    "Mora perto da vítima?[S/N]" ,
    "Devia para a vítima[S/N]?" ,
    "Já trabalhou com a vítima?[S/N]" 
]
resposta = 0
for c in Lista:
  resposta += (input(c) == "S")
if resposta == 5:
  print("Assassino")
elif resposta >=3:
  print("Cúmplice")
elif resposta ==2:
  print("Suspeito")
else:
  print("Inocente")
