import mysql.connector

# Conectar Banco de Dados
mydb = mysql.connector.connect (
    host = "localhost",
    user = "root",
    password = "1234567",
    database = "PythonCRUD"
)
mycursor = mydb.cursor()
'''
# Criar Banco de Dados
mycursor.execute("CREATE DATABASE PythonCRUD")

mycursor.execute("SHOW DATABASES")

for i in mycursor:
    print(i)

# Criar tabela
mycursor.execute("CREATE TABLE users ( \
    id INT AUTO_INCREMENT PRIMARY KEY, \
    name VARCHAR(15), \
    password VARCHAR(15)) \
    ")
# Checando se a tabela existe:
mycursor.execute("SHOW TABLES")
for i in mycursor:
    print(i)
'''
# Criar Consulta
def validation(user, password):

    mycursor.execute("SELECT name, password FROM users")
    myresult = mycursor.fetchall()
    list = []
    for x in myresult:
        list.append(x)

    for i in range(len(list)):
        if list[i][0] == user:
            if list[i][1] == password:
                print('Success')
            else:
                print('Senha incorreta')
        else:
            print("Usuario nao cadastrado")

# Inserindo users no banco:
def insert(new_user, password):
    sql = "INSERT INTO users (name, password) VALUES (%s, %s)"
    val = (new_user, password)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "usuário registrado com sucesso")

