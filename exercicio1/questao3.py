
nome = input("Qual o seu nome? ")
print("Por favor responda as perguntas abaixo com SIM ou NÃO")

perguntas = ("Telefonou para vitima? ","Esteve no local do crime? ","Mora perto da vitima? ",
             "Devia para a vitima? ", "Já trabalhou com a vitima? "  )

respostas = []

for i in range(len(perguntas)):
 entrada = input(perguntas[i])
 respostas.append(entrada)

soma = 0

for i in range(len(respostas)):
 if (respostas[i] == "SIM" or respostas[i] == "sim"):
   soma += 1
if (soma == 2):
 print("SUSPEITO")
elif (soma == 3 or soma == 4):
 print("CÚMPLICE")
elif (soma == 5):
 print("ASSASSINO")
else:
 print("INOCENTE")
