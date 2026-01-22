import json
import os

from db_draft import db_start_draft


# We create a func that adds a new client to a json file without deleteing the old ones
def clients_draft(filepath, nume, prenume, telefon, oras, pariah=False):
    # We check if the json exists
    if os.path.isfile(filepath) is True:
        # If the json exists we open in read mode
        with open(filepath, "r") as file:
            all_clients = json.load(file)
    # If the json doesn't exist we start with an empty list
    else:
        all_clients = []

    # We create a client dict template
    id = len(all_clients) + 1
    client = {
        "ID": id,
        "Nume": nume,
        "Prenume": prenume,
        "Nr.Telefon": telefon,
        "Oras": oras,
        "Pariah": pariah,
    }

    # We add the new client dict to the all_clients list
    all_clients.append(client)

    # We open the json in write mode and convert the all_clients list to a json
    with open(filepath, "w") as file:
        # indent=4 for better farmat
        json.dump(all_clients, file, indent=4)

    db_start_draft(filepath, id)
