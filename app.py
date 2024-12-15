import pandas as pd
import joblib

from flask import Flask , render_template, url_for ,redirect
from forms import Smschecker
app = Flask(__name__)
app.config['SECRET_KEY'] = "secret_key"


#model = joblib.load("sms_detection.pkl")

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html" , title = "Home")

@app.route("/check",methods =['GET','POST'])
def check():
    form = Smschecker()
    if form.validate_on_submit():
        sms_text = form.sms_check.data

        try:
            # Load your pre-trained model and vectorizer
            model = joblib.load('sms_detection2.pkl')
            vectorizer = joblib.load('vectorizer2.pkl')

            # Transform the input text
            x_new = vectorizer.transform([sms_text])

            # Predict the result
            prediction = model.predict(x_new)[0]

            message = f"The SMS is {prediction}"
        except Exception as e:
            message = f"Error during prediction: {e}"
    else:
        message = "Please provide valid input details!"
    return render_template("checker.html" , title = "SMS_Check_Box" ,form = form ,  output = message)

@app.route("/ham")
def ham():
    return render_template("ham.html" , title = "Ham")

@app.route("/spam")
def spam():
    return render_template("spam.html" , title = "Spam")

@app.route("/about")
def about():
    return render_template("about.html" , title = "about" )

@app.route("/predict")
def predict():
    
        
    return redirect(url_for("check") )

if __name__ == "__main__":
    app.run(debug=True)