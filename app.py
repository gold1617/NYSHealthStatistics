from flask import Flask
from flask import jsonify
from flask import render_template
from collections import OrderedDict
import csv

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

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
    
    keyorder = ['County','Percentage of Adults Binge Drinking','Percentage of Obese Students','Percentage of Adults who smoke','Percentage of Obese Adults','Heart Attack Hospitalization per 10000','Unemployment Percentage','Hospitalization for Short-Term complications of Diabetes per 10000']
    
    

    sorted_data = []
    
    for d in data:
        sorted_data.append(OrderedDict(sorted(d.items(), key=lambda i:keyorder.index(i[0]))))

    return jsonify(sorted_data)


if __name__ == "__main__":
    app.run()
