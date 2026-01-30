### https://medium.com/jungletronics/building-a-simple-blockchain-with-python-and-flask-a95da7b5b713
# TODO : Faire des classes pour les polls, users et block.

import datetime
import hashlib
import threading
import json
import secrets
import os
from http.server import BaseHTTPRequestHandler, HTTPServer

### Blockchain
# Simulation d'une blockchain qui permet de créer, de miner et de sauvegarder des votes, des utilisateurs et des sondages

class Blockchain:
    def __init__(self):
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        self.users_path = os.path.join(BASE_DIR, "users.json")
        self.polls_path = os.path.join(BASE_DIR, "polls.json")
        self.chain_path = os.path.join(BASE_DIR, "chain.json")
        
        self.votes = [] # Liste des votes en attente d'un minage de block

        # Charger les utilisateurs
        self.users = []
        with open(self.users_path, 'r', encoding='utf-8') as file:
            data_loaded = json.load(file)
            self.users = data_loaded

        # Charger les sondages
        self.polls = []
        with open(self.polls_path, 'r', encoding='utf-8') as file:
            data_loaded = json.load(file)
            self.polls = data_loaded

        # Charger la chain de tout les blocks miné (blockchain)
        self.chain = []
        with open(self.chain_path, 'r', encoding='utf-8') as file:
            data_loaded = json.load(file)
            self.chain = data_loaded

            # Genesis Block
            if data_loaded == []:
                self.create_block(proof=1, previous_hash='0')

        # Creation d'une clé par défaut pour l'utiliser pour tester le code
        test_key = self.create_key()
        print("La clé de l'utilisateur par défaut est :", test_key)

    def create_key(self):
        # Cette fonction permet de créer une clé d'identifiant aléatoire pour chaque personne de manière anonyme, on pourrait imaginer qu'elle soit créer et integré dans la carte d'identité mais inconnu et inconnaisable.
        private_key = secrets.token_hex(32)  # Génère une clé privée aléatoire
        public_key = hashlib.sha256(private_key.encode()).hexdigest()
        self.users.append(public_key)
        with open(self.users_path, 'w', encoding='utf-8') as file:
            json.dump(self.users, file, indent=4)
        return public_key

    def create_block(self, proof, previous_hash):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': str(datetime.datetime.now()),
            'proof': proof,
            'previous_hash': previous_hash,
            'votes': self.votes  # Ajouter des votes au block
        }
        self.votes = []
        self.chain.append(block)
        with open(self.chain_path, 'w', encoding='utf-8') as file:
            json.dump(self.chain, file, indent=4)
        return block

    def get_previous_block(self):
        return self.chain[-1]

    def proof_of_work(self, previous_proof):
        new_proof = 1
        check_proof = False

        while not check_proof:
            hash_operation = hashlib.sha256(
                str(new_proof** 2 - previous_proof** 2 ).encode()).hexdigest()
            if hash_operation[:5] == '00000' :
                check_proof = True
            else:
                new_proof += 1

        return new_proof

    def hash(self, block):
        encoded_block = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(encoded_block).hexdigest()

    def is_chain_valid(self, chain):
        previous_block = chain[0]
        block_index = 1
        while block_index < len(chain):
            block = chain[block_index]
            if block['previous_hash'] != self.hash(previous_block):
                return False

            previous_proof = previous_block['proof']
            proof = block['proof']
            hash_operation = hashlib.sha256(
                str (proof** 2 - previous_proof**2).encode()).hexdigest()

            if hash_operation[:5] != '00000':
                return False

            previous_block = block
            block_index += 1

        return True

    def add_vote(self, poll, user, choice):
        # Ajoute une vote à la liste des votes en attente
        self.votes.append({
            'poll': poll,
            'user' : user,
            'choice' : choice
        })
        return self.get_previous_block()['index'] + 1   # Index du bloc qui contiendra cette vote

    def add_poll(self, title, choices):
        # Ajout du sondage à la liste des sondages
        self.polls.append({
            'title' : title,
            'choices' : choices
        })
        with open(self.polls_path, 'w', encoding='utf-8') as file:
            json.dump(self.polls, file, indent=4)

        return True

    def has_voted(self, user, title_poll):
        count = 0

        for block in self.chain:
            votes = block["votes"]
            if votes != []:
                for poll in votes:
                    if poll["poll"] == title_poll and user == poll["user"]:
                        return True

        return False


### API de communication
# Permet de faire le lien entre le serveur web et la "blockchain"

