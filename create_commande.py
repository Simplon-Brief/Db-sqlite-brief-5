import sqlite3

# Initialisation de la connexion à la base de données
conn = sqlite3.connect('db.sqlite')

# Création du curseur à partir de la connexion
c = conn.cursor()

# Activer les clés étrangères
c.execute("PRAGMA foreign_keys = ON")

# Ajout de la table Commande avec une clé étrangère sur Clients.id
c.execute("""
CREATE TABLE IF NOT EXISTS Commande (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    client_id INTEGER,
    produit TEXT,
    date_commande DATETIME,
    FOREIGN KEY (client_id) REFERENCES Clients(id) ON DELETE CASCADE
)
""")

# Fermeture de la connexion à la base de données
conn.close()


