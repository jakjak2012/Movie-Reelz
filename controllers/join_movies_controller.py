from flask_app import app
from flask import render_template, request, redirect, session, flash

from flask_app.models.join_movies_model import Join_Movies


@app.route('/show_favorite')
def show_favorite():

    if 'uid' not in session: 
        redirect('/sign_in')

    data = {
        'id': session['uid']
    }

    favorites = Join_Movies.show_favorite(data)
    return render_template('favorites.html', favorites = favorites)
