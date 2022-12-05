from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

from flask_app.models.user_model import User

class Movie:
    def __init__(self,data):
        self.id = data["id"]
        self.imdb_id = data["imdb_id"]
        self.title = data["title"]
        self.imdb_rating = data["imdb_rating"]
        self.release_date = data["release_date"]
        self.runtime = data["runtime"]
        self.genre = data["genre"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def get_movies(cls):
        query = "SELECT * FROM movies;"
        results = connectToMySQL('movies_db').query_db(query)
        users = []
        for m in results:
            users.append(cls(m))
        return users
    
    @classmethod
    def add_favorite(cls, data):
        query = "INSERT INTO join_movies (user_id, movie_id) VALUES (%(user_id)s, %(movie_id)s);"
        return connectToMySQL('movies_db').query_db(query, data)

    

