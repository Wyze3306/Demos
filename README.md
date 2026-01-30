# DEMOS — prototype de vote citoyen décentralisé (blockchain)

**DEMOS** est un prototype NSI qui simule un système de vote en ligne :
- identification via **scan NFC** (démo)
- enregistrement des votes dans une **blockchain** (chaîne de blocs)
- consultation et votes via une **interface web**

Ce projet est une **démonstration pédagogique** (Trophées NSI) : il ne prétend pas être un système électoral officiel.

## Pourquoi ce projet ? (constat + chiffres)

- **Coût et lourdeur logistique** : l’organisation des élections mobilise des moyens importants.
  - En 2022, le budget prévu pour l’**organisation des élections** (programme 232 « Vie politique », action 02) atteint **~412,7 M€** (élection présidentielle + législatives + autres scrutins de l’année).
- **Rareté des référendums** : sous la Ve République, seulement **9 référendums** ont été organisés depuis 1958 (hors référendum constitutionnel de 1958).
- **Risque de fraude / manipulation** : même en France, des affaires ont existé.
  - Exemple : *affaire des faux électeurs du 5e arrondissement de Paris* (Jean Tiberi), avec des inscriptions fictives et une condamnation.

L’objectif de DEMOS est de montrer comment la blockchain peut aider à :
- rendre le processus plus **auditable**
- limiter la dépendance à un **seul acteur central**
- simplifier l’accès au vote (sans supprimer les garanties)

## Idée principale

Dans DEMOS :
- un vote est une donnée (`poll`, `user`, `choice`)
- les votes sont regroupés en blocs
- chaque bloc pointe vers le **hash** du précédent
- une modification a posteriori casserait la chaîne (perte d’intégrité)

## Ce que fait la démo (fonctionnalités)

- **Créer une clé utilisateur** : une clé est générée côté serveur (démo).
- **Créer un sondage / scrutin** : interface `admin.html`.
- **Voter** : page `vote.html` (saisie d’une clé ou pré-remplissage via URL).
- **Scanner NFC (démo)** : `scan.html` lit une donnée NFC (Web NFC) et redirige avec un paramètre `user`.
- **Blockchain consultable** : route `/chain`.
- **Minage automatique** : un thread mine régulièrement un bloc si des votes sont en attente.

## Architecture du projet

- **Serveur** : `sources/Server/main.py`
  - mini-API HTTP (module `http.server`)
  - stockage en JSON (`users.json`, `polls.json`, `chain.json`)
- **Site web** : `sources/Site Web/`
  - `index.html` (accueil)
  - `vote.html` (voter)
  - `scan.html` (scan NFC)
  - `admin.html` (créer un sondage)

## Lancer la démo

### Prérequis

- Python 3
- Un navigateur récent
  - pour `scan.html`, un smartphone compatible NFC + navigateur compatible Web NFC

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

## Intégration “République” (idée d’évolution)

DEMOS sert aussi de support pour une proposition :
- remplacer la **carte d’électeur papier** par un identifiant lié à la **carte d’identité / passeport**
- utiliser une authentification NFC côté citoyen (comme dans la démo)
- distribuer la validation des blocs à des organismes **certifiés** (mairies, universités, entreprises sous contrat)

Modèle possible :
- l’État contractualise avec des validateurs (infrastructure + audits)
- une partie du coût logistique (impression / envoi / centralisation) peut être réduite
- la “récompense” n’est pas une crypto-monnaie : c’est une **rémunération contractuelle** pour un service public (validation + disponibilité)

## Limites (important)

Cette version est une **simulation** :
- le stockage est en JSON local (pas de réseau P2P réel)
- l’anonymat cryptographique complet n’est pas implémenté
- la sécurité NFC dépend du matériel/navigateur (Web NFC)
- un vrai système doit intégrer : audit, certification, gestion d’identité, secret du vote, résistance aux attaques, procédures légales

## Sources (chiffres)

- **Référendums sous la Ve République** : 9 depuis 1958 (hors 1958) — vie-publique.fr
- **Coût de la campagne du référendum 2005** : **130,6 M€** — réponse ministérielle publiée au JO Sénat (13/10/2005)
- **Budget 2022 — organisation des élections** : **~412,7 M€** (programme 232, action 02) — budget.gouv.fr
