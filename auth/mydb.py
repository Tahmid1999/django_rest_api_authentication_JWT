import  mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd =  'qwe123'
)

cursorObject = dataBase.cursor()
cursorObject.execute("CREATE DATABASE django_auth")
print("All Done!")

