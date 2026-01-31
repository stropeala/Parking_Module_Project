import sqlite3
from datetime import datetime
from os import path
from re import findall
from time import sleep


def create_db(db_path: str) -> None:
    # Connect to the SQLite database or create it if it doesnt exist
    conn = sqlite3.connect(db_path)

    # Create a cursor object to interact with the database
    cursor = conn.cursor()

    # SQL query to create the table
    sql = """
        CREATE TABLE "Clients" (
       	"ID"	INTEGER UNIQUE,
       	"First_Name"	TEXT,
       	"Last_Name"	TEXT,
       	"Phone_Nr"	NUMERIC UNIQUE,
       	"City_of_Residence"	TEXT,
       	"DateTime_entrance"	NUMERIC,
       	"DateTime_exit"	NUMERIC,
        "Hours_Parked" NUMERIC,
       	"Pariah"	TEXT,
       	PRIMARY KEY("ID" AUTOINCREMENT)
        );
    """

    # Execute the table creation query
    cursor.execute(sql)

    # Close the connections to the database
    cursor.close()
    conn.close()

    print("Table created!\nContinuing...")


def get_conn(db_path: str) -> sqlite3.Connection:
    # We get connection to db only if db_path is valid
    if path.isfile(db_path):
        con = sqlite3.connect(db_path)
    else:
        print("Couldn't connect to database!")
    return con  # pyright: ignore


def write_client(
    db_path: str,
    firstname: str,
    lastname: str,
    phone: str,
    city: str,
    entry: str,
) -> None:
    conn = get_conn(db_path)
    if conn:
        cursor = conn.cursor()
        sql = f"""
            INSERT INTO Clients
            ('First_Name', 'Last_Name', 'Phone_Nr','City_of_residence',
            'DateTime_entrance', 'DateTime_exit','Hours_Parked', 'Pariah')
            VALUES
            ('{firstname}', '{lastname}', '{phone}', '{city}',
            '{entry}', 'None', 'None', 'False')
        """
        print(sql)
        cursor.execute(sql)
        conn.commit()
        cursor.close()
        conn.close()
    else:
        print("Couldn't connect to database!")


def timer(hours: int):
    if 1 <= hours <= 3:
        t = hours
        while t:
            sleep(1)
            t -= 1
        exit = str(datetime.now())
        return exit

    elif 3 < hours < 7:
        t = hours
        while t:
            sleep(1)
            t -= 1
        exit = str(datetime.now())
        return exit

    elif 7 <= hours < 10:
        t = hours
        while t:
            sleep(1)
            t -= 1
        exit = str(datetime.now())
        return exit

    else:
        t = hours
        while t:
            sleep(1)
            t -= 1
        exit = str(datetime.now())
        return exit


def update_hrs_parked(db_path: str, exit, hours: int) -> None:
    conn = get_conn(db_path)
    if conn:
        cursor = conn.cursor()
        sql1 = f"UPDATE Clients SET DateTime_exit='{exit}' WHERE DateTime_exit='None'"
        cursor.execute(sql1)
        conn.commit()
        sql2 = f"UPDATE Clients SET Hours_Parked='{hours}' WHERE Hours_Parked='None'"
        cursor.execute(sql2)
        conn.commit()
        cursor.close()
        conn.close()
    else:
        print("Couldn't connect to database!")


def update_pariah(db_path: str) -> None:
    conn = get_conn(db_path)
    if conn:
        cursor = conn.cursor()
        sql = "UPDATE Clients SET Pariah='True' WHERE Hours_Parked >= 7"
        cursor.execute(sql)
        conn.commit()
        cursor.close()
        conn.close()
    else:
        print("Couldn't connect to database!")


def create_extra_table(db_path: str) -> None:
    conn = get_conn(db_path)
    if conn:
        cursor = conn.cursor()

        sql1 = """
            CREATE TABLE Under_2Hours AS
            SELECT *
            FROM Clients
            WHERE Hours_Parked <= 3;
        """
        cursor.execute(sql1)

        sql2 = """
            CREATE TABLE Over_2Hours AS
            SELECT *
            FROM Clients
            WHERE Hours_Parked > 3 AND Hours_Parked < 7;
        """
        cursor.execute(sql2)

        cursor.execute("DROP TABLE IF EXISTS Over_3Days")
        sql3 = """
            CREATE TABLE Over_3Days AS
            SELECT *
            FROM Clients
            WHERE Hours_Parked >= 7;
        """
        cursor.execute(sql3)

        cursor.close()
        conn.close()
    else:
        print("Couldn't connect to database!")


def read_and_write_extra_tables(db_path: str) -> list:
    # Get a connection to the db
    conn = get_conn(db_path)

    if conn:
        # Get a cursor object fro the connection
        cursor = conn.cursor()

        # Build the SQL query
        sql1 = """
            SELECT ID
            FROM Clients
            GROUP BY ID
            HAVING min(Hours_Parked) <= 3;
        """
        # Execute the prepared SQL query (sql)
        cursor.execute(sql1)
        # Retrieve/Get/Fetch all entries/rows from the cursor
        id = findall(r"\d+", str(cursor.fetchall()))
        print(
            f"IDs of clients who were parked for less than 2 hours: {id}\nExtra table created: Under_2Hours\n"
        )

        sql2 = """
            SELECT ID
            FROM Clients
            GROUP BY ID
            HAVING min(Hours_Parked) > 3 AND max(Hours_Parked) < 7;
        """
        cursor.execute(sql2)
        id2 = findall(r"\d+", str(cursor.fetchall()))
        print(
            f"IDs of clients who were parked for more than 2 hours: {id2}\nExtra table created: Over_2Hours\n"
        )

        sql3 = """
            SELECT ID
            FROM Clients
            GROUP BY ID
            HAVING min(Hours_Parked) >= 7;
        """
        cursor.execute(sql3)
        id3 = findall(r"\d+", str(cursor.fetchall()))
        cursor.close()
        conn.close()
        print(
            f"IDs of clients who were parked for more than 3 days: {id3}\nExtra table created: Over_3Days\n"
        )
        create_extra_table(db_path)

    else:
        print("Couldn't connect to database!")

    return []
