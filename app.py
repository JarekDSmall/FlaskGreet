from flask import Flask

app = Flask(__name__)

# Route for /welcome
@app.route("/welcome")
def welcome():
    return "welcome"

# Route for /welcome/home
@app.route("/welcome/home")
def welcome_home():
    return "welcome home"

# Route for /welcome/back
@app.route("/welcome/back")
def welcome_back():
    return "welcome back"

if __name__ == "__main__":
    app.run(debug=True)
