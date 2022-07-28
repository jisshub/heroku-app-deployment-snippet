<h2 text-aligin="center">heroku-app-deployment-snippet</h2>


### Create Environment

Create a virtual environment and install dependencies:

```bash
conda create -n myenv python=3.7 Flask
conda activate myenv
```

### Create requirements.txt file

- Add packages to requirements.txt file:

```txt
Flask
gunicorn
Jinja2
Werkzeug
```

### Create App

*app.py*

```py
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
```

### Run the app in command prompt

```bash
python app.py
```

Navigate to the URL: http://localhost:5000/

### Create Procfile in root directory

**Procfile**

```Procfile
web: gunicorn app:app
```

### Push the changes to github

```bash
git add --all
git commit -am "Push All"
git pull && git push
```

### Deploy to Heroku

* Install Heroku CLI and login using heroku login and setup the app in Heroku Web.

```bash
heroku login

```