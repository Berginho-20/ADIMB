import sqlite3

def conectar():
    return sqlite3.connect('academia.db')

def criar_tabela():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS alunos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            modalidade TEXT,
            graduacao TEXT,
            endereco TEXT,
            nascimento TEXT,
            cpf TEXT ,
            celular TEXT,
            data_inicio TEXT,
            vencimento_dia INT,
            valor REAL,
            plano TEXT,
            pagamento TEXT
        )
    ''')
    conn.commit()
    conn.close()

def inserir_aluno(dados):
    conn = conectar()
    cursor = conn.cursor()
    sql = '''INSERT INTO alunos (nome, modalidade, graduacao, endereco, nascimento, 
             cpf, celular, data_inicio, vencimento_dia, valor, plano, pagamento)
             VALUES (?,?,?,?,?,?,?,?,?,?,?,?)'''
    cursor.execute(sql, dados)
    conn.commit()
    conn.close()

def listar_alunos():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM alunos")
    lista = cursor.fetchall()
    conn.close()
    return lista
# Adicione isso ao final do seu bdd.py

def buscar_aluno_por_nome(nome):
    conn = conectar()
    cursor = conn.cursor()
    # O LIKE permite buscar parte do nome (ex: buscar 'Ana' traz 'Ana Maria')
    cursor.execute("SELECT * FROM alunos WHERE nome LIKE ?", (f'%{nome}%',))
    resultados = cursor.fetchall()
    conn.close()
    return resultados

def excluir_aluno(id_aluno):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM alunos WHERE id = ?", (id_aluno,))
    conn.commit()
    conn.close()

def atualizar_aluno(id_aluno, coluna, novo_valor):
    conn = conectar()
    cursor = conn.cursor()
    # Usamos f-string na coluna apenas porque nomes de colunas não aceitam o ? do SQL
    sql = f"UPDATE alunos SET {coluna} = ? WHERE id = ?"
    cursor.execute(sql, (novo_valor, id_aluno))
    conn.commit()
    conn.close()
