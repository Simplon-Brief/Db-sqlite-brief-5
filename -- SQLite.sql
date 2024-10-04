-- SQLite
CREATE TABLE Clients (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nom VARCHAR(155),
    prenom VARCHAR(155),
    email TEXT,
    date DATETIME
);
