import json
import os
import pathlib
import re

from db import db


# We create a func that adds a new client to a json file without deleteing the old ones
def clients(filepath, nume, prenume, telefon, oras, pariah=False):
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
    # We open the json in write mode
    # and dump the all_clients list containig the dicts to a json
    with open(filepath, "w") as file:
        # indent=4 for better format
        json.dump(all_clients, file, indent=4)

    # We call the func that sorts the data
    db(filepath, id)

    # We open the json with all the clients timers that we made
    # and open it in read mode to extract the list
    db_filepath2 = (
        f"{pathlib.Path(filepath).parent.resolve()}/client_timers/client_timers.json"
    )
    with open(db_filepath2, "r") as file:
        client_db2 = json.load(file)

    # We make a for loop for each dict in the list
    # to check the timer and change tha pariah value
    # if its over the "3 days" threshold
    ids = list(range(len(all_clients)))
    for i in ids:
        timp_str = client_db2[i]["Date & Hour"]["Timp"]
        match = re.findall(r"\d+", timp_str)
        timp_int = int(match[0])
        if 7 <= timp_int:
            # We update the dict with True
            all_clients[i].update({"Pariah": True})

    # Now we open the same file to overwrite with our new list
    with open(filepath, "w") as file:
        # indent=4 for better format
        json.dump(all_clients, file, indent=4)

    # We make a json with only the people with pariah true
    pariah_filepath = (
        f"{pathlib.Path(filepath).parent.resolve()}/clients_pariah_true.json"
    )

    # We make an empty list and add to it only the dicts with pariah true
    pariah_clients = []
    for client in all_clients:
        if client.get("Pariah") is True:
            pariah_clients.append(client)

    # We write the json
    with open(pariah_filepath, "w") as file:
        json.dump(pariah_clients, file, indent=4)
