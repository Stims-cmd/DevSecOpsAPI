# Étape 1 : choisir une image de base
FROM python:3.9

# Étape 2 : définir le dossier de travail
WORKDIR /test_docker

# Étape 3 : copier les fichiers du projet dans l’image
COPY requirements_qt.txt .
COPY python_pokeapi.py .
COPY html_pokeapi.html .

# Étape 4 : installer les dépendances
RUN pip install -r requirements_qt.txt

# Étape 5 : définir la commande de lancement
EXPOSE 5000
CMD ["python", "python_pokeapi.py"]
