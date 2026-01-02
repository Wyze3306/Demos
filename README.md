# 🔐 Demos - Vote Décentralisé via Blockchain

**Un système de vote démocratique sécurisé et transparent, basé sur la technologie blockchain.**

---

## 🎯 Le Concept

La démocratie moderne fait face à un défi : comment garantir que chaque vote compte vraiment ? Comment empêcher la fraude électorale tout en preservant l'anonymat du votant ? Comment garantir une transparance totale ?

**Demos** répond à ces questions en utilisant la **blockchain** : une technologie qui rend chaque vote **transparent et vérifiable**, sans révéler l'identité du votant.

### Le Problème
- 🚫 Les systèmes centralisés : une organisation (un état) contrôle tout
- 🚫 Les urnes papier : lentes, corruptibles, difficiles à auditer
- 🚫 Le vote électronique classique : confiance à une machine et corruptible

### Notre Solution
- ✅ **Décentralisé** : pas d'autorité centrale, plusieurs nœuds indépendants
- ✅ **Transparent** : tout le monde peut vérifier chaque vote
- ✅ **Anonyme** : nul ne sait qui a voté quoi
- ✅ **Immuable** : impossible de modifier un vote après coup
- ✅ **Rapide** : résultats directes

---

## 💡 Comment ça Marche ?

### Étape 1 : Tu T'inscris
Tu crées un compte avec une **clé privée** (comme un mot de passe secret) et une **clé publique** (comme ton identifiant public).

