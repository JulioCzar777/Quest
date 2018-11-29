#Vetor1 e 2 definidos
vetor1 = [1,3,5,7,9,11,13,15,17,19]
vetor2 = [2,4,6,8,10,12,14,16,18,20]
vetor3 = []
for i in range(10):
  vetor3.append(vetor1[i])
  vetor3.append(vetor2[i])
print(vetor1)
print(vetor2)
print(vetor3)  
#Vetor1 e 2 indefinidos
import random
vetor1 = []
vetor2 = []
vetor3 = []
for i in range(10):
    vetor1.append(random.randint(1,100))
    vetor2.append(random.randint(1,100))
    vetor3.append(vetor1[i])
    vetor3.append(vetor2[i])
print(vetor1)
print(vetor2)
print(vetor3)
