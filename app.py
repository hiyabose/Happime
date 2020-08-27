from flask import Flask, request, url_for, redirect, render_template
import pickle
import numpy as np

app = Flask(__name__, template_folder="template")

reg = pickle.load(open("model.pkl", "rb"))


@app.route("/")
def hello_world():
     return render_template("hel.html")


@app.route("/predict", methods=["POST"])
def home():
   
    data2 = float(request.form["b"])
    data3 = float(request.form["c"])
    data4 = float(request.form["d"])
    d5 = float(request.form["e"])
   
   

    arr = np.array(
        [
            [
                
                data2,
                data3,
                data4,
                d5
                            ]
        ]
    )
    pred = reg.predict(arr)
    print(pred)
    return render_template("index.html", data=pred)


if __name__ == "__main__":
    app.run(debug=True)
