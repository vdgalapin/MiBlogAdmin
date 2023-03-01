import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort
from datetime import date

app = Flask(__name__)
app.config['SECRET_KEY'] = 'AJqWZcd8YB'
app.config["DEBUG"] = True

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

def get_post(post_id):
    conn = get_db_connection()
    post = conn.execute('SELECT * FROM articles WHERE id = ?',
                        (post_id,)).fetchone()
    conn.close()

    if post is None:
        abort(404)
    return post

@app.route('/<int:post_id>')
def post(post_id):
    post = get_post(post_id)
    return render_template('post.html', post=post)


@app.route('/create', methods=['POST', 'GET'])
def create():
    if request.method == 'POST':
        category = request.form['Category']
        title = request.form['Title']
        short = request.form['content']
        images = 'random'

        today = date.today()
        # Textual month, day and year	
        date_written = today.strftime("%B %d, %Y")

        insert = True
        if category == "" or title == "" or short == "":
            flash("Please fill all input!")
            insert == False
 
        if insert:
            conn = get_db_connection()
            conn.execute('INSERT INTO articles (category, title, short, images, date_written) VALUES (?, ?, ?, ?, ?)',
                            (category, title, short, images, date_written))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))

    return render_template('create.html')

@app.route('/<int:id>/edit', methods=['POST', 'GET'])
def edit(id):
    post = get_post(id)

    if request.method == 'POST':
        category = request.form['category']
        title = request.form['title']
        short = request.form['short']
        images = 'random'


        insert = True
        if category == "" or title == "" or short == "":
            flash("Please fill all input!")
            insert == False

        if insert:
            conn = get_db_connection()
            conn.execute('UPDATE articles SET category = ?, title = ?, short = ?, images = ?'
                         'WHERE id = ?' ,
                        (category, title, short, images, id))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))

    return render_template('edit.html', post = post)

@app.route('/')
def index():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM articles').fetchall()
    conn.close()
    return render_template('index.html', posts=posts)