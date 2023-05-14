from flask import Flask
app = Flask(__name__)

if __name__ == "__main__":
    app.run(debug=True)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route("/bye")
def say_bye():
    return "Bye!"

@app.route("/user/<username>")
def greet(name):
    return f"Hello, {name}!"


# import time
# print(current_time)

# def speed_calc_decorator(function):
#     def wrapper():
#         current_time = time.time()
#         function()
#         new_time = time.time()
#         completion_time = new_time - current_time
#         print(completion_time)
#     return wrapper

# @speed_calc_decorator
# def fast_function():
#     for i in range(10000000):
#         i * i

# @speed_calc_decorator
# def slow_function():
#     for i in range(100000000):
#         i * i

# fast_function()
# slow_function()
