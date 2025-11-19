-- SQL script to create the database schema for the Dream Dictionary application
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100) UNIQUE NOT NULL,
    password_hash TEXT NOT NULL
);

-- Table to store dream symbols and their meanings
CREATE TABLE symbols (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(id),
    symbol VARCHAR(100),
    personal_meaning TEXT,
    category VARCHAR(50)
);

-- Table to store user dreams
CREATE TABLE dreams (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(id),
    content TEXT,
    date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    mood VARCHAR(20)
);

-- Junction table to map dreams to symbols
CREATE TABLE dream_symbol_mapping (
    dream_id INT REFERENCES dreams(id),
    symbol_id INT REFERENCES symbols(id),
    PRIMARY KEY(dream_id, symbol_id)
);
