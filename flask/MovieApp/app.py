import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect, abort

app = Flask(__name__)
app.config["DEBUG"] = True
app.config['SECRET_KEY'] = 'your secret key'

def get_db_connection():
    conn = sqlite3.connect('movies.db')
    conn.row_factory = sqlite3.Row
    return conn

def get_movie(movie_id):
    conn = get_db_connection()
    movie = conn.execute('SELECT * FROM movies WHERE id = ?', (movie_id,)).fetchone()
    conn.close()
    if movie is None:
        abort(404)
    return movie

@app.route('/', methods=('GET', 'POST'))
def index():
    conn = get_db_connection()
    if request.method == 'POST':
        search_input = request.form.get("search_box")
        if request.form['action'] == 'director_button':
            director = conn.execute('SELECT * FROM movies WHERE director LIKE:search', { "search": '%' + search_input + '%' }).fetchall()
            return render_template('index.html', movies=director)
        elif request.form['action'] == 'search_button':
            rating = conn.execute('SELECT * FROM movies WHERE rating LIKE:search', { "search": '%' + search_input + '%' }).fetchall()
            return render_template('index.html', movies=rating)
        elif request.form['action'] == 'year':
            year = conn.execute('SELECT * FROM movies ORDER BY year DESC').fetchall()
            return render_template('index.html', movies=year)
        elif request.form['action'] == 'runtime':
            runtime = conn.execute('SELECT * FROM movies ORDER BY runtime DESC').fetchall()
            return render_template('index.html', movies=runtime)
        elif request.form['action'] == 'imdb_score':
            imdb_score = conn.execute('SELECT * FROM movies ORDER BY imdb_score DESC').fetchall()
            return render_template('index.html', movies=imdb_score)
    movies = conn.execute('SELECT * FROM movies').fetchall()
    conn.close()
    
    return render_template('index.html', movies=movies)
    

@app.route('/actors')
def actors():
    conn = get_db_connection()
    actors_data = conn.execute('SELECT actors.name, movies.title FROM actors, movies WHERE actors.movie_id = movies.id;').fetchall()
    conn.close()
    return render_template('actors.html', actors=actors, actors_data=actors_data)

@app.route('/<int:id>/delete/', methods=('POST',))
def delete(id):
    movie = get_movie(id)
    conn = get_db_connection()
    conn.execute('DELETE FROM movies WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    flash('"{}" was successfully deleted!'.format(movie['title']))
    return redirect(url_for('index'))

app.run(host="0.0.0.0")