### Étape 2 : Tu votes
1. Tu choisis ton candidat/option
2. Ton vote est **chiffré** (personne ne peut le lire)
3. Tu signes ton vote avec ta clé privée (preuve que c'est bien toi)

### Étape 3 : Le Vote Entre dans la Blockchain
- Ton vote rejoint un **bloc** avec d'autres votes
- Ce bloc est **sécurisé** avec une signature cryptographique unique (SHA-256)
- Le bloc est lié au bloc précédent : formation d'une **chaîne immuable**

### Étape 4 : Les Nœuds Valident
- **10 ordinateurs indépendants** (nœuds) vérifient que :
  - Tu as le droit de voter
  - Tu n'as pas voté 2 fois
  - Ton vote est bien signé
- Ils **votent** pour accepter le bloc
- **Majorité gagne** : le bloc est accepté

### Étape 5 : Résultats Transparents
- La blockchain complète est **publique**
- N'importe qui peut télécharger l'historique complet
- On peut vérifier que chaque vote a été compté (sans savoir qui a voté quoi)

---

## 🏗️ Architecture (Vue d'Ensemble)

```
┌─────────────────────────────────────────────────────────┐
│                       DEMOS                             │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐             │
│  │ Nœud 1   │  │ Nœud 2   │  │ Nœud 3   │  ...       │
│  │ (Laptop) │  │ (Desktop)│  │ (Serveur)│  (10 max) │
│  └──────────┘  └──────────┘  └──────────┘             │
│       │              │              │                  │
│       └──────────┬───┴──────────┬───┘                  │
│                  │              │                      │
│         [Réseau Distribué P2P]                        │
│                  │              │                      │
│       ┌──────────┴──────────────┴──────┐              │
│       │                                 │              │
│    ┌──────────────────────────────────────┐           │
│    │   BLOCKCHAIN (Chaîne de Blocs)      │           │
│    │                                     │           │
│    │  ┌─────────────────────────────┐   │           │
│    │  │ Block #1 (Votes 1-100)     │   │           │
│    │  │ Hash: 0x3a4f...            │   │           │
│    │  └─────────────────────────────┘   │           │
│    │            ↓ (lié à)                │           │
│    │  ┌─────────────────────────────┐   │           │
│    │  │ Block #2 (Votes 101-200)   │   │           │
│    │  │ Hash: 0x7f2c...            │   │           │
│    │  └─────────────────────────────┘   │           │
│    │            ↓                        │           │
│    │  ┌─────────────────────────────┐   │           │
│    │  │ Block #3 (Votes 201-300)   │   │           │
│    │  │ Hash: 0x9b8e...            │   │           │
│    │  └─────────────────────────────┘   │           │
│    │                                     │           │
│    └─────────────────────────────────────┘           │
│                                                         │
│  ┌──────────────────────────────────────────────┐    │
│  │  INTERFACE WEB (pour voter)                  │    │
│  │                                              │    │
│  │  ┌────────────────────────────────────────┐ │    │
│  │  │ Bienvenue sur DemocraChain             │ │    │
│  │  │ [Connexion avec clé privée]            │ │    │
│  │  │                                        │ │    │
│  │  │ Scrutin actuel: Couleur du drapeau    │ │    │
│  │  │  ☐ Bleu  ☐ Blanc  ☐ Rouge            │ │    │
│  │  │           [VOTER]                     │ │    │
│  │  │                                        │ │    │
│  │  │ Résultats en temps réel:              │ │    │
│  │  │ Bleu: 34%  Blanc: 42%  Rouge: 24%     │ │    │
│  │  └────────────────────────────────────────┘ │    │
│  └──────────────────────────────────────────────┘    │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

---

### Programme NSI - Thèmes Couverts

| Thème NSI | Implémentation de Demos |
|-----------|----------------------------------|
| **Structures de Données** | Blockchain = structure chaînée, arbres de validation |
| **Algorithmes** | Consensus distribué, vérification de signatures |
| **Cryptographie** | RSA/ECDSA pour signer les votes, SHA256 pour hashing |
| **Bases de Données** | Registre des votes, table des électeurs, transactions |
| **Programmation Sûre** | Validation stricte, vérification d'intégrité |
| **Systèmes Distribués** | Réseau P2P, synchronisation entre nœuds |
| **Récursivité** | Vérification de la chaîne (bloc N valide si N-1 valide) |

---

## 🛠️ Les outils utilisés

```
Backend:
  - Python3
  - SQLite (base de données)
  - cryptography (chiffrement)

Frontend:
  - CSS
  - HTML
```

---

## 🚀 Cas d'Usage

### 🏛️ Politique & Entreprise
- **Élection du dirigeants** : transparent, anti-fraude
- **Transparence totale** : vérifiable par tous, incorruptible
- **Rapidité** : résultats en minutes, pas en jours
- **Anonymes** : avis honnêtes sans crainte de représailles (Régime de Vichy en France par le passé)
- **Référendum** : Référendum plus réguliers car plus simple à lancer un sondage
- **Budget** : utilisation de l'argent publique sans filtre

### 🎮 Jeux
- **Économie gamifiée** : tokens votants = réputation

---

## 📚 Documentation Supplémentaire

- 📖 **[Architecture Détaillée](docs/ARCHITECTURE.md)** - Schémas UML et diagrammes
- 🔒 **[Sécurité](docs/SECURITY.md)** - Menaces et contre-mesures
- 🛠️ **[Guide Technique](docs/TECHNICAL.md)** - Installation, API, déploiement
- 🧪 **[Tests](docs/TESTING.md)** - Comment tester le système

---

## 👥 Équipe

**Demos** est développé par une équipe de **2 étudiants NSI Terminale** dans le cadre des **Trophées NSI 2026**.

- Moi
- x

---

## 📝 Licence

Ce projet est un prototype éducatif réalisé dans le cadre des **Trophées NSI 2026**.
Ce projet est distribué sous licence MIT.

---

## 🎓 Sources & Inspirations

- Whitepaper Bitcoin (Nakamoto, 2008)[https://bitcoin.org/files/bitcoin-paper/bitcoin_fr.pdf]
- Vidéo Bitcoin V2F sur Youtube (viens, on recode Bitcoin pour le comprendre)[https://youtu.be/U4S-RGNyTJA?si=7s9qKXFBUFnTpXDs]
- Vidéo Bitcoin L'envers du décode sur Youtube (Viens on Recode le Bitcoin de ZÉRO !)[https://youtu.be/dHcrB6xwUmc?si=OC_Qyvm1J1zqRe7O]
- Actualité Vote du 1er Ministre sur Discord (vote en ligne) (L’Insurrection de la Génération Z au Népal : La Gouvernance par la Révolution Discord)[https://www.moyens.net/tech/linsurrection-generation-z-nepal-gouvernance-revolution-discord/]
- Recent Advancements in Blockchain Voting and E-Voting Systems [https://digitaldemocracyforum.com/recent-advancements-in-blockchain-voting-and-e-voting-systems/]
- Programme NSI Terminale (Info Mounier)[https://info-mounier.fr/terminale_nsi/]
