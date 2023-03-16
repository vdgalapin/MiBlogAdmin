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

# For upload file
from werkzeug.utils import secure_filename

# For date time
from datetime import date

# File path for images
UPLOAD_FOLDER = '/static/images'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)
app.config['SECRET_KEY'] = 'AJqWZcd8YB'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):     
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS        

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

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/create', methods=['POST', 'GET'])
def create():
    if request.method == 'POST':
        category = request.form['Category']
        title = request.form['Title']
        content = request.form['content']
        today = date.today()
        # Textual month, day and year	
        date_written = today.strftime("%B %d, %Y")

        insert = True
        if category == "" or title == "" or content == "":
            flash("Please fill all input!")
            insert = False
 

        # checks if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            insert = False
        
        file = request.files['file']
     
        # if user does not select file
        if file.filename == '':
            flash('No selected file')
            insert = False

        # Gets if the file extension is allowed
        if file and allowed_file(file.filename):

            #  Gets the secure filename
            filename = secure_filename(file.filename)

            # Check if file already exist
            if os.path.exists(os.path.join(app.root_path, 'static', 'images', filename)):
                flash(filename + ' already exist. Please, rename the file.')
                insert = False
            
        if insert:
            # creates directory
            os.makedirs(os.path.join(app.root_path, 'static', 'images'), exist_ok=True)
            
            # when saving the file
            file.save(os.path.join(app.root_path, 'static', 'images', filename))

            conn = get_db_connection()
            conn.execute('INSERT INTO articles (category, title, short, images, date_written) VALUES (?, ?, ?, ?, ?)',
                            (category, title, content, filename, date_written))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))

    return render_template('create.html')


                               
@app.route('/<int:id>/edit', methods=['POST', 'GET'])
def edit(id):

    post = get_post(id)
    
    if request.method == 'POST':
        if request.form['action'] == 'delete':

            filename = post['images']

            if os.path.exists(os.path.join(app.root_path, 'static', 'images', filename)):
                  os.remove(os.path.join(app.root_path, 'static', 'images', filename))

            conn = get_db_connection()
            conn.execute('DELETE FROM articles WHERE id = ?', (id,))

            conn.commit()
            conn.close()
            
            flash('"{}" was successfully deleted!'.format(post['title']))
            
            return redirect(url_for('index'))
        
        elif request.form['action'] == 'submit':    
            category = request.form['category']
            title = request.form['title']
            short = request.form['short']
            images = request.form['images']

            insert = True
            if category == "" or title == "" or short == "":
                flash("Please fill all input!")
                insert = False
    
                # checks if the post request has the file part
            if 'file' not in request.files:
                flash('No file part')
                insert = False
            
            file = request.files['file']

            # if user does not select file
            if file.filename == '' and images == "`":
                flash('No selected file')
                insert = False

            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)

                # Check if the filename already exist                         
                if os.path.exists(os.path.join(app.root_path, 'static', 'images', filename)):
                    flash(filename + ' already exist. Please, rename the file.')
                    insert = False 

            if insert:

                # Creates the file directory
                os.makedirs(os.path.join(app.root_path, 'static', 'images'), exist_ok=True)

                # when saving the file
                file.save(os.path.join(app.root_path, 'static', 'images', filename))

                conn = get_db_connection()

                conn.execute('UPDATE articles SET category = ?, title = ?, short = ?, images = ?'
                            'WHERE id = ?' ,
                            (category, title, short, filename, id))

                conn.commit()
                conn.close()

                return redirect(url_for('index'))
        else:

            flash('Unsupported action!')

    return render_template('edit.html', post = post)



@app.route('/')
def index():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM articles').fetchall()
    conn.close()
    return render_template('index.html', posts=posts)