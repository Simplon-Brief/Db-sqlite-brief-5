import sqlite3
from datetime import datetime

# Connexion à la base de données
conn = sqlite3.connect('db.sqlite')
c = conn.cursor()

# Liste des commandes avec les client_id existants
commandes = [
    (1, 'Pare choc de Kangoo', datetime.now().strftime('%Y-%m-%d %H:%M:%S')),
    (2, '25 mètres de cordes', datetime.now().strftime('%Y-%m-%d %H:%M:%S')),
    (3, 'Implants capillaires', datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
]

# Insérer plusieurs commandes à la fois en utilisant le client_id
c.executemany("""
INSERT INTO Commande (client_id, produit, date_commande) 
VALUES (?, ?, ?)
""", commandes)

# Valider les changements dans la base de données
conn.commit()

# Fermer la connexion
conn.close()

print("Commandes ajoutées avec succès !")