class API:
    def mine_block(self):
        # Cette vérification n'est pas nécessaire mais permet d'optimisé l'espace de stockage
        if blockchain.votes == []:
            return "Il n'y a pas encore de vote dans le block donc il n'a pas été miné."

        previous_block = blockchain.get_previous_block()
        previous_proof = previous_block['proof']
        proof = blockchain.proof_of_work(previous_proof)
        previous_hash = blockchain.hash(previous_block)
        block = blockchain.create_block(proof, previous_hash)
        return block

    # Récupération de la blockchain complète
    def get_chain(self):
        return {
            'chain' : blockchain.chain,
            'length' : len (blockchain.chain)
        }

    # Vérification de la validité de la blockchain
    def is_valid(self):
        is_valid = blockchain.is_chain_valid(blockchain.chain)
        if is_valid:
            return "La blockchain est valide."
        else:
            return "La blockchain n'est pas valide."

    # Ajout d'une nouvelle vote
    def add_vote(self, vote):
        if type(vote) != dict:
            return "Le vote demandé n'est pas valide. (Pas un dictionnaire)"

        vote_keys = ['poll', 'user', 'choice']
        if len(vote) != len(vote_keys):
            return "Le vote demandé ne contient pas tout les éléments demandés.", vote_keys

        for key in vote.keys():
            if key not in vote_keys:
                return "Certains éléments du vote sont manquants.", vote_keys

        key = vote["user"]
        if not key in blockchain.users:
            # Dans un système réel cela ne devrait pas arriver car pour voter sur le site on "scannerait" la carte d'identité pour récupérer la clé privée
            return "Cette clé n'existe pas"

        if blockchain.has_voted(key, vote["poll"]):
            return "Vous avez déjà voté pour ce sondage."

        for poll in blockchain.polls:
            title = poll["title"]
            choices = poll["choices"]
            if title == vote["poll"]:
                if not vote['choice'] in choices:
                    return "La valeur du choix du vote est incorrecte."

        index = blockchain.add_vote(vote['poll'], vote['user'], vote['choice'])
        return 'Ce vote a été ajoutée au bloc', index

    def add_poll(self, poll):
        print(poll)
        if type(poll) != dict:
            return "Le sondage demandé n'est pas valide. (Pas un dictionnaire)"

        poll_keys = ['title', 'choices']
        if len(poll) != len(poll_keys):
            return "Le poll demandé ne contient pas tout les éléments demandés.", poll_keys

        for key in poll.keys():
            if key not in poll_keys:
                return "Certains éléments du poll sont manquants.", poll_keys

        title = poll["title"]
        for exist_poll in blockchain.polls:
            print(exist_poll)
            if title == exist_poll["title"]:
                return "Ce sondage existe déjà."

        index = blockchain.add_poll(poll['title'], poll['choices'])
        return 'Le sondage a bien été créé.'

    def get_count_poll_total(self, title_poll):
        count = 0

        for block in blockchain.chain:
            votes = block["votes"]
            print(votes)
            if votes != []:
                for poll in votes:
                    print(poll)
                    if poll["poll"] == title_poll:
                        count += 1

        return count

    def get_count_poll(self, title_poll, choice):
        result = []

        for block in blockchain.chain:
            votes = block["votes"]
            print(votes)
            if votes != []:
                for poll in votes:
                    print(poll)
                    if poll["poll"] == title_poll and poll["choice"] == choice:
                        result[poll["choice"]] += 1

        return result



### SERVEUR WEB
# Utilisé pour comminiqué avec le site web

class RequestHandler(BaseHTTPRequestHandler):
    def _send_json(self, data, status=200):
        response = json.dumps(data).encode()

        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(response)))
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()

        self.wfile.write(response)

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "POST, GET, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()

    def do_GET(self):
        if self.path == "/chain":
            self._send_json(API.get_chain())

        elif self.path == "/is_valid":
            self._send_json(API.is_valid())

        elif self.path == "/get_polls":
            self._send_json(blockchain.polls)

        elif self.path == "/create_user":
            self._send_json(blockchain.create_key())

        else:
            self._send_json({"error": "Route GET inconnue"}, 404)

    def do_POST(self):
        content_length = int(self.headers.get('Content-Length', 0))
        body = self.rfile.read(content_length).decode()

        if self.path == "/add_vote":
            try:
                vote = json.loads(body)
            except json.JSONDecodeError:
                self._send_json({"error": "JSON invalide"}, 400)
                return

            self._send_json(API.add_vote(vote))

        elif self.path == "/add_poll":
            try:
                poll = json.loads(body)
            except json.JSONDecodeError:
                self._send_json({"error": "JSON invalide"}, 400)
                return

            response = API.add_poll(poll)
            self._send_json(response)

        elif self.path == "/get_count_poll_total":
            try:
                poll = json.loads(body)
            except json.JSONDecodeError:
                self._send_json({"error": "JSON invalide"}, 400)
                return

            self._send_json(API.get_count_poll_total(poll['poll']))

        elif self.path == "/get_count_poll":
            try:
                poll = json.loads(body)
            except json.JSONDecodeError:
                self._send_json({"error": "JSON invalide"}, 400)
                return

            print(poll)
            print(poll['poll'])
            self._send_json(API.get_count_poll(poll['poll'], poll['choice']))

        else:
            self._send_json({"error": "Route POST inconnue"}, 404)


### Lancement de toutes les classes

# Création de la blockchain
blockchain = Blockchain()

# Lancement de l'API
API = API()

# Lancement du thread avec l'event pour miner les blocks
stop_event = threading.Event()

def task_repetitive(interval):
    while not stop_event.is_set():
        print("Le minage d'un block vient d'être lancé.")
        print(API.mine_block())
        stop_event.wait(interval)  # non bloquant pour le thread principal

# Lancer la tâche
thread = threading.Thread(
    target=task_repetitive,
    args=(5,),
    daemon=True
)
thread.start()

# Lancement du Serveur Web (natif python)
def run_web_serveur():
    server = HTTPServer(("localhost", 8000), RequestHandler)
    print("Serveur lancé sur http://localhost:8000")
    server.serve_forever()

run_web_serveur()