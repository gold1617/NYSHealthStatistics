from flask import Flask
from flask import jsonify
from flask import render_template
import csv

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/data")
def data():
    f = open("./static/data/Health_Metrics.csv")
    reader = csv.reader(f)
    
    data = []
    keys = []

    for i,line in enumerate(reader):
        cur = {}
        if i==0:
            for item in line:
                keys.append(item)
        else:
            for j,item in enumerate(line):
                cur[keys[j]] = item
            data.append(cur)


    return jsonify(data)


if __name__ == "__main__":
    app.run()
