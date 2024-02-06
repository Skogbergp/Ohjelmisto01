import mysql.connector

def sqlMaakoodit(country_code):
    sql = f"SELECT TYPE,COUNT(*) FROM airport WHERE iso_country = '{country_code}' GROUP BY type order by COUNT(*) DESC"
    print(sql)
    cursor = mydb.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    print(cursor)
    if cursor.rowcount != 0:
        return rows

mydb = mysql.connector.connect(
    host="localhost",
    port = 3306,
    user="root",
    password="root",
    database="lento_peli",
    autocommit=True
)

user_input = input("Syötä maakoodi: ")
airports = sqlMaakoodit(user_input)
if airports != None:
    for airport in airports:
        print(f"{airport[0]}: {airport[1]}")
else:
    print("Lentokenttiä ei löytynyt")