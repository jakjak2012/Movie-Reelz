from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models.user_model import User
from flask_app.models.movie_model import Movie

class Join_Movies:
    def __init__(self, data):
        self.user_id = data["user_id"]
        self.movie_id = data["movie_id"]

    @classmethod
    def show_favorite(cls, data):
        query = "SELECT * FROM users JOIN join_movies ON users.id = join_movies.user_id JOIN movies ON movies.id = join_movies.movie_id WHERE users.id = %(id)s;"
        results = connectToMySQL('movies_db').query_db(query, data)
        favorites = []
        for f in results:
            user = cls(f)
            user_data = {
                **f, 
                "id": f['id'],
                "created_at": f['created_at'],
                "updated_at": f['updated_at'],
            }
            movie_data = {
                **f,
                "movie_id" : f['movies.id'],
            }
            user.user_info = User(user_data)
            user.movie = Movie(movie_data) 
            favorites.append(user)

        return favorites