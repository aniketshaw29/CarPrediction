#a flask python application for frontend display of car price prediction model
from flask import Flask, request, render_template
import pickle

# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)

#to retrive pickled data
model = pickle.load(open("car_price_prediction_model.pickle", "rb")) #rb stands for read-binary mode

# The route() function of the Flask class is a decorator,
# which tells the application which URL should call the associated function.
@app.route('/') # ‘/’ URL is bound with landingPage() function.
def landingPage():
    return render_template("index.html")


@app.route('/predictionResult') 
def predictionResul():
    return render_template("index.html")

#main
if __name__ == "__main__":
    #run method of flask class run the application 
    app.run(debug = True, port=6969) #on local development server 
else:
    pass

