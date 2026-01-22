import datetime
import json
import os
import pathlib
import random
import time


# We create a func that stores the timetable data for each client
def db_start(filepath, id):
    db_filepath = f"{pathlib.Path(filepath).parent.resolve()}/ID_{id}_timer.json"
    if os.path.isfile(db_filepath) is True:
        with open(db_filepath, "r") as file:
            client_db = json.load(file)
    else:
        client_db = {}

    client_db_dict_start = {
        "ID": id,
        "Date & Hour": {"Intrare in parcare": str(datetime.datetime.now())},
    }

    db_start_dict = client_db | client_db_dict_start

    with open(db_filepath, "w") as file:
        # indent=4 for better farmat
        json.dump(db_start_dict, file, indent=4)


def db_end(filepath, id):
    db_filepath = f"{pathlib.Path(filepath).parent.resolve()}/ID_{id}_timer.json"

    ore = random.randint(1, 96)
    t = ore
    while t:
        time.sleep(1)
        t -= 1

    with open(db_filepath, "r") as file:
        client_db = json.load(file)

    client_db["Date & Hour"]["Iesire din parcare"] = str(datetime.datetime.now())
    client_db["Date & Hour"]["Timp"] = f"{ore} ore"
    with open(db_filepath, "w") as file:
        # indent=4 for better farmat
        json.dump(client_db, file, indent=4)
