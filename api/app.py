from dog import *
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    url = randomImage() 
    return render_template("home.html", url = url)

if __name__ == "__main__":
    app.run(debug=True)