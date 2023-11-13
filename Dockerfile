# Utilisation de l'image de base Python
FROM python:3

# Définition du répertoire de travail dans le conteneur
WORKDIR /app

# Copie des fichiers locaux (actuels) dans le conteneur
COPY . /app

# Installation des dépendances définies dans requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Commande pour exécuter le script Python
CMD ["python", "app.py"]
