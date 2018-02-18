CREATE TABLE infb.links(
    id SERIAL PRIMARY KEY,
    link TEXT UNIQUE,
    is_post SMALLINT NOT NULL,
    date_analyzed TIMESTAMP NOT NULL
);