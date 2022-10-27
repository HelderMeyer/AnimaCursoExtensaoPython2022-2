# Pede o nome do aluno e sua nota (de 0 a 10) e, se ele tirou nota 10, mostra "Você é o bichão mesmo!"

nomeAluno = input("Qual é o seu nome: ")
notaAluno = float(input("Qual foi sua nota: "))

if notaAluno == 10:
  print("\nParabéns, {}! Você é o bichão mesmo, hein?".format(nomeAluno))
elif notaAluno >= 7 and notaAluno < 10:
  print("Parabéns pela nota!")
elif notaAluno > 0 and notaAluno < 7:
  print("Você pode melhorar!")
elif notaAluno == 0:
  print("Foi quase... Tenta estudar mais, você consegue!")
else:
  print("Como assim????")