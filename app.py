from flask import Flask, render_template

# create flask app instance
app = Flask(__name__)


# define a home page and set a route to this page
@app.route('/')
def home():
    return render_template('index.html')


# run the app
if __name__ == "__main__":
    app.run()
