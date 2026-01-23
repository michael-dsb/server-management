from flask import Flask, render_template

# Create the Flask application
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

# about page route
@app.route("/about")
def about():
    return render_template("about.html")

# Run the app
if __name__ == "__main__":
    app.run(debug=True)