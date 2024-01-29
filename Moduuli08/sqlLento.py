import mysql.connector

conn = mysql.connector.connect(
    host="127.0.0.1",
    port= 3306,
    database="lento_peli",
    user="root",
    password="root",
    autocommit=True
)

def hae_lentokentta(ICAO):
    sql = f"SELECT name,municipality FROM airport WHERE ident = '{ICAO}'"
    print(sql)
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    if cur.rowcount != 0:
        for row in rows:
            print(row)

hae_lentokentta(input("Syötä ICAO-koodi: "))