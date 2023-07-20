from flask import Flask, request
from time import perf_counter

import logging

from index import _index

logging.basicConfig(format="%(asctime)s - %(message)s")

app = Flask(__name__)

@ app.route("/bets/<code>", methods = ["GET"])
def place_bets(code):
    try:
        start = perf_counter()
        _index(code=code)
        finish = perf_counter()
    except:
        _index(code=code)
        return "Fail"
    else:
        print(f"It took {finish-start} seconds(s) to finish")
        return "Success"

if __name__ == "__main__":
    app.run(debug = True)
    print(app)
