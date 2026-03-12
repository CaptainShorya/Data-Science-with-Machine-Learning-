from flask import Flask

# Create Flask application
app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome, presenting you my docker container"

# Run the application
if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0", port=5000)