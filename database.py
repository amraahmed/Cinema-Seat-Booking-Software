import sqlite3
class Database():
    def __init__(self):
        self.conn = sqlite3.connect('cinema.db')
        self.cursor = self.conn.cursor()
            
    def get_generes(self):
        generes_query = 'SELECT distinct(category) FROM movies'
        self.cursor.execute(generes_query)
        self.conn.commit()
        results = self.cursor.fetchall()
        generes = [i[0] for i in results]
        return (generes)
        
    def get_movies(self):
        movies_query = 'SELECT name FROM movies'
        self.cursor.execute(movies_query)
        self.conn.commit()
        results = self.cursor.fetchall()
        allmovies = [i[0] for i in results]
        return allmovies
        
        
    def get_movie(self,genre):
        movies_query = 'SELECT name FROM movies WHERE category = ? '
        self.cursor.execute(movies_query,(genre,))
        self.conn.commit()
        results = self.cursor.fetchall()
        movies = [i[0] for i in results]
        return movies