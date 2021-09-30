CREATE TABLE fragrances(
    fragrance_id serial PRIMARY KEY,
    name VARCHAR(150),
    description VARCHAR(1024),
    cost NUMERIC,
    forbidden BOOLEAN default 'f'
)