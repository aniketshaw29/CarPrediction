import numpy as np
from flask import Flask, request, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open("LinearRegression.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods = ["POST"])
def predict():
    year = request.form.get('Year')
    present_price = request.form.get('Present Price')
    kms_driven = request.form.get("Kms Driven")
    fuel = request.form.get("Fuel Type")
    seller_type = request.form.get("Seller Type")
    transmission = request.form.get("Transmission")
    owner = request.form.get("Owner")
    prediction = model.predict(year, present_price, kms_driven, fuel, seller_type, transmission, owner)
    return render_template("index.html", prediction_txt = "The price of the car is {}".format(prediction))

if __name__ == "__main__":
    app.run(debug = True)
else:
    pass
