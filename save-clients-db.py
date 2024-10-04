import sqlite3
import csv
import shutil
from datetime import datetime

# Étape 1 : Sauvegarder la base de données
# Spécifier le chemin du fichier de base de données SQLite
db_file = 'db.sqlite'
# Générer un nom de fichier de sauvegarde avec la date
backup_file = f'db_backup_{datetime.now().strftime("%Y%m%d_%H%M%S")}.sqlite'

# Sauvegarder la base de données en copiant le fichier
shutil.copy(db_file, backup_file)
print(f"Sauvegarde de la base de données réalisée sous : {backup_file}")

# Étape 2 : Exporter les données vers un fichier CSV
# Connexion à la base de données
conn = sqlite3.connect(db_file)
c = conn.cursor()

# Requête SQL pour récupérer toutes les données de la table Clients (ou une autre table)
c.execute("SELECT * FROM Clients")
commandes = c.fetchall()

# Nom des colonnes (facultatif, utile pour l'export)
column_names = [description[0] for description in c.description]

# Chemin du fichier CSV
csv_file = 'clients_export.csv'

# Écriture dans un fichier CSV
with open(csv_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    # Écrire les en-têtes de colonnes
    writer.writerow(column_names)
    # Écrire les données
    writer.writerows(commandes)

print(f"Export des données vers le fichier CSV : {csv_file}")

# Fermeture de la connexion à la base de données
conn.close()
