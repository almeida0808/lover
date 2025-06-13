from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

start_date = datetime(2020, 8, 17, 0, 0, 0)


@app.route("/")
def home():
    return render_template("index.html", start_date=start_date.isoformat())


if __name__ == "__main__":
    app.run(debug=True)
