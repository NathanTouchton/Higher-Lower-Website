from flask import Flask
app = Flask(__name__)

# Have user enter number between 0 and 9
# Generate random number
# Route to URL that ends with user's number
# If too low, in red text: "Too low. Try again!"
# If too high, in purple text: "Too high. Try again!"
# If correct, in green text: "Correct!"


@app.route("/")
def greeting():
    return "<h1>Guess a number between 0 and 9: </h1>\
        <img src=/static/fleventy-five.gif>"
