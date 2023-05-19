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
    return "<h1>Guess a number between 0 and 9: </h1>\
        <input type=text inputmode=numeric>\
            <input type=submit value=Submit>\
            <br>\
        <img src=/static/fleventy-five.gif>"

@app.route("/test-form")
def form():
    return render_template("index.html")


@app.route("/submit", methods=["POST"])
def submit():
    input_value = request.form["input_field"]
    return redirect("/result/" + input_value)

@app.route("/result/<input_value>")
def result(input_value):
    return f"You typed {input_value}"
