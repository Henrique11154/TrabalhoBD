import mysql.connector

mydb = mysql.connector.connect(
    host="relational.fit.cvut.cz",
    user="guest",
    password="relational",
    database="northwind"
)

mycursor = mydb.cursor()


mycursor.execute("SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE = 'BASE TABLE' AND TABLE_SCHEMA='northwind'")


myresult = mycursor.fetchall()


i = 1
for registro in myresult:   
    print(i ,"-"  , registro[0])
    i = i + 1

print("-----Pesquisa-------")

print("Escolha uma tabela")
tabela = input()


mycursor2 = mydb.cursor()

mycursor2.execute(f"SELECT column_name FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = '{tabela}' and table_schema = 'northwind'")

myresult2 = mycursor2.fetchall()

i = 1
for registro2 in myresult2:
    print(i, "-" , registro2[0])
    i = i + 1


print("Escolha uma coluna que deseja pesquisar.")
coluna = input()
print("favor informe se é numero ou palavra.")
o = input() #opcao

if o == "numero":
    print("Digite sua pesquisa:")
    pes = int(input()) #pesquisa
else:
    print("Digite sua pesquisa:")
    pes = input()

mycursor3 = mydb.cursor()

mycursor3.execute(f"SELECT * FROM {tabela} where {coluna} like '%{pes}%'")

myresult3 = mycursor3.fetchall()

for registro3 in myresult3:
    print(registro3)



