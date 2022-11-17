# Primeiro passo: importar a biblioteca sqlite3

import sqlite3

# PASSOS 2 E 3 VIRARÃO FUNÇÃO CONECTAR()

def conectar():

  # Segundo passo: Vamos estabelecer uma conexão com o banco

  conexao = sqlite3.connect("dc_universe.db")

  # Terceiro passo: Criar um objeto do tipo cursor

  cursor = conexao.cursor()

  return conexao, cursor



