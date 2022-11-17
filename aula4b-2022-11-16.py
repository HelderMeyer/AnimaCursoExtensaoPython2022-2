# Primeiro passo: importar a biblioteca sqlite3

import sqlite3

# Segundo passo: Vamos estabelecer uma conexão com o banco

conexao = sqlite3.connect("dc_universe.db")

# Terceiro passo: Criar um objeto do tipo cursor

cursor = conexao.cursor()

# Quarto passo: comando para inserir um herói/vilão

sql = "INSERT INTO pessoas (pessoa_id, nome, nome_civil, tipo) VALUES (12,'The Flash','Barry Allen','Herói(na)')"

# Quinto passo: Executar o comando SQL

print(cursor.execute(sql))

# Sexto passo: Confirmar o INSERT com o commit() e fechar o banco

conexao.commit()
conexao.close()