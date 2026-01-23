import re

all_clients = [
    {
        "ID": 1,
        "Nume": "Frank",
        "Prenume": "Fleming",
        "Nr.Telefon": "(810) 011-4394",
        "Oras": "Port Huron, MI",
        "Pariah": "false",
    },
    {
        "ID": 2,
        "Nume": "Keith",
        "Prenume": "Wood",
        "Nr.Telefon": "(475) 651-6147",
        "Oras": "Bridgeport, CT",
        "Pariah": "false",
    },
    {
        "ID": 3,
        "Nume": "Marty",
        "Prenume": "Koch",
        "Nr.Telefon": "(681) 518-7418",
        "Oras": "Charleston, WV",
        "Pariah": "false",
    },
    {
        "ID": 4,
        "Nume": "Billie",
        "Prenume": "Forbes",
        "Nr.Telefon": "(570) 542-1228",
        "Oras": "Scranton, PA",
        "Pariah": "false",
    },
    {
        "ID": 5,
        "Nume": "Deloris",
        "Prenume": "White",
        "Nr.Telefon": "(386) 167-3182",
        "Oras": "Palm Coast, FL",
        "Pariah": "false",
    },
    {
        "ID": 6,
        "Nume": "Sherwood",
        "Prenume": "Holder",
        "Nr.Telefon": "(574) 347-8989",
        "Oras": "Elkhart, IN",
        "Pariah": "false",
    },
    {
        "ID": 7,
        "Nume": "Tobias",
        "Prenume": "Snyder",
        "Nr.Telefon": "(502) 947-8597",
        "Oras": "Louisville, KY",
        "Pariah": "false",
    },
    {
        "ID": 8,
        "Nume": "Mattie",
        "Prenume": "Garcia",
        "Nr.Telefon": "(270) 921-6744",
        "Oras": "Henderson, KY",
        "Pariah": "false",
    },
    {
        "ID": 9,
        "Nume": "Hugh",
        "Prenume": "Maxwell",
        "Nr.Telefon": "(530) 532-3263",
        "Oras": "Davis, CA",
        "Pariah": "false",
    },
    {
        "ID": 10,
        "Nume": "Diana",
        "Prenume": "Acosta",
        "Nr.Telefon": "(724) 410-6441",
        "Oras": "Mccandless, PA",
        "Pariah": "false",
    },
]


client_db2 = [
    {
        "ID": 1,
        "Date & Hour": {
            "Intrare in parcare": "2026-01-23 12:02:40.415549",
            "Iesire din parcare": "2026-01-23 12:02:49.416221",
            "Timp": "9 ore",
        },
    },
    {
        "ID": 2,
        "Date & Hour": {
            "Intrare in parcare": "2026-01-23 12:02:49.416733",
            "Iesire din parcare": "2026-01-23 12:02:57.417276",
            "Timp": "8 ore",
        },
    },
    {
        "ID": 3,
        "Date & Hour": {
            "Intrare in parcare": "2026-01-23 12:02:57.417793",
            "Iesire din parcare": "2026-01-23 12:02:58.417940",
            "Timp": "1 ore",
        },
    },
    {
        "ID": 4,
        "Date & Hour": {
            "Intrare in parcare": "2026-01-23 12:02:58.418477",
            "Iesire din parcare": "2026-01-23 12:03:07.419129",
            "Timp": "9 ore",
        },
    },
    {
        "ID": 5,
        "Date & Hour": {
            "Intrare in parcare": "2026-01-23 12:03:07.419678",
            "Iesire din parcare": "2026-01-23 12:03:15.420272",
            "Timp": "8 ore",
        },
    },
    {
        "ID": 6,
        "Date & Hour": {
            "Intrare in parcare": "2026-01-23 12:03:15.421694",
            "Iesire din parcare": "2026-01-23 12:03:21.422159",
            "Timp": "6 ore",
        },
    },
    {
        "ID": 7,
        "Date & Hour": {
            "Intrare in parcare": "2026-01-23 12:03:21.422792",
            "Iesire din parcare": "2026-01-23 12:03:23.423026",
            "Timp": "2 ore",
        },
    },
    {
        "ID": 8,
        "Date & Hour": {
            "Intrare in parcare": "2026-01-23 12:03:23.423974",
            "Iesire din parcare": "2026-01-23 12:03:31.424637",
            "Timp": "8 ore",
        },
    },
    {
        "ID": 9,
        "Date & Hour": {
            "Intrare in parcare": "2026-01-23 12:03:31.425307",
            "Iesire din parcare": "2026-01-23 12:03:36.425742",
            "Timp": "5 ore",
        },
    },
    {
        "ID": 10,
        "Date & Hour": {
            "Intrare in parcare": "2026-01-23 12:03:36.426580",
            "Iesire din parcare": "2026-01-23 12:03:39.426905",
            "Timp": "3 ore",
        },
    },
]

ids = list(range(len(all_clients)))
for i in ids:
    timp_str = client_db2[i]["Date & Hour"]["Timp"]
    match = re.findall(r"\d", timp_str)
    timp_int = int(match[0])
    if 7 <= timp_int:
        all_clients[i].update({"Pariah": True})
