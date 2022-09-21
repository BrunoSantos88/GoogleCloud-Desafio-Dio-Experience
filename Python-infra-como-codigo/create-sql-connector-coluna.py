# importing required libraries
import mysql.connector
 
mydb = mysql.connector.connect(
      host="endpoind=rds",
      user="phpserver",
      passwd="senha",
      database="meubanco"

)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE Dados (AlunoID int,Nome VARCHAR(50), Sobrenome varchar(50),Endereco varchar(150),Cidade varchar(50),Host varchar(50))")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)