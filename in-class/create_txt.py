import datetime
import os
import random


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
        # opens the file in read mode. Places all data in the file in existing_clients.
        with open(filepath_clients, "r") as file:
            existing_clients = file.read()
    else:
        # if the file doesn't exist, create an empty string to write to.
        existing_clients = ""

    # Creates a random ID and a string for the clients.
    id = random.randint(100, 999)

    new_client = f"{id}, {nume}, {prenume}, {telefon}, {oras}, {pariah}\n"

    # all_clients is the existing clients list, as well as the added clients.
    all_clients = existing_clients + new_client

    with open(filepath_clients, "w") as file:
        # Opens the file again, this time in write mode.
        file.write(all_clients)

    # We call db func
    db(filepath_db, id)


def db(filepath_db: str, id: int) -> None:
    if os.path.isfile(filepath_db):
        # Opens DB in read mode, then adds all existing data to a string. If no string exists, creates new string.
        with open(filepath_db, "r") as file:
            existing_clients_db = file.read()
    else:
        existing_clients_db = ""

    exit = client_exit(year=2026, month=2)

    entry = client_entry(year=2026, month=2)

    time = exit - entry

    # String from which we read data.
    new_client_db = f"{id}, {entry}, {exit}, {time}\n"

    # "All clients db" is the existing database plus the new database
    all_clients_db = existing_clients_db + new_client_db

    with open(filepath_db, "w") as file:
        # Writes to "all clients DB"
        file.write(all_clients_db)


def client_exit(year=2026, month=2):

    day = random.randint(3, 4)
    hour = random.randint(0, 12)
    minute = 0
    second = 0

    exit = datetime.datetime(year, month, day, hour, minute, second)

    return exit


def client_entry(year=2026, month=2):

    entry = datetime.datetime(
        year,
        month,
        day=random.randint(1, 2),
        hour=random.randint(0, 23),
        minute=random.randint(0, 59),
        second=random.randint(0, 59),
    )

    return entry


if __name__ == "__main__":
    filepath_clients = "in-class/data/clients.txt"
    filepath_db = "in-class/data/db.txt"

    clients = {
        1: ("Lynn", "Newton", 12065557341, "SeattleUSA"),
        2: ("Ethan", "Coleman", 447911284563, "LondonUK"),
        3: ("Alice", "Johnson", 12125559034, "NewYorkUSA"),
        4: ("Robert", "Smith", 61298765432, "SydneyAustralia"),
        5: ("Carol", "Williams", 14155556721, "SanFranciscoUSA"),
        6: ("David", "Brown", 498912345678, "MunichGermany"),
        7: ("Emma", "Davis", 33612345678, "ParisFrance"),
        8: ("Frank", "Miller", 13035559912, "DenverUSA"),
        9: ("Grace", "Wilson", 46701234567, "StockholmSweden"),
        10: ("Henry", "Moore", 813090123456, "TokyoJapan"),
        11: ("Ivy", "Taylor", 8613812345678, "BeijingChina"),
        12: ("Jack", "Anderson", 14165559821, "TorontoCanada"),
        13: ("Karen", "Thomas", 5511987654321, "SaoPauloBrazil"),
        14: ("Leo", "Jackson", 27215551234, "CapeTownSouthAfrica"),
        15: ("Mia", "White", 390212345678, "MilanItaly"),
        16: ("Noah", "Harris", 972501234567, "TelAvivIsrael"),
        17: ("Olivia", "Martin", 34911234567, "MadridSpain"),
        18: ("Paul", "Thompson", 353871234567, "DublinIreland"),
        19: ("Quinn", "Garcia", 5215512345678, "MexicoCityMexico"),
        20: ("Rachel", "Martinez", 5491123456789, "BuenosAiresArgentina"),
        21: ("Samuel", "Robinson", 64211234567, "AucklandNewZealand"),
        22: ("Tina", "Clark", 41791234567, "ZurichSwitzerland"),
        23: ("Umar", "Rodriguez", 971501234567, "DubaiUAE"),
        24: ("Vera", "Lewis", 351912345678, "LisbonPortugal"),
        25: ("William", "Lee", 821012345678, "SeoulSouthKorea"),
        26: ("Xena", "Walker", 2348012345678, "LagosNigeria"),
        27: ("Yuri", "Hall", 79161234567, "MoscowRussia"),
        28: ("Zara", "Allen", 923001234567, "LahorePakistan"),
        29: ("Aaron", "Young", 6591234567, "SingaporeSingapore"),
        30: ("Bella", "King", 46731234567, "GothenburgSweden"),
    }
    # Data added to the string.
    for first, last, phone, city in clients.values():
        create_clients_and_db(filepath_clients, filepath_db, first, last, phone, city)
