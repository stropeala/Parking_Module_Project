import datetime
import json
import os
import pathlib
import random
import time


# We create a func that stores the timetable data for each client
def db_draft(filepath, id):
    db_filepath = f"{pathlib.Path(filepath).parent.resolve()}/client_timers_draft/client_id{id}_timer_draft.json"
    if os.path.isfile(db_filepath) is True:
        with open(db_filepath, "r") as file:
            client_db = json.load(file)
    else:
        client_db = {}

    intrare = datetime.datetime.now()
    client_db_dict_start = {
        "ID": id,
        "Date & Hour": {"Intrare in parcare": str(intrare)},
    }

    db_start_dict = client_db | client_db_dict_start
    with open(db_filepath, "w") as file:
        json.dump(db_start_dict, file, indent=4)

    ore = random.randint(1, 10)
    if 1 <= ore <= 3:
        db_filepath_u2hours = f"{pathlib.Path(filepath).parent.resolve()}/clients_timer_under_2hours_draft.json"
        if os.path.isfile(db_filepath_u2hours) is True:
            with open(db_filepath_u2hours, "r") as file:
                client_db_u2hours = json.load(file)
        else:
            client_db_u2hours = []

        t = ore
        while t:
            time.sleep(1)
            t -= 1

        iesire = datetime.datetime.now()
        client_db_dict_u2hours = {
            "ID": id,
            "Date & Hour": {
                "Intrare in parcare": str(intrare),
                "Iesire din parcare": str(iesire),
                "Timp": f"{ore} ore",
            },
        }

        client_db_u2hours.append(client_db_dict_u2hours)
        with open(db_filepath_u2hours, "w") as file:
            json.dump(client_db_u2hours, file, indent=4)

        db_filepath = f"{pathlib.Path(filepath).parent.resolve()}/client_timers_draft/client_id{id}_timer_draft.json"
        with open(db_filepath, "r") as file:
            client_db = json.load(file)

        client_db["Date & Hour"]["Iesire din parcare"] = str(iesire)
        client_db["Date & Hour"]["Timp"] = f"{ore} ore"
        with open(db_filepath, "w") as file:
            json.dump(client_db, file, indent=4)

    elif 3 < ore < 7:
        db_filepath_2hours = f"{pathlib.Path(filepath).parent.resolve()}/clients_timer_above_2hours_draft.json"
        if os.path.isfile(db_filepath_2hours) is True:
            with open(db_filepath_2hours, "r") as file:
                client_db_2hours = json.load(file)
        else:
            client_db_2hours = []

        t = ore
        while t:
            time.sleep(1)
            t -= 1

        iesire = datetime.datetime.now()
        client_db_dict_2hours = {
            "ID": id,
            "Date & Hour": {
                "Intrare in parcare": str(intrare),
                "Iesire din parcare": str(iesire),
                "Timp": f"{ore} ore",
            },
        }

        client_db_2hours.append(client_db_dict_2hours)
        with open(db_filepath_2hours, "w") as file:
            json.dump(client_db_2hours, file, indent=4)

        db_filepath = f"{pathlib.Path(filepath).parent.resolve()}/client_timers_draft/client_id{id}_timer_draft.json"
        with open(db_filepath, "r") as file:
            client_db = json.load(file)

        client_db["Date & Hour"]["Iesire din parcare"] = str(iesire)
        client_db["Date & Hour"]["Timp"] = f"{ore} ore"
        with open(db_filepath, "w") as file:
            json.dump(client_db, file, indent=4)

    elif 7 <= ore:
        db_filepath_3days = f"{pathlib.Path(filepath).parent.resolve()}/clients_timer_above_3days_draft.json"
        if os.path.isfile(db_filepath_3days) is True:
            with open(db_filepath_3days, "r") as file:
                client_db_3days = json.load(file)
        else:
            client_db_3days = []

        t = ore
        while t:
            time.sleep(1)
            t -= 1

        iesire = datetime.datetime.now()
        client_db_dict_3days = {
            "ID": id,
            "Date & Hour": {
                "Intrare in parcare": str(intrare),
                "Iesire din parcare": str(iesire),
                "Timp": f"{ore} ore",
            },
        }

        client_db_3days.append(client_db_dict_3days)
        with open(db_filepath_3days, "w") as file:
            json.dump(client_db_3days, file, indent=4)

        db_filepath = f"{pathlib.Path(filepath).parent.resolve()}/client_timers_draft/client_id{id}_timer_draft.json"
        with open(db_filepath, "r") as file:
            client_db = json.load(file)

        client_db["Date & Hour"]["Iesire din parcare"] = str(iesire)
        client_db["Date & Hour"]["Timp"] = f"{ore} ore"
        with open(db_filepath, "w") as file:
            json.dump(client_db, file, indent=4)

    else:
        db_filepath = f"{pathlib.Path(filepath).parent.resolve()}/client_timers_draft/client_id{id}_timer_draft.json"
        with open(db_filepath, "r") as file:
            client_db = json.load(file)

        t = ore
        while t:
            time.sleep(1)
            t -= 1

        client_db["Date & Hour"]["Iesire din parcare"] = str(datetime.datetime.now())
        client_db["Date & Hour"]["Timp"] = f"{ore} ore"
        with open(db_filepath, "w") as file:
            json.dump(client_db, file, indent=4)
