import mysql.connector

mydb = mysql.connector.connect(
    host="relational.fit.cvut.cz",
    user="guest",
    password="relational",
    database="northwind"
)

mycursor = mydb.cursor()

j = True

while j == True:

    mycursor.execute("SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE = 'BASE TABLE' AND TABLE_SCHEMA='northwind'")

    myresult = mycursor.fetchall()

    i = 1
    for registro in myresult:   
        print(i ,"-"  , registro[0])
        i = i + 1

    print("Escolha uma tabela")
    t = input() #tabela
    f = 1

    for registro in myresult:
        if t == str(f):
            t = registro[0]
            break
        f = f + 1

    mycursor.execute(f"SELECT column_name FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = '{t}' and table_schema = 'northwind'")

    myresult = mycursor.fetchall()

    i = 1
    for registro in myresult:
        print(i, "-" , registro[0])
        i = i + 1

    print("Escolha uma coluna que deseja pesquisar.")
    c = input() #coluna
    f = 1

    for registro in myresult:
        if c == str(f):
            c = registro[0]
            break
        f = f + 1

    print("favor informe se é numero ou palavra.")
    o = input() #opção

    if o == "numero":
        print("Digite sua pesquisa:")
        pes = input() #pesquisa
        mycursor.execute(f"SELECT * FROM `{t}` where `{c}` = '{pes}'")

        myresult = mycursor.fetchall()

        for registro in myresult:
            print(registro)
    else:
        print("Digite sua pesquisa")
        pes = input()
        mycursor.execute(f"SELECT * FROM `{t}` where `{c}` like '%{pes}%'")

        myresult = mycursor.fetchall()

        for registro in myresult:
            print(registro)