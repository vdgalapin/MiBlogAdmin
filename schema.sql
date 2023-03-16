-- DROP TABLE IF EXISTS articles;

-- CREATE TABLE articles (
--     id INTEGER PRIMARY KEY AUTOINCREMENT,
--     created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
--     category TEXT NOT NULL,
--     title TEXT NOT NULL,
--     short TEXT NOT NULL,
--     images TEXT NOT NULL,
--     date_written TEXT NOT NULL
-- );

-- DROP TABLE IF EXISTS paragraphs;
-- CREATE TABLE paragraphs (
--     paragraph_id INTEGER,
--     created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
--     content TEXT NOT NULL,
--     article_id INT NOT NULL,
--     FOREIGN KEY (article_id) REFERENCES articles(id)
-- );

-- CREATE TABLE images (
--     image_id INTEGER,
--     created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
--     image_name TEXT NOT NULL,
--     article_id INT NOT NULL,
--     FOREIGN KEY (article_id) REFERENCES articles(id)
-- );