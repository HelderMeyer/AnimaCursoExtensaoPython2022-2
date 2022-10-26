# Comando input(): permitar que o usuário digite algo

nome = input("Digite o seu nome: ")

idade = int(input("Digite a sua idade: "))

# Comando de saída, para exibir na tela

print("Olá, {}! Sua idade é {} anos.".format(nome,idade))

if idade > 18:
  print("Você é maior de idade!")
else:
  print("VocÊ é menor de idade!")

# E se eu quisesse mostrar o DOBRO da idade informada?

dobro = int(idade) * 2
print("O dobro da idade informada é {}".format(dobro))
