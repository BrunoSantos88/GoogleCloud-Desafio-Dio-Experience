# importing required libraries
import mysql.connector
 
dataBase = mysql.connector.connect(
      host="endppont-rds",
      user="phpserver",
      passwd="senha",
      

)
# preparing a cursor object
cursorObject = dataBase.cursor()
 
# creating database
cursorObject.execute('CREATE DATABASE meubanco'
)

print("tabela")