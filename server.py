from random import randint
from flask import Flask, request, redirect, render_template

app = Flask(__name__)

# Have user enter number between 0 and 9
# Generate random number
# Route to URL that ends with user's number
# If too low, in red text: "Too low. Try again!"
# If too high, in purple text: "Too high. Try again!"
# If correct, in green text: "Correct!"

@app.route("/")
def greeting():
    """This is the homepage on the site that asks for a number."""
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():
    input_value = int(request.form["input_field"])
    number = randint(0, 9)
    if input_value < number:
        return redirect("/result/too-low")
    elif input_value > number:
        return redirect("/result/too-high")
    elif input_value == number:
        return redirect("/result/correct")

@app.route("/result/too-low")
def too_low():
    return "<h1 style=color:red>Too low. Try again!</h1>\
        <img src=/static/its-too-low-egoraptor.gif>\
        <br>\
        <br>\
        <a href=/>Home</a>"

@app.route("/result/too-high")
def too_high():
    return "<h1 style=color:purple>Too high. Try again!</h1>\
        <img src=/static/too-much.gif>\
        <br>\
        <br>\
        <a href=/>Home</a>"

@app.route("/result/correct")
def correct():
    return "<h1 style=color:green>Correct!</h1>\
        <img src=/static/correct.gif>\
        <br>\
        <br>\
        <a href=/>Home</a>"
