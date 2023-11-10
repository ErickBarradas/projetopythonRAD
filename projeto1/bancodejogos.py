import sqlite3 as sql

def connect():
    conn=sql.connect('bancodejogos.sqlite')
    cursor=conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTIS bancodejogos
                    (id INTERGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT,
                    status TEXT,
                    genero TEXT,
                    plataforma TEXT,
                    nota INTENGER)''')
    conn.commit()
    conn.close()

def insert(nome, status, genero, plataforma, nota):
    conn = sql.connect("bancodejogos.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO bancodejogos VALUES (NULL,?,?,?,?,?)",
                (nome, status, genero, plataforma, nota))
    conn.commit()
    conn.close()
    view()

def view():
    conn = sql.connect("bancodejogos.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM bancodejogos")
    rows = cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn = sql.connect("bancodejogos.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM bancodejogos WHERE id=?", (id,))
    conn.commit()
    conn.close()

def update(id, nome, status, genero, plataforma, nota ):
    conn = sql.connect("bancodejogos.db")
    cur = conn.cursor()
    cur.execute("UPDATE bancodejogos SET nome=?, status=?, genero=?, plataforma=?, nota=? WHERE id=?",
                (nome, status, genero, plataforma, nota))
    conn.commit()
    conn.close()


connect()