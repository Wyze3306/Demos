# DEMOS — prototype de vote citoyen décentralisé (blockchain)

**DEMOS** est un prototype NSI qui simule un système de vote en ligne :
- identification via **scan NFC** (démo)
- enregistrement des votes dans une **blockchain** (chaîne de blocs)
- consultation et votes via une **interface web**

Ce projet est une **démonstration pédagogique** (Trophées NSI) : il ne prétend pas être un système électoral officiel.

## Idée principale

- **Créer une clé utilisateur** : une clé est générée côté serveur (démo).
- **Créer un sondage / scrutin** : interface `admin.html`.
- **Voter** : page `vote.html` (saisie d’une clé ou pré-remplissage via URL).
- **Scanner NFC (démo)** : `scan.html` lit une donnée NFC (Web NFC) et redirige avec un paramètre `user`.
- **Blockchain consultable** : route `/chain`.
- **Minage automatique** : un thread mine régulièrement un bloc si des votes sont en attente.

## Architecture du projet

- **Serveur** : `sources/Server/main.py`
  - mini-API HTTP
  - stockage en JSON (`users.json`, `polls.json`, `chain.json`)
- **Site web** : `sources/Site Web/`
  - `index.html` (accueil)
  - `vote.html` (voter)
  - `scan.html` (scan NFC)
  - `admin.html` (créer un sondage)

## Lancer la démo

### Prérequis

- Python 3
- Facultatif : Un navigateur récent pour `scan.html`, un smartphone compatible NFC + navigateur compatible Web NFC

### Démarrage du serveur

Exécuter :

```bash
python sources/Server/main.py
```

Le serveur démarre sur `http://localhost:8000`.

### Ouvrir le site

Ouvrir `sources/Site Web/index.html` dans un navigateur.

## API (principales routes)

- **GET** `/get_polls` : liste des scrutins
- **POST** `/add_poll` : créer un scrutin
- **POST** `/add_vote` : voter
- **GET** `/chain` : récupérer la blockchain
- **GET** `/is_valid` : vérifier l’intégrité
- **GET** `/create_user` : générer une clé (démo)

## Usage de l'IA et Sources

L'agent Claude a été utilisé pour redesigner le site web et corriger de nombreuses fautes d'orthographe.
De plus, l'outil "Création d'Image" de ChatGPT a été utilisée pour générer le logo du projet et le recto/verso de notre carte physique.

Pour le code python de la blockchain, nous nous sommes basés sur ce tutoriel : https://medium.com/jungletronics/building-a-simple-blockchain-with-python-and-flask-a95da7b5b713



