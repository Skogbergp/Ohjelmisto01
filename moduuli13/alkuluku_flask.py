from flask import Flask, request
import json
app = Flask(__name__)
@app.route("/alkuluku/<luku>")
def primeNumber(luku):
    try:
        luku = int(luku)
        is_prime = True
        for i in range(2,int(luku**0.5)+1):
            if luku % i == 0:
                is_prime = False

        result = {
            "number" : luku,
            "isPrime" : is_prime
        }

    except ValueError:
        tilakoodi = 400

        result = {
            "status" : tilakoodi,
            "message" : "Incorrect input"
        }

    result = json.dumps(result)
    return result

if __name__  == "__main__":
    app.run(use_reloader=True,host="127.0.0.1",port=3000)

