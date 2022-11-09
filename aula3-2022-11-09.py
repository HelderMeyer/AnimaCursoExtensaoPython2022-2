print("Início da aula 3 (09/11/2022)")

contador = 1

# Exibir de 1 até 10 repetidamente

while(contador <= 10):
  print(contador)
  contador += 1

# Laço for (python for = for each)

fruta = "morango"

print(fruta)

# Lista

frutas = ["Morango","Maçã","Melão"]

# Mostra todas as frutas

print(frutas)

# Mostra apenas uma fruta especificada (Terceira fruta)

print(frutas[2])

# Exibir quantas frutas tem na lista

print(len(frutas)) # len = lenght (tamanho)

# Quero incluir uma fruta nova

frutas.append("Manga")
print(len(frutas))
print(frutas)

print(frutas[0])
print(frutas[1])
print(frutas[2])
print(frutas[3])

print("\n")

i = 0
while(i<len(frutas)):
  print(frutas[i])
  i += 1