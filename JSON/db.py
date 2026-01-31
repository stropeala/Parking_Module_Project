"""
With this func we aim to sort all the date we have in separate jsons:
    - a separate json for each client with their id and time inside the parking lot
    - a json with the all the clients and their timers
    - a json with the clients that stayed under 2 hours parked
    - a json with the clients that stayed over 2 hours parked
    - a json wioth the clients hat stayed 3 days or more parked
"""

import datetime
import json
import os
import pathlib
import random
import time


# We create a func that stores the timetable data for each client
def db(filepath, id):
    # We start by making a separate json for each client and their time inside the parking lot
    # We use the filepath inside the clients func so if that path changes this doesnt break
    db_filepath = f"{pathlib.Path(filepath).parent.resolve()}/client_timers/client_id{id}_timer.json"
    # We check if the json exists
    if os.path.isfile(db_filepath) is True:
        # If the json exists we open in read mode
        with open(db_filepath, "r") as file:
            client_db = json.load(file)
    # If the json doesn't exist we start with an empty dict
    else:
        client_db = {}

    # We create an entry dict template
    # We also note the entry time for each client
    intrare = datetime.datetime.now()
    client_db_dict_start = {
        "ID": id,
        "Date & Hour": {"Intrare in parcare": str(intrare)},
    }

    # We combine the two dicts into a new one
    db_start_dict = client_db | client_db_dict_start
    # We open the json in write mode and dump the new dict
    # With this we will write a new json for each client timer by id
    with open(db_filepath, "w") as file:
        # indent=4 for better format
        json.dump(db_start_dict, file, indent=4)

    # We make a var with a random amout of time for the timer later
    ore = random.randint(1, 10)
    # We now start by making if statements to sort the jsons
    if 1 <= ore <= 3:
        # If the time is between adn including 1 and 3
        # we make a json for the clients that aprked for less than 2 hrs
        # We use the filepath inside the clients func so if that path changes this doesnt break
        db_filepath_u2hours = (
            f"{pathlib.Path(filepath).parent.resolve()}/clients_timer_under_2hours.json"
        )
        # We check if the json exists
        if os.path.isfile(db_filepath_u2hours) is True:
            # If the json exists we open in read mode
            with open(db_filepath_u2hours, "r") as file:
                client_db_u2hours = json.load(file)
        # If the json doesn't exist we start with an empty list
        else:
            client_db_u2hours = []

        # We make a timer loop that simulates the time inside the parking lot
        t = ore
        while t:
            time.sleep(1)
            t -= 1

        # We create an under 2 hr client dict template
        iesire = datetime.datetime.now()
        client_db_dict_u2hours = {
            "ID": id,
            "Date & Hour": {
                "Intrare in parcare": str(intrare),
                "Iesire din parcare": str(iesire),
                "Timp": f"{ore} ore",
            },
        }

        # We add the new dict to the first list
        client_db_u2hours.append(client_db_dict_u2hours)
        # We open the json in write mode and dump the new list with the dicts
        with open(db_filepath_u2hours, "w") as file:
            json.dump(client_db_u2hours, file, indent=4)

        # Now we start doing the same thing for the other jsons
        db_filepath = f"{pathlib.Path(filepath).parent.resolve()}/client_timers/client_id{id}_timer.json"
        with open(db_filepath, "r") as file:
            client_db = json.load(file)

        client_db["Date & Hour"]["Iesire din parcare"] = str(iesire)
        client_db["Date & Hour"]["Timp"] = f"{ore} ore"
        with open(db_filepath, "w") as file:
            json.dump(client_db, file, indent=4)

        db_filepath2 = f"{pathlib.Path(filepath).parent.resolve()}/client_timers/client_timers.json"
        if os.path.isfile(db_filepath2) is True:
            with open(db_filepath2, "r") as file:
                client_db2 = json.load(file)
        else:
            client_db2 = []

        client_db_dict_start2 = {
            "ID": id,
            "Date & Hour": {
                "Intrare in parcare": str(intrare),
                "Iesire din parcare": str(iesire),
                "Timp": f"{ore} ore",
            },
        }

        client_db2.append(client_db_dict_start2)
        with open(db_filepath2, "w") as file:
            json.dump(client_db2, file, indent=4)

    # If the time is between 3 and 7
    # we make a json for the clients that parked for more than 2 hrs
    elif 3 < ore < 7:
        db_filepath_2hours = (
            f"{pathlib.Path(filepath).parent.resolve()}/clients_timer_above_2hours.json"
        )
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

        db_filepath = f"{pathlib.Path(filepath).parent.resolve()}/client_timers/client_id{id}_timer.json"
        with open(db_filepath, "r") as file:
            client_db = json.load(file)

        client_db["Date & Hour"]["Iesire din parcare"] = str(iesire)
        client_db["Date & Hour"]["Timp"] = f"{ore} ore"
        with open(db_filepath, "w") as file:
            json.dump(client_db, file, indent=4)

        db_filepath2 = f"{pathlib.Path(filepath).parent.resolve()}/client_timers/client_timers.json"
        if os.path.isfile(db_filepath2) is True:
            with open(db_filepath2, "r") as file:
                client_db2 = json.load(file)
        else:
            client_db2 = []

        client_db_dict_start2 = {
            "ID": id,
            "Date & Hour": {
                "Intrare in parcare": str(intrare),
                "Iesire din parcare": str(iesire),
                "Timp": f"{ore} ore",
            },
        }

        client_db2.append(client_db_dict_start2)
        with open(db_filepath2, "w") as file:
            json.dump(client_db2, file, indent=4)

    # If the time is more than 7
    # we make a json for the clients that parked for more than 3 days
    elif 7 <= ore:
        db_filepath_3days = (
            f"{pathlib.Path(filepath).parent.resolve()}/clients_timer_above_3days.json"
        )
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

        db_filepath = f"{pathlib.Path(filepath).parent.resolve()}/client_timers/client_id{id}_timer.json"
        with open(db_filepath, "r") as file:
            client_db = json.load(file)

        client_db["Date & Hour"]["Iesire din parcare"] = str(iesire)
        client_db["Date & Hour"]["Timp"] = f"{ore} ore"
        with open(db_filepath, "w") as file:
            json.dump(client_db, file, indent=4)

        db_filepath2 = f"{pathlib.Path(filepath).parent.resolve()}/client_timers/client_timers.json"
        if os.path.isfile(db_filepath2) is True:
            with open(db_filepath2, "r") as file:
                client_db2 = json.load(file)
        else:
            client_db2 = []

        client_db_dict_start2 = {
            "ID": id,
            "Date & Hour": {
                "Intrare in parcare": str(intrare),
                "Iesire din parcare": str(iesire),
                "Timp": f"{ore} ore",
            },
        }

        client_db2.append(client_db_dict_start2)
        with open(db_filepath2, "w") as file:
            json.dump(client_db2, file, indent=4)

    # This adds the exit time for the separate jsons
    else:
        db_filepath = f"{pathlib.Path(filepath).parent.resolve()}/client_timers/client_id{id}_timer.json"
        with open(db_filepath, "r") as file:
            client_db = json.load(file)

        t = ore
        while t:
            time.sleep(1)
            t -= 1

        iesire = datetime.datetime.now()
        client_db["Date & Hour"]["Iesire din parcare"] = str(iesire)
        client_db["Date & Hour"]["Timp"] = f"{ore} ore"
        with open(db_filepath, "w") as file:
            json.dump(client_db, file, indent=4)

        db_filepath2 = f"{pathlib.Path(filepath).parent.resolve()}/client_timers/client_timers.json"
        if os.path.isfile(db_filepath2) is True:
            with open(db_filepath2, "r") as file:
                client_db2 = json.load(file)
        else:
            client_db2 = []

        client_db_dict_start2 = {
            "ID": id,
            "Date & Hour": {
                "Intrare in parcare": str(intrare),
                "Iesire din parcare": str(iesire),
                "Timp": f"{ore} ore",
            },
        }

        client_db2.append(client_db_dict_start2)
        with open(db_filepath2, "w") as file:
            json.dump(client_db2, file, indent=4)
