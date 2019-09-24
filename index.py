from flask import Flask, request, flash, jsonify, render_template, redirect
from scraper import * # Web Scraping utility functions for Online Clubs with Penn.\
from flask_wtf import FlaskForm
from wtforms import FloatField, SubmitField, StringField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError
from User import User
app = Flask(__name__)
app.secret_key = "lucy"

#Variables to store clubs and users
club_list = [] #Assign the club information from scraper
for club in get_all_club_object():
    club_list.append(club)
users = {}

#Create a new User Jan
jen = User(username= "jen", email= "jen@upenn.edu", password= "pennlabs2019!")
jen.add_fav_club("PennLabs")
users['jen'] = jen

@app.route('/')
def main():
    return "Welcome to Penn Club Review!"

@app.route('/api')
def api():
    return "Welcome to the Penn Club Review API!."

@app.route('/api/clubs', methods=['post', 'get'])
def clubs():
    if request.method == "POST":
        #Create a new club object according to information in the request
        club_name = request.form['clubname']
        club_description = request.form['clubdescription']
        club_tags = request.form['clubtags'].split(",")
        new_club = Club(club_name = club_name, club_description = club_description)
        for tag in club_tags:
            new_club.add_club_tag(tag)
        clubs.append(new_club)
    elif request.method == "GET":
        result = []
        for c in club_list:
            result.append(c.jsonify())
        return jsonify(result)

@app.route('/api/user/<username>', methods = ['GET'])
def profile(username):
    user = users.get(username)
    if user is None:
        return "This user doesn't exist!"
    else:
        fav_club = ""
        for club in user.fav_clubs:
            fav_club = fav_club + club
        return "The user name is " + username +".\n" + "He/She likes " + fav_club

@app.route('/api/favorite', methods = ['POST'])
def like():
    club_name = request.form['clubname']
    user = request.form['user']
    if users.get(user) is not None:
        for club in club_list:
            if club.club_name == club_name:
                club.like(user)
                user.add_fav_club(club)

@app.route('/dashboard')
def dash():
    return render_template("dashboard.html")

class Login(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    password = StringField('password', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired()])

@app.route('/login',methods=['GET','POST'])
def login():
    form = Login(request.form)

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = users.get(username)
        if user is None:
            return "This user doesn't exit! Please register first!"
        else:
            if (user.validate_login(user.password_hash, password)):
                flash("You've successfully logged in!")
                return redirect("/dashboard")
            else:
                flash("Username or password is incorrect")
                return render_template("login.html", form=form)

    else:
        return render_template("login.html", form = form)


@app.route('/register',methods=['POST', 'GET'])
def register():
    form = Login(request.form)

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        new_user = User(username= username, email= email, password= password)
        users[username] = new_user
        if (new_user is not None):
            flash("You've successfully registered!")
        return render_template('register.html', form = form)

    else:
        return render_template('register.html', form = form)

if __name__ == '__main__':
    app.run()
