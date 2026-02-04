import datetime
import os
import random
from time import sleep


def create_clients_and_db(
    filepath_clients: str,
    filepath_db: str,
    nume: str,
    prenume: str,
    telefon: int,
    oras: str,
    pariah=False,
) -> None:
    # We check if the file exists
    if os.path.isfile(filepath_clients):
        with open(filepath_clients, "r") as file:
            existing_clients = file.read()
    else:
        existing_clients = ""

    id = random.randint(1, 65000)
    new_client = f"{id}, {nume}, {prenume}, {telefon}, {oras}, {pariah}\n"

    all_clients = existing_clients + new_client

    with open(filepath_clients, "w") as file:
        file.write(all_clients)

    db(filepath_db, id)


def db(filepath_db: str, id: int) -> None:
    if os.path.isfile(filepath_db):
        with open(filepath_db, "r") as file:
            existing_clients_db = file.read()
    else:
        existing_clients_db = ""

    entry = datetime.datetime.now()

    hours = random.randint(1, 10)

    t = hours
    while t:
        sleep(1)
        t -= 1

    exit = datetime.datetime.now()

    time = exit - entry

    new_client_db = f"{id}, {str(entry)}, {str(exit)}, {str(time)}\n"

    all_clients_db = existing_clients_db + new_client_db

    with open(filepath_db, "w") as file:
        file.write(all_clients_db)


if __name__ == "__main__":
    filepath_clients = "in-class/data/clients.txt"
    filepath_db = "in-class/data/db.txt"

    clients = {
        1: ("Lynn", "Newton", 2063428631, "Seattle"),
        2: ("Sunt", "UnTest", 783265872, "Timisoara"),
        3: ("Alice", "Johnson", 912345678, "NewYork"),
        4: ("Bob", "Smith", 823456789, "Chicago"),
        5: ("Carol", "Williams", 734567890, "SanFrancisco"),
        6: ("David", "Brown", 645678901, "Austin"),
        7: ("Emma", "Davis", 556789012, "Boston"),
        8: ("Frank", "Miller", 467890123, "Denver"),
        9: ("Grace", "Wilson", 378901234, "Portland"),
        10: ("Henry", "Moore", 289012345, "LosAngeles"),
        11: ("Ivy", "Taylor", 190123456, "SanDiego"),
        12: ("Jack", "Anderson", 901234567, "Phoenix"),
        13: ("Karen", "Thomas", 812345670, "Dallas"),
        14: ("Leo", "Jackson", 723456781, "Atlanta"),
        15: ("Mia", "White", 634567892, "Miami"),
        16: ("Noah", "Harris", 545678903, "Orlando"),
        17: ("Olivia", "Martin", 456789014, "Tampa"),
        18: ("Paul", "Thompson", 367890125, "Nashville"),
        19: ("Quinn", "Garcia", 278901236, "SanAntonio"),
        20: ("Rachel", "Martinez", 189012347, "ElPaso"),
        21: ("Sam", "Robinson", 890123458, "LasVegas"),
        22: ("Tina", "Clark", 701234569, "Reno"),
        23: ("Umar", "Rodriguez", 612345670, "Houston"),
        24: ("Vera", "Lewis", 523456781, "Minneapolis"),
        25: ("Will", "Lee", 434567892, "SanJose"),
        26: ("Xena", "Walker", 345678903, "Oakland"),
        27: ("Yuri", "Hall", 256789014, "Sacramento"),
        28: ("Zara", "Allen", 167890125, "Berkeley"),
        29: ("Aaron", "Young", 978901236, "PaloAlto"),
        30: ("Bella", "King", 889012347, "MountainView"),
    }

    for first, last, phone, city in clients.values():
        create_clients_and_db(filepath_clients, filepath_db, first, last, phone, city)
