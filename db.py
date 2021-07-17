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
        id INT PRIMARY KEY,
        nome varchar(100) NOT NULL,   
        cnpj varchar(14) unique,
        telefone varchar(11),
        email varchar(100),
        uf varchar(2)
    )"""

    cursor.execute(query)

    query = """ 
    CREATE TABLE servico(
        id INT PRIMARY KEY,
        nome varchar(100) NOT NULL,
        empresa_id INT,
        foreign key (empresa_id) references empresa(id) ON DELETE CASCADE  
    )"""

    cursor.execute(query)

    query = """ 
    CREATE TABLE servico_prestado(
        id INT PRIMARY KEY,
        empresa_id INT,
        servico_id INT,
        foreign key (empresa_id) references empresa(id) ON DELETE CASCADE,
        foreign key (servico_id) references servico(id) ON DELETE CASCADE
    )"""

    cursor.execute(query)

    query = """ 
    CREATE TABLE atividade (
        id INT PRIMARY KEY,
        codigo varchar(45),
        descricao varchar(150),
        principal boolean,
        empresa_id INT,
        foreign key (empresa_id) references empresa(id) ON DELETE CASCADE
    )"""

    cursor.execute(query)
    

    conn.commit()
    conn.close()

class EmpresaCrud:
    def add(params): 
        conn = sqlite3.connect('empresas.db')  

        query = ("INSERT INTO empresa (nome, cnpj, telefone, email, uf) "
                "VALUES (:nome, :cnpj, :telefone, :email, :uf)")

        conn.execute(query, params)
        conn.commit()
        conn.close()

    def listar():
        conn = sqlite3.connect('empresas.db')  

        cursor = conn.cursor()
        cursor = conn.execute("SELECT * from empresa")
        print(cursor.fetchall())
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

    def listar():
        conn = sqlite3.connect('empresas.db')  
        cursor = conn.cursor()
        cursor = conn.execute("SELECT * from atividade")
        print(cursor.fetchall())
        conn.close() 

    def deletar(id):
        conn = sqlite3.connect('empresas.db') 

        query = ('delete from empresa where id = :id')
        params = {'id': id} 

        conn.execute(query, params) 
        conn.commit() 
        conn.close()