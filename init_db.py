import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

# cur.execute("INSERT INTO articles (category, title, short, images, date_written) VALUES (?, ?, ?, ?, ?)",
#             ('Running', 'Endorphin Speed 2', ' Best half marathon shoe in my opinon. It does not have everything, but it has every essential I needed.', 'ES_2.jpg', 'November 28, 2022')
#             )

connection.commit()
connection.close()