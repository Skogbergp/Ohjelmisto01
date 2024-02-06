import mysql.connector

def sqlMaakoodit(country_code):
    sql = f"SELECT TYPE,COUNT(*) FROM airport where iso_country ='{country_code}' GROUP BY type"
    print(sql)
    cursor = mydb.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    print(cursor)
    return rows


mydb = mysql.connector.connect(
    host="localhost",
    port = 3306,
    user="root",
    password="root",
    database="lento_peli",
    autocommit=True
)
airports = sqlMaakoodit("FI")
for airport in airports:
    print(airport[0],airport[1])