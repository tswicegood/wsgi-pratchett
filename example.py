from flask import Flask
from pratchett import GNUTerryPratchett
from werkzeug import run_simple

app = Flask(__name__)


@app.route("/")
def handler():
    return "Hello"


app = GNUTerryPratchett(app)
run_simple('localhost', 5000, app)
