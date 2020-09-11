"""CRUD operations."""

from model import db, User, Movie, Rating, connect_to_db
from datetime import datetime

def create_user(email, password):
    """Create and return a new user."""

    user = User(email=email, password=password)

    db.session.add(user)
    db.session.commit()

    return user

def create_movie(title, overview, release_date, poster_path):
    """Create and return a new movie."""

    movie = Movie(title = title, overview = overview, release_date = release_date, poster_path = poster_path)

    db.session.add(movie)
    db.session.commit()

    return movie


def get_movies():
    """Return all movies."""

    return Movie.query.all()

def get_movie_by_id(movie_id):
    """Get movie using movie ID"""
    movie = Movie.query.get(movie_id)

    return movie

def create_rating(score, user, movie):
    """Create and return a rating"""

    rating = Rating(score = score, user = user, movie = movie)
    
    db.session.add(rating)
    db.session.commit()

    return rating

def get_all_users():
    """Create a list of all users."""

    return User.query.all()

def get_user_by_id(user_id):
    """Get user by id"""

    user = User.query.get(user_id)

    return user

def get_user_by_email(email):

    user = User.query.filter(User.email==email).first()

    return user

if __name__ == '__main__':
    from server import app
    connect_to_db(app)