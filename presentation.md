# DEMOS — script de présentation

## 1) Introduction (20 secondes)

Bonjour, nous sommes **Rémy Grisollet**, **Alban Henry** et **Ricky Tébaldi**.

Notre projet s’appelle **DEMOS**.
C’est une **simulation** de ce que pourrait devenir un système de vote moderne :
- plus accessible (vote à distance),
- plus auditable,
- et pensé autour d’une **blockchain**.

L’idée n’est pas de dire “on a inventé le vote officiel du futur”, mais de montrer **un prototype pédagogique** et une vision réaliste d’intégration.

## 2) Le constat : aujourd’hui, voter coûte cher et reste lourd

Première réalité : organiser un vote, c’est cher.

Pour donner un ordre de grandeur :
- dans le budget de l’État, la ligne “**organisation des élections**” (programme 232, action 02) prévoit **environ 412,7 millions d’euros** en 2022 pour organiser notamment la présidentielle et les législatives.

Deuxième réalité : les référendums sont rares.
- Sous la Ve République, il y a eu **9 référendums** depuis 1958 (sans compter celui de 1958).

Et pourtant, quand on en organise un, le coût est significatif :
- pour la campagne du référendum de 2005, une réponse ministérielle indique une dépense évaluée à **130,6 millions d’euros** (impression, envois aux électeurs, subventions aux communes, campagne audiovisuelle).

Donc on a un paradoxe :
- on dit “il faut faire participer les citoyens”,
- mais on a un outil, le référendum, peu utilisé, notamment parce qu’il est complexe et coûteux à déployer.

## 3) Le risque : manipulations et fraudes

Troisième réalité : même dans un pays démocratique, il y a eu des affaires de fraude ou d’irrégularités.

Exemple concret en France :
- l’**affaire des faux électeurs du 5e arrondissement de Paris**, avec des inscriptions fictives sur listes électorales et une condamnation.

L’idée n’est pas de dire “tout est truqué”, mais de rappeler une chose :
- un système **centralisé** et **peu auditable** crée de la défiance,
- et une fraude, même locale, suffit à fragiliser la confiance.

## 4) Notre idée : une blockchain de votes

DEMOS illustre une approche : enregistrer les votes dans une **chaîne de blocs**.

Concrètement, une blockchain, c’est :
- une liste de blocs,
- chaque bloc contient des votes,
- et chaque bloc contient le **hash** du bloc précédent.

Ce que ça apporte :
- **Immutabilité** : si quelqu’un modifie un vote dans un bloc, le hash change, et la chaîne ne “colle” plus.
- **Traçabilité / audit** : on peut vérifier l’intégrité de l’historique.
- **Décentralisation** : au lieu d’un seul serveur “qui décide”, on peut imaginer plusieurs validateurs indépendants.

Et c’est là que la décentralisation devient un concept important :
- si une seule entité contrôle tout, elle peut aussi tout “arranger”.
- si plusieurs entités contrôlent les mêmes données et se surveillent mutuellement, falsifier devient beaucoup plus difficile.

## 5) Une intégration réaliste : carte d’identité / passeport au lieu de carte d’électeur DEMOS

Dans notre démo, on simule l’identification via **NFC**.
L’idée à terme serait de s’appuyer sur un document déjà existant :
- la **carte d’identité** ou le **passeport**, qui contiennent une puce.

Objectif :
- ne pas dépendre d’une “carte de vote DEMOS” spécifique,
- mais s’intégrer dans la République avec un outil déjà distribué.

Le rôle de la carte serait uniquement :
- prouver que “je suis une personne réelle et autorisée à voter”,
- sans mettre l’identité dans la blockchain.

Important : dans un vrai système, il faut préserver **le secret du vote**.
Donc l’identification sert à obtenir un **droit de vote**, pas à stocker “qui vote quoi”.

## 6) Les validateurs : mairies, universités, entreprises sous contrat

Une blockchain publique comme Bitcoin rémunère les mineurs avec une cryptomonnaie.

Dans un système républicain, on peut imaginer autre chose :
- des validateurs **certifiés** (mairies, universités, entreprises, opérateurs publics/privés),
- choisis via un **contrat avec l’État** (obligations de disponibilité, audits, sécurité).

Leur “récompense” serait :
- une **rémunération de service** (pas un token),
- comparable au coût d’infrastructure et d’organisation.

L’idée défendue dans notre proposition est que :
- une partie du coût actuel (impression, envois, centralisation) pourrait être réduite,
- et que, dans un scénario optimiste, on pourrait viser un coût global **divisé par 2** sur certains postes logistiques.

## 7) La démo : comment fonctionne DEMOS aujourd’hui

DEMOS est composé de deux parties :

- un **serveur Python** qui simule une blockchain et une API HTTP,
- un **site web** qui permet de créer des scrutins et de voter.

Parcours de démo :
- on crée un sondage dans `admin.html`,
- on récupère une clé utilisateur (démo),
- on vote dans `vote.html`,
- et le serveur mine automatiquement un bloc avec les votes.

On peut ensuite consulter :
- la blockchain complète,
- et vérifier qu’elle est cohérente.

## 8) Limites et honnêteté scientifique

On assume clairement les limites :
- ce prototype stocke les données en JSON local,
- il ne simule pas un vrai réseau P2P,
- et il ne contient pas toutes les briques d’un système officiel : chiffrement du bulletin, preuves cryptographiques, audits de sécurité, cadre légal.

Mais il démontre l’essentiel :
- comment on obtient une **trace immuable**,
- comment on rend un vote **auditable**,
- et comment on peut imaginer une gouvernance **décentralisée et contractualisée**.

## 9) Conclusion

DEMOS est une démo qui pose une question simple :
**comment moderniser la démocratie, sans sacrifier la confiance ?**

Merci.

## Sources

- vie-publique.fr : **9 référendums** sous la Ve République depuis 1958 (hors 1958)
- JO Sénat (réponse publiée le 13/10/2005) : **130,6 M€** pour l’organisation de la campagne du référendum 2005
- budget.gouv.fr (programme 232, action 02) : **~412,7 M€** prévus en 2022 pour l’organisation des élections
