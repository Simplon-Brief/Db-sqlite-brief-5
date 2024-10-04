import sqlite3

# Initialisation de la connexion à la base de données
conn = sqlite3.connect('db.sqlite')

# Création du curseur à partir de la connexion
c = conn.cursor()

# Liste de plusieurs clients à insérer
Clients = [
    ('Culcédupoulet', 'Edmond', 'fandekangoodu54@gmail.com'),
    ('Peuplu', 'Jean', 'auboutdurouleau@gmail.com'),
    ('Pacesoir', 'Zinedine', 'materazzisucks@gmail.com')
]

# Insertion de plusieurs clients à la fois
c.executemany("""
INSERT INTO Clients (nom, prenom, email) 
VALUES (?, ?, ?)
""", Clients)

# Valider les changements dans la base de données
conn.commit()

# Fermer la connexion à la base de données
conn.close()

print("Clients ajoutés avec succès !")
