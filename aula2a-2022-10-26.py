# Comando input(): permitar que o usuário digite algo

nome = input("Digite o seu nome: ")

idade = int(input("Digite a sua idade: "))

# Comando de saída, para exibir na tela

print("\nOlá, {}! Sua idade é {} anos.".format(nome,idade))

# E se eu quisesse mostrar o DOBRO da idade informada?

dobro = int(idade) * 2
print("O dobro da idade informada é {}.".format(dobro))

# Estrutura condicional - o famoso "Se/If"
# Se a pessoa for maior de idade, mostre "Você é maior de idade"

if idade >= 18:
  print("Você é maior de idade!")
else:
  print("Você é menor de idade!")

# Se quiser perguntar o gênero (M = Masculino e F = Feminino)
# Mostre (...e você também precisa/precisou prestar o serviço militar obrigatório)

genero = input("\nQual é o seu gênero (M - Masculino & F - Feminino): ").title()[0]

if genero == "M":
  print("\nVocê terá que fazer o alistamento militar")
elif genero == "F":
  print("\nVocê não precisa fazer o alistamento militar")

  