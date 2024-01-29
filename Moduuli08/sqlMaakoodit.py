import mysql.connector

def sqlMaakoodit(maakoodi):
    sql = f"SELECT type FROM airport where iso_country = '{maakoodi}'"
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
airport_types = set()
airports = sqlMaakoodit("FI")
print(airports)
for type in airports:
    airport_types.add(type)
print(airport_types)