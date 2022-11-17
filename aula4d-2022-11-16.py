import aula4c_2022_11_16 as bd

conexao, cursor = bd.conectar()

nome = input("Digite o nome do herói/vilão: ")
nome_civil = input("Informe o nome civil do herói/vilão (sua identidade secreta): ")
tipo_numerico = input("Tecle 1 para Herói(na) ou 2 para Vilã(o): ")

# Consulta para o valor máximo usado no banco

sql = "SELECT MAX(pessoa_id)+1 FROM pessoas"

cursor.execute(sql)
pessoa_id = cursor.fetchone()[0]

if(tipo_numerico) == "1":
  tipo = "Herói(na)"
else:
  tipo = "Vilã(o)"

sql2 = f"INSERT INTO pessoas (pessoa_id, nome, nome_civil, tipo) VALUES ('{pessoa_id}', '{nome}', '{nome_civil}', '{tipo}')"

cursor.execute(sql2)
conexao.commit()
conexao.close() 


