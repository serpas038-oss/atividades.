import mysql.connector
from crud import Crud

conexao = mysql.connector.connect(
    host = '127.0.0.1',
    user = 'root',
    password = 'senac',
    database = 'cadastro',
    port = '3307'
)
cursor = conexao.cursor()

a = Crud()

comando = a.unir()
print(comando)
cursor.execute(comando)

resultado = cursor.fetchall()
for i in resultado:
    print(i)