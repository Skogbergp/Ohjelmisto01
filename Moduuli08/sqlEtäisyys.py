import geopy
import mysql.connector
from geopy.distance import geodesic

db = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="root",
    database="lento_peli",
    autocommit=True
)


def haeTiedot(ICAO):
    sql = f"SELECT latitude_deg, longitude_deg FROM airport WHERE ident = '{ICAO}'"
    cursor = db.cursor()
    cursor.execute(sql)
    return cursor.fetchall()


first_location = haeTiedot(input("Syötä ICAO-koodi\n"))
second_location = haeTiedot(input("Syötä ICAO-koodi\n"))

distance = geodesic(first_location, second_location)
print(f"{distance.kilometers:.2f} km")
