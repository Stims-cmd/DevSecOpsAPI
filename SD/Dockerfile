# Image Python officielle légère
FROM python:3.11-alpine

# Dossier de travail
WORKDIR /main

# Copier les dépendances
COPY requirements.txt .

# Installer les librairies Python
RUN pip install --no-cache-dir -r requirements.txt

# Copier le code source
COPY . .

EXPOSE 5000

# Lancer l'API
CMD ["python3", "app.py"]
