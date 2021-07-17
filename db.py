import sqlite3

# Connect to sqlite database

def criarBD():
    conn = sqlite3.connect('empresas.db')
    cursor = conn.cursor()

    cursor.execute("DROP TABLE IF EXISTS EMPRESA")
    cursor.execute("DROP TABLE IF EXISTS SERVICO")
    cursor.execute("DROP TABLE IF EXISTS SERVICO_PRESTADO")
    cursor.execute("DROP TABLE IF EXISTS ATIVIDADE")

    query = """
    CREATE TABLE empresa(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome varchar(100) NOT NULL,   
        cnpj varchar(14) unique,
        telefone varchar(11),
        email varchar(100),
        uf varchar(2)
    )"""

    cursor.execute(query)

    query = """ 
    CREATE TABLE servico(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome varchar(100) NOT NULL,
        empresa_id INTEGER,
        foreign key (empresa_id) references empresa(id) ON DELETE CASCADE  
    )"""

    cursor.execute(query)

    query = """ 
    CREATE TABLE servico_prestado(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        empresa_id INTEGER,
        servico_id INTEGER,
        foreign key (empresa_id) references empresa(id) ON DELETE CASCADE,
        foreign key (servico_id) references servico(id) ON DELETE CASCADE
    )"""

    cursor.execute(query)

    query = """ 
    CREATE TABLE atividade (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        codigo varchar(45),
        descricao varchar(150),
        principal boolean,
        empresa_id INTEGER,
        foreign key (empresa_id) references empresa(id) ON DELETE CASCADE
    )"""

    cursor.execute(query)
    

    conn.commit()
    conn.close()

class EmpresaCrud:
    def add(params): 
        conn = sqlite3.connect('empresas.db')  

        query = ("INSERT INTO empresa ( nome, cnpj, telefone, email, uf) "
                "VALUES (:nome, :cnpj, :telefone, :email, :uf)")

        conn.execute(query, params)
        conn.commit()
        cursor = conn.execute("SELECT * from empresa where cnpj = '{}'".format(params['cnpj']))

        empresa_criada = cursor.fetchone()

        conn.close()
        print(empresa_criada)
        return empresa_criada


    def listar():
        conn = sqlite3.connect('empresas.db')  

        cursor = conn.cursor()
        cursor = conn.execute("SELECT * from empresa")
        for i in cursor.fetchall():
            print(i) 
        conn.close()     
    
    def deletar(id):

        conn = sqlite3.connect('empresas.db') 

        query = ('delete from empresa where id = :id')
        params = {'id': id} 

        conn.execute(query, params) 
        conn.commit() 
        conn.close()

class ServicoCrud:
    
    def listar():
        conn = sqlite3.connect('empresas.db')  

        cursor = conn.cursor()
        cursor = conn.execute("SELECT * from servico")
        print(cursor.fetchall())
        conn.close()  
    def add(params):
        conn = sqlite3.connect('empresas.db')  

        query = ("INSERT INTO servico (id, nome, empresa_id) ",
                "VALUES (null, :nome, empresa_id)")
        conn.execute(query, params) 
        conn.commit()
        conn.close()

class ServicoPrestadoCrud:
    def add(params):
        conn = sqlite3.connect('empresas.db')  
        
        query = ("INSERT INTO servico_prestado (id, empresa_id, servico_id) ",
                 "values (null, :empresa_id, :servico_id)")

        conn.execute(query, params) 
        conn.commit()
        cursor = conn.execute("SELECT * from empresa where cnpj = {}".format(params['cnpj']))
        print(cursor.fetchone())
        conn.close()

        return cursor.fetchone()

    def listar():
        conn = sqlite3.connect('empresas.db')  

        cursor = conn.cursor()
        cursor = conn.execute("SELECT * from servico_prestado")
        print(cursor.fetchall())
        conn.close() 
    def deletar(id):
        conn = sqlite3.connect('empresas.db') 

        query = ('delete from empresa where id = :id')
        params = {'id': id} 

        conn.execute(query, params) 
        conn.commit() 
        conn.close()

class AtividadeCrud:
    def add(params):
        conn = sqlite3.connect('empresas.db')  

        query = ("INSERT INTO atividade (id, codigo, descricao, principal) ",
                 "VALUES (null, :codigo, :descricao, :principal)")

        conn.execute(query, params) 
        conn.commit()
        conn.close()

    def listar(empresa_id):
        conn = sqlite3.connect('empresas.db')  
        cursor = conn.execute("SELECT * from atividade where empresa_id = '{}'".format(empresa_id))
        print(cursor.fetchall())
        conn.close() 

    def deletar(id):
        conn = sqlite3.connect('empresas.db') 

        query = ('delete from empresa where id = :id')
        params = {'id': id} 

        conn.execute(query, params) 
        conn.commit() 
        conn.close()