import mysql.connector

# Conectar Banco de Dados
mydb = mysql.connector.connect (
    host = "localhost",
    user = "root",
    password = "1234567"
)
mycursor = mydb.cursor()

# Criar Banco de Dados
mycursor.execute("CREATE DATABASE PythonCRUD")

mycursor.execute("SHOW DATABASES")

for i in mycursor:
    print(i)

