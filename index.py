from flask import Flask, request, jsonify, render_template
from scraper import * # Web Scraping utility functions for Online Clubs with Penn.
from User import User
app = Flask(__name__)

#Variables to store clubs and users
club_list = [] #Assign the club information from scraper
for club in get_all_club_object():
    club_list.append(club)
users = []

#Create a new User Jan
jen = User(username= "jen", email= "jen@upenn.edu", password= "pennlabs2019!")
users.append(jen)

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
    print("The user name is " + username)
    return "The user name is " + username + ".\n" + "He likes xxx clubs"

@app.route('/api/favorite', methods = ['POST'])
def like():
    club_name = request.form['clubname']
    user = request.form['user']
    for club in club_list:
        if club.club_name == club_name:
            club.like(user)

@app.route('/dashboard')
def dash():
    return render_template("dashboard.html")




if __name__ == '__main__':
    app.run()
