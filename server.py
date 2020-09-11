"""Server for movie ratings app."""

from flask import (Flask, render_template, request, flash, session,
                   redirect)
from model import connect_to_db
import crud
from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined


@app.route("/")
def index():
    """Homepage"""
    return render_template("homepage.html")

@app.route("/", methods = ['POST'])
def check_login():
    """Log into account"""
    email = request.form.get("email")
    password = request.form.get("password")

    user = crud.get_user_by_email(email)

    if user:
        if password == user.password:
            session['key'] = user.user_id
            flash("Logged in!")
        else:
            flash("Wrong password, try again")
    else:
        flash("Account does not exist")
    
    return render_template("homepage.html")

    

@app.route("/movies")
def all_movies():
    movies = crud.get_movies()

    return render_template("all_movies.html", movies = movies)

@app.route("/movies/<movie_id>")
def movie_details(movie_id):
    movie = crud.get_movie_by_id(movie_id)
    
    return render_template("movie_details.html", movie = movie)

@app.route("/users")
def list_users():
    """Shows list of users"""

    users = crud.get_all_users()

    return render_template("all_users.html", users=users)

@app.route("/users/<user_id>")
def show_user_details(user_id):
    user = crud.get_user_by_id(user_id)

    return render_template("user_details.html", user=user)
    
@app.route("/users", methods=['POST'])
def register_user():
    """Create a new user"""
    email = request.form.get('email')
    password = request.form.get('password')

    user = crud.get_user_by_email(email)

    if user:
        flash("Email already exists, create account with different email")
    else:
        crud.create_user(email, password)
        flash("Account successfully created!")

    return redirect("/")




if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)
