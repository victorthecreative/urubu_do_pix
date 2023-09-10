import sqlite3
from datetime import datetime

def init_db():
    """Inicializa o banco de dados e cria a tabela de usuários se ela não existir."""
    conn = sqlite3.connect('urubu_do_pix.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY,
        nome TEXT NOT NULL,
        chave_aleatoria TEXT NOT NULL
    )
    ''')
    conn.commit()
    conn.close()

def inserir_usuario(nome, chave_aleatoria):
    """Insere um novo usuário no banco de dados."""
    with sqlite3.connect('urubu_do_pix.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
        INSERT INTO usuarios (nome, chave_aleatoria)
        VALUES (?, ?)
        ''', (nome, chave_aleatoria))
        conn.commit()

def buscar_usuarios():
    """Busca e retorna todos os usuários do banco de dados."""
    with sqlite3.connect('urubu_do_pix.db') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM usuarios')
        return cursor.fetchall()

def init_deposit_db():
    """Inicializa a tabela de depósitos se ela não existir."""
    conn = sqlite3.connect('urubu_do_pix.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS depositos (
        id INTEGER PRIMARY KEY,
        nome_usuario TEXT NOT NULL,
        chave_aleatoria TEXT NOT NULL,
        valor_deposito REAL NOT NULL,
        codigo_deposito TEXT NOT NULL,
        data_deposito TEXT NOT NULL
    )

    ''')
    conn.commit()
    conn.close()


def inserir_deposito(nome_usuario, chave_aleatoria, valor_deposito, codigo_deposito):
    data_atual = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with sqlite3.connect('urubu_do_pix.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
        INSERT INTO depositos (nome_usuario, chave_aleatoria, valor_deposito, codigo_deposito, data_deposito)
        VALUES (?, ?, ?, ?, ?)
        ''', (nome_usuario, chave_aleatoria, valor_deposito, codigo_deposito, data_atual))
        conn.commit()
        

def buscar_depositos():
    """Busca e retorna todos os depósitos do banco de dados."""
    with sqlite3.connect('urubu_do_pix.db') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM depositos')
        return cursor.fetchall()
    
def init_rendimento_db():
    """Inicializa a tabela de rendimentos se ela não existir."""
    conn = sqlite3.connect('urubu_do_pix.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS rendimentos (
        id INTEGER PRIMARY KEY,
        dia INTEGER NOT NULL,
        nome TEXT NOT NULL,
        chave_usuario TEXT NOT NULL,
        codigo_deposito TEXT NOT NULL,
        valor_depositado REAL NOT NULL,
        valor_rendimento REAL NOT NULL
    )
    ''')
    conn.commit()
    conn.close()

def inserir_rendimento(dia, nome, chave_usuario, codigo_deposito, valor_depositado, valor_rendimento):
    """Insere um novo rendimento no banco de dados."""
    with sqlite3.connect('urubu_do_pix.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
        INSERT INTO rendimentos (dia, nome, chave_usuario, codigo_deposito, valor_depositado, valor_rendimento)
        VALUES (?, ?, ?, ?, ?, ?)
        ''', (dia, nome, chave_usuario, codigo_deposito, valor_depositado, valor_rendimento))
        conn.commit()
        
def buscar_depositos_por_chave(chave_aleatoria):
    """Busca e retorna todos os depósitos associados a uma chave aleatória específica."""
    with sqlite3.connect('urubu_do_pix.db') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT id, nome_usuario, chave_aleatoria, valor_deposito, codigo_deposito, data_deposito FROM depositos WHERE chave_aleatoria = ?', (chave_aleatoria,))
        return cursor.fetchall()



    
