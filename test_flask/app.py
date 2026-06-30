from flask import Flask, render_template

# Initialize the Flask application
app = Flask(__name__)

# Define the home route
@app.route("/")
def home():
    return "Hello, World!"

# Define another route with a simple HTML template
@app.route("/hello/<name>")
def hello(name):
    return render_template("index.html", name=name)

@app.route('/create/')
def create():
    return 'Create'

@app.route('/read/<id>/')
def read(id):
    print(id)
    return 'Read' + id

# Run the Flask app in debug mode
if __name__ == "__main__":
    app.run(debug=True)
