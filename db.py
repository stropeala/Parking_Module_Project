import datetime
import json
import os
import pathlib


# We create a func that stores the timetable data for each client
def db_start(filepath, id):
    db_filepath = f"{pathlib.Path(filepath).parent.resolve()}/db.json"
    if os.path.isfile(db_filepath) is True:
        with open(db_filepath, "r") as file:
            all_clients_db = json.load(file)
    else:
        all_clients_db = []

    client_db = {
        "ID": id,
        "Date & Hour": {"Intrare in parcare": str(datetime.datetime.now())},
    }

    all_clients_db.append(client_db)

    with open(db_filepath, "w") as file:
        # indent=4 for better farmat
        json.dump(all_clients_db, file, indent=4)
