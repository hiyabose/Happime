from flask import Flask, request, url_for, redirect, render_template
import pickle
import numpy as np
import requests
import json
import yaml

# put actual path to your project in place of PATH_TO_YOUR_PROJECT
# create an application.yml in the same folder as PATH_TO_YOUR_PROJECT and keep the below key: value pairs
conf = yaml.load(open('/PATH_TO_YOUR_PROJECT/application.yml'), Loader=yaml.SafeLoader)

X_APP_ID = conf['X_APP_ID']
X_REST_KEY = conf['X_REST_KEY']
BASE_URL = conf['BASE_URL']
USERS_ENDPOINT = '/classes/_User'

app = Flask(__name__, template_folder="template")

reg = pickle.load(open("model.pkl", "rb"))


@app.route("/")
def hello_world():
    return render_template("hel.html")


@app.route("/predict", methods=["POST"])
def home():
    data1 = float(request.form["a"])
    data2 = request.form["b"]
    data3 = request.form["c"]
    data4 = request.form["d"]
    d5 = request.form["e"]

    user_body = {"username": data2,
                 "email": data3,
                 "password": data4,
                 "phone": d5,
                 "type": "COUNSELLOR"}

    # create a new user by calling POST API to users endpoint
    user_creation_result = requests.post(BASE_URL + USERS_ENDPOINT,
                                         data=json.dumps(user_body),
                                         headers={"X-Parse-Application-Id": X_APP_ID,
                                                  "X-Parse-REST-API-Key": X_REST_KEY,
                                                  "Content-Type": "application/json"})
    print('Response after user creation: {}'.format(user_creation_result.json()))

    arr = np.array(
        [
            [

                data1,
                data1,
                data1,
                data1
            ]
        ]
    )
    pred = reg.predict(arr)
    print(pred)
    return render_template("index.html", data=pred)


# fetch all users of type:COUNSELLOR
def fetchAllCounsellors():
    counsellors_data = requests.get(BASE_URL + USERS_ENDPOINT + "?where={\"type\":\"COUNSELLOR\"}",
                                    headers={"X-Parse-Application-Id": X_APP_ID,
                                             "X-Parse-REST-API-Key": X_REST_KEY})
    list_of_counsellors = counsellors_data.json().get('results')
    print('Number of users before creation {}'.format(len(list_of_counsellors)))


# fetch all users of type:STUDENT
def fetchAllStudents():
    counsellors_data = requests.get(BASE_URL + USERS_ENDPOINT + "?where={\"type\":\"STUDENT\"}",
                                    headers={"X-Parse-Application-Id": X_APP_ID,
                                             "X-Parse-REST-API-Key": X_REST_KEY})
    list_of_counsellors = counsellors_data.json().get('results')
    print('Number of users before creation {}'.format(len(list_of_counsellors)))


if __name__ == "__main__":
    app.run(debug=True)
