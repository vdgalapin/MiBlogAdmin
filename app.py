# Allows us to run a command in the python script
import os

# SQL
import sqlite3
# Flask
# render_template - post the page
# request - Gets form field values
# url_for - link page name
# flash - for error messages
# redirect - loads to another link page
from flask import Flask, render_template, request, url_for, flash, redirect, send_from_directory

# No Page Found
from werkzeug.exceptions import abort

app = Flask(__name__)


############################################################################################
# START FUNCTIONS
############################################################################################


def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

def get_post(post_id):
    
    conn = get_db_connection()
    post = conn.execute('SELECT * FROM articles WHERE id = ?',
                        (post_id,)).fetchone()
    contents  = conn.execute("SELECT id, paragraph,  IIF(ac.image != '', ac.image, 'NONE') image, IIF(ac.image_2 != '', ac.image_2, 'NONE') image_2, IIF(ac.image_3 != '', ac.image_3, 'NONE') image_3, how_many_images,  IIF(image_width != '', image_width, '0') image_width, IIF(image_height != '', image_height, '0')  image_height, image_row_span, paragraph_column_span, IIF(image_side != '', image_side, 'R')  image_side  FROM articleContents ac LEFT  JOIN image im ON ac.image = im.image WHERE articleID = ?",
                        (post_id,)).fetchall()
    conn.close()

    if post is None:
        abort(404)
    return post, contents

############################################################################################
# END FUNCTIONS
############################################################################################

############################################################################################
# START ROUTES 
############################################################################################
@app.route('/<int:post_id>')
# @login_required
def post(post_id):
    post, contents = get_post(post_id)
    return render_template('post.html', post=post, contents=contents)

@app.route('/')
# @login_required
def index():
        conn = get_db_connection()
        posts = conn.execute('SELECT * FROM articles').fetchall()
        conn.close()
        return render_template('index.html', posts=posts)


############################################################################################
# END ROUTES
############################################################################################