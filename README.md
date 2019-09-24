# Penn Labs Server Challenge
Remember to **document your work** in this `README.md` file! Feel free to delete these installation instructions in your fork of this repository.

##Web Scraper
In `scraper.py`, I used BeautifulSoup to scrap club information from https://ocwp.pennlabs.org and create a `Club` object 
to store information for each club. I added a method `get_all_club_object()` that returns a list of club objects to be used in `index.py`

##Club Object
1.Fields
* `club_name`: name of a club 
* `club_tags`: a list of tags of a club
* `club_description`: description of a club
* `fav_count`: a list that stores all the users who have liked the club. The size of the list if the number of users who have liked the club

2.Methods
* `add_club_tag(club_tag)`: add tags to a club object
* `jsonify`: return a json file of the club information
* `like(user)`: add a user who has liked the club to the `fav_count` list

##User Object
1.Fields
* `email`: user's email 
* `username`: user's username, used to log in
* `password_hash`: hash of the password
* `fav_clubs`: a list that stores all the clubs a user has liked

2.Methods
* `add_fav_club`: when a user has liked a club, add the club to the user's favorite club list
* `validate_login`: validate the password for a user

##Flask APP
1. Data Storage: I used a list to store all the clubs that are gained through web scraper or the clubs that are added through `/api/clubs`. 
I used a dictionary to store the users with username as key in order to allow faster lookup.

2. `/api/clubs`: If the request is GET, it will return the list of clubs in JSON format. If the request is POST, it will create a new club
according to the information in the request and add the club to the data storage. 

3. `/api/user/<username>`: It will retrieve the username specified in the URL and look up the user in the database.If the user 
exists, it will return the user's username and a list of clubs that the user has liked. If the user doesn't exist, it will return "This user doesn't exist!"

4. `/api/user/favoriate`: It allows a user specified in the request to favorite a club. After the request, the user will be added to a club's `fav_count` 
list if the user hasn't liked the club before. Similarly, the club will be added to the user's `fav_club` list.

##Additional Functions
1. Penn Clubs Dashboard: I created a front end with Bootstrap and HTML to display all the information of clubs in our database. The data is passed from `/api/clubs` to front end by using AJAX. 
The route for the dashboard is `/dashboard`.

1. Login: The route for login is `/login`. It passes a Flaskform to the frontend which allows users to type in their username and password.
If the user is not in the database, the web will return "This user doesn't exit! Please register first!". If the username and password are both correct,
the web will return "You've successfully logged in!". If either the username or the password is incorrect,
the web will return "Username or password is incorrect".
`Example user: Jennifer - username: jen password: pennlabs2019!`

2. Register: The route for register is `/register`. It passes a Flaskform to the frontend which allows users to type in their username, email and password. The web will create a new User object and store in 
the database after the user successfulLy registered. The user will be redirected to the login page after they finish registering.




