# Criação de funções

preco = 1999.90

# Calcular 5% de imposto, guardar na variável imposto e exibir na tela

imposto = preco * 0.05
print(imposto)

preco2 = 100
imposto2 = preco2 * 0.05
print(imposto2)

# Criação de uma função Calcular_Imposto, que calcula um imposto de 5% e retorna a quem pediu...

preco3 = float(input("Digite o preço: "))

def calcular_imposto(preco_produto):
  imposto = preco_produto * 0.05
  return imposto

imposto3 = calcular_imposto(preco3)

print("O valor do imposto é de R${}".format(imposto3))

# Agora calcular imposto a alíquota agora é 7%

valores = [1.99, 24.50, 78.27, 1515.5]

# Se eu quiser calcular o imposto destes quatro valores... e exibir na tela assim: "O imposto de ... é ..." (1o. preço, 2o. imposto)

for valor in valores:

  print(f"O imposto de {valor} é {calcular_imposto(valor)}")