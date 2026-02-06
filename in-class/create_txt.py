import datetime
import os
import random


def create_clients_and_db_txt(
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

    entry = client_entry(year=2026, month=2)
    exit = client_exit(year=2026, month=2)

    while exit <= entry:
        exit = client_exit(year=2026, month=2)

    time = exit - entry

    # String from which we read data.
    new_client_db = f"{id}, {entry}, {exit}, {time}\n"

    # "All clients db" is the existing database plus the new database
    all_clients_db = existing_clients_db + new_client_db

    with open(filepath_db, "w") as file:
        # Writes to "all clients DB"
        file.write(all_clients_db)


def client_exit(year=2026, month=2):
    day = random.randint(1, 7)
    hour = random.randint(0, 23)
    minute = random.randint(0, 59)
    second = random.randint(0, 59)
    exit = datetime.datetime(year, month, day, hour, minute, second)
    return exit


def client_entry(year=2026, month=2):
    entry = datetime.datetime(
        year,
        month,
        day=random.randint(1, 7),
        hour=random.randint(0, 23),
        minute=random.randint(0, 59),
        second=random.randint(0, 59),
    )
    return entry


if __name__ == "__main__":
    filepath_clients = "in-class/data/txt/clients.txt"
    filepath_db = "in-class/data/txt/db.txt"

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
        31: ("Connor", "Mitchell", 13235558921, "PhoenixUSA"),
        32: ("Diana", "Perez", 442071234567, "ManchesterUK"),
        33: ("Elijah", "Roberts", 12135557892, "LosAngelesUSA"),
        34: ("Fiona", "Turner", 61395551234, "MelbourneAustralia"),
        35: ("George", "Phillips", 14255556543, "BostonUSA"),
        36: ("Hannah", "Campbell", 498912367845, "BerlinGermany"),
        37: ("Isaac", "Parker", 33145678912, "LyonFrance"),
        38: ("Julia", "Evans", 13125559876, "ChicagoUSA"),
        39: ("Kevin", "Edwards", 46851234567, "MalmoSweden"),
        40: ("Laura", "Collins", 819012345678, "OsakaJapan"),
        41: ("Mason", "Stewart", 8613912345678, "ShanghaiChina"),
        42: ("Nina", "Sanchez", 14385559123, "MontrealCanada"),
        43: ("Oscar", "Morris", 5521987654321, "RioDeJaneiroBrazil"),
        44: ("Penny", "Rogers", 27315551234, "JohannesburgSouthAfrica"),
        45: ("Quentin", "Reed", 390612345678, "RomeItaly"),
        46: ("Ruby", "Cook", 972521234567, "JerusalemIsrael"),
        47: ("Simon", "Morgan", 34611234567, "BarcelonaSpain"),
        48: ("Tara", "Bell", 353861234567, "CorkIreland"),
        49: ("Ulysses", "Murphy", 5255512345678, "GuadalajaraMexico"),
        50: ("Violet", "Bailey", 5411123456789, "CordobaArgentina"),
        51: ("Walter", "Rivera", 64271234567, "WellingtonNewZealand"),
        52: ("Wendy", "Cooper", 41781234567, "GenevaSwitzerland"),
        53: ("Xavier", "Richardson", 971521234567, "AbuDhabiUAE"),
        54: ("Yasmin", "Cox", 351962345678, "PortoPortugal"),
        55: ("Zachary", "Howard", 821112345678, "BusanSouthKorea"),
        56: ("Abigail", "Ward", 2349012345678, "AbujaNigeria"),
        57: ("Blake", "Torres", 79261234567, "SaintPetersburgRussia"),
        58: ("Chloe", "Peterson", 923211234567, "KarachiPakistan"),
        59: ("Derek", "Gray", 6581234567, "SingaporeSingapore"),
        60: ("Elena", "Ramirez", 46741234567, "UppsalaSweden"),
        61: ("Felix", "James", 12025557654, "WashingtonDCUSA"),
        62: ("Gina", "Watson", 447811234567, "BirminghamUK"),
        63: ("Hugo", "Brooks", 12135558901, "SanDiegoUSA"),
        64: ("Iris", "Kelly", 61285551234, "BrisbaneAustralia"),
        65: ("James", "Sanders", 14155557890, "OaklandUSA"),
        66: ("Kate", "Price", 498915678234, "FrankfurtGermany"),
        67: ("Liam", "Bennett", 33345678912, "MarseileFrance"),
        68: ("Maya", "Wood", 13035558765, "AustinUSA"),
        69: ("Nathan", "Barnes", 46761234567, "HelsingborgSweden"),
        70: ("Olive", "Ross", 815012345678, "YokohamaJapan"),
        71: ("Peter", "Henderson", 8613712345678, "GuangzhouChina"),
        72: ("Quincy", "Coleman", 14035559456, "CalgaryCanada"),
        73: ("Rosa", "Jenkins", 5531987654321, "BrasiliaBrazil"),
        74: ("Steve", "Perry", 27825551234, "DurbanSouthAfrica"),
        75: ("Tess", "Powell", 390312345678, "FlorenceItaly"),
        76: ("Troy", "Long", 972531234567, "HaifaIsrael"),
        77: ("Uma", "Patterson", 34915234567, "ValenciaSpain"),
        78: ("Victor", "Hughes", 353851234567, "GalwayIreland"),
        79: ("Willow", "Flores", 5215612345678, "MonterreyMexico"),
        80: ("Xander", "Washington", 5421123456789, "RosarioArgentina"),
        81: ("Yara", "Butler", 64221234567, "ChristchurchNewZealand"),
        82: ("Zane", "Simmons", 41761234567, "BaselSwitzerland"),
        83: ("Amelia", "Foster", 971541234567, "SharjahUAE"),
        84: ("Brian", "Gonzales", 351922345678, "CoimbraPortugal"),
        85: ("Clara", "Bryant", 821212345678, "IncheonSouthKorea"),
        86: ("Dante", "Alexander", 2347012345678, "PortHarcourtNigeria"),
        87: ("Ella", "Russell", 79651234567, "KazanRussia"),
        88: ("Finn", "Griffin", 923121234567, "IslamabadPakistan"),
        89: ("Gemma", "Diaz", 6571234567, "SingaporeSingapore"),
        90: ("Henry", "Hayes", 46811234567, "LundSweden"),
        91: ("Isla", "Myers", 13105557123, "PortlandUSA"),
        92: ("Jake", "Ford", 442031234567, "LeedsUK"),
        93: ("Kira", "Hamilton", 12125558234, "BrooklynUSA"),
        94: ("Lucas", "Graham", 61735551234, "PerthAustralia"),
        95: ("Molly", "Sullivan", 14085556789, "SanJoseUSA"),
        96: ("Nolan", "Wallace", 498917834562, "HamburgGermany"),
        97: ("Ophelia", "Woods", 33456789123, "NiceFrance"),
        98: ("Preston", "Cole", 17025559087, "LasVegasUSA"),
        99: ("Rika", "Freeman", 46901234567, "NorrkopingSweden"),
        100: ("Shane", "Wells", 817012345678, "NagoyaJapan"),
    }
    # Data added to the string.
    for first, last, phone, city in clients.values():
        create_clients_and_db_txt(
            filepath_clients, filepath_db, first, last, phone, city
        )
