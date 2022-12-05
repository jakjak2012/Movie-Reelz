from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.movie_model import Movie
from flask_app.models.user_model import User



@app.route('/dashboard')
def display_movies():
    movies = Movie.get_movies()

    return render_template('dashboard.html', movies = movies)


@app.route('/add_favorite/<int>')
def add_favorite(int):
    
    if 'uid' not in session: 
        redirect('/dashboard')

    data = {
        'user_id': session["uid"],
        'movie_id': int 
    }
    Movie.add_favorite(data)
    return redirect('/dashboard')
