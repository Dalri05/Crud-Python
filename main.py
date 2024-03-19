import mysql.connector

conexao = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "123456",
    database = "pessoas"
)
cursor = conexao.cursor()
nome = "joao"
idade = 18
email = "joao,dalri05@gmail.com"


#CREATE
#comando = f'INSERT INTO usuarios (nome, idade, email) VALUES ("{nome}", "{idade}", "{email}")'
#cursor.execute(comando)
#conexao.commit()

#READ
#comando = 'SELECT * FROM usuarios'
#cursor.execute(comando)
#resultado = cursor.fetchall()
#print(resultado)

#UPDATE
#comando = 'UPDATE usuarios SET idade = 12 WHERE email = "joao,dalri05@gmail.com"'
#cursor.execute(comando)
#conexao.commit()

#DELETE
#comando = 'DELETE FROM usuarios WHERE idnome = 3'
#cursor.execute(comando)
#conexao.commit()

cursor.close()
conexao.close