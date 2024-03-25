from flask import Flask, request
import mysql.connector
import json
app = Flask(__name__)
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="lento_peli",
    autocommit=True
)
@app.route('/kenttä/<icao>')
def icao_search(icao):
    try:
        icao = icao.upper()
        sql = f"SELECT ident,name,municipality FROM airport WHERE ident ='{icao}'"
        cur = conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        cur.close()
        if len(rows) == 0:
            result = {
                "message": "No results for" + icao

            }

        else:
            row = rows[0]
            result = {
                "ICAO": row[0],
                "Name": row[1],
                "Municipality":row[2]

            }
    except ValueError:
        tilakoodi = 400
        result = {
            "status": tilakoodi,
            "message": "Invalid input"
        }
    result = json.dumps(result)

    return result

@app.errorhandler(404)
def page_not_found(virhekoodi):
    result = {
        "status" : 404,
        "message": "Page not found"
    }
    result = json.dumps(result)
    return result

if __name__ == '__main__':
    app.run(use_reloader=True,host="127.0.0.1",port=3000)