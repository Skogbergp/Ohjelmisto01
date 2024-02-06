import mysql.connector

def sqlMaakoodit(country_code):
    sql = (f"SELECT TYPE,COUNT(*) "
           f"FROM airport WHERE iso_country = '{country_code} '"
           f"GROUP BY type order by COUNT(*) DESC")
    cursor = mydb.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    if cursor.rowcount != 0:
        return rows

mydb = (mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="root",
    database="lento_peli",
    autocommit=True
))

user_input = input("Syötä maakoodi: ")
airports = sqlMaakoodit(user_input)
if airports != None:
    for airport in airports:
        print(f"{airport[0]}: {airport[1]}")
else:
    print("Lentokenttiä ei löytynyt")