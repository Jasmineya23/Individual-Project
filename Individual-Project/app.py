from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase
config={
  "apiKey": "AIzaSyCEVtXjvM5uiGxEm9ydm3abBKJUC-Gtsow",
  "authDomain": "project-63a79.firebaseapp.com",
  "databaseURL": "https://project-63a79-default-rtdb.europe-west1.firebasedatabase.app",
  "projectId": "project-63a79",
  "storageBucket": "project-63a79.appspot.com",
  "messagingSenderId": "891421806834",
  "appId": "1:891421806834:web:4370e4d7b5e810c7acc06b",
  "measurementId": "G-WWM6DVWB3H"
    }

    
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db = firebase.database()

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'
@app.route('/')
def home():
    return render_template('homep.html')

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    
    error = ""
    if request.method == 'POST':
       email = request.form['email']
       password = request.form['password']
       try:
        login_session['user'] = auth.sign_in_with_email_and_password(email, password)
        return redirect(url_for('home'))
       except:
           error = "Authentication failed"
           return render_template("login.html")
    return render_template("login.html")



@app.route('/signup', methods=['GET', 'POST'])
def signup():
    error = ""
    if request.method == 'POST':
       email = request.form['email']
       password = request.form['password']
       try:
        login_session['user'] = auth.create_user_with_email_and_password(email, password)
        return redirect(url_for('home'))
       except:
        error = "Authentication failed"
        return render_template("signup.html")
    return render_template("signup.html")

@app.route('/signout')
def signout():
    login_session['user'] = None
    auth.current_user = None
    return redirect(url_for('signin'))


@app.route('/add_tweet', methods=['GET', 'POST'])
def add_tweet():
    return render_template("add_tweet.html")


@app.route('/productsp')
def productsp():
    return render_template("productsp.html")


@app.route('/aboutus')
def aboutus():
    return render_template("aboutus.html")



if __name__ == '__main__':
    app.run(debug=True)