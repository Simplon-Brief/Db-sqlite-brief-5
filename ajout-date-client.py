import sqlite3
from datetime import datetime

# Connexion à la base de données
conn = sqlite3.connect('db.sqlite')
c = conn.cursor()

# Récupérer la date actuelle
date_actuelle = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

# Mettre à jour les enregistrements existants avec la date d'inscription
c.execute("""
UPDATE Clients
SET date_inscription = ?
""", (date_actuelle,))

# Valider les changements
conn.commit()

# Fermer la connexion
conn.close()

print("Dates d'inscription mises à jour pour tous les clients !")