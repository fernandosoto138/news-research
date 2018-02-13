CREATE TABLE infb.posts(
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    body TEXT NOT NULL,
    publication_date DATE,
    link_id INT NOT NULL,
    category_id INT NOT NULL,
    author_id INT NOT NULL
);
