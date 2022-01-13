import sqlite3
conn = sqlite3.connect('base_test.db')
my_cursor = conn.cursor()
my_cursor.execute("""
    CREATE TABLE IF NOT EXISTS User(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        last_name VARCHAR(50) NOT NULL,
        first_name VARCHAR(50) NOT NULL,
        telephone_number VARCHAR(50),
        e_mail VARCHAR(50) NOT NULL,
        password VARCHAR(50) NOT NULL,
        is_admin BOOLEAN NOT NULL
    );""")
my_cursor.execute("""
    CREATE TABLE IF NOT EXISTS Entreprise(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(100) NOT NULL,
        place VARCHAR(50) NOT NULL
    );""")
my_cursor.execute("""
    CREATE TABLE IF NOT EXISTS Candidature(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        enterprise_id INTEGER NULL,
        contact VARCHAR(100)
    );""")

my_cursor.executemany("INSERT INTO User(last_name,first_name,telephone_number,e_mail,password,is_admin) VALUES(?,?,?,?,?,?)", 
    [("Bourez", "Rudy", "060660606","mail@mail.com", "******", False),
    ("Hamour", "Yanis", "0606060606","mail@mail.com", "******", False),
    ("Durand", "Brune", "","mail@mail.com", "******", True),
    ("Abgrall", "Floriant", "0606060606","mail@mail.com", "******", False),
    ("Belarbi", "Safia", "","mail@mail.com", "******", True),
    ("Adeoye", "Gidéon", "0606060606","mail@mail.com", "******", False),
    ("Druesne", "Steven", "0606060606","mail@mail.com", "******", False),
    ("Haddou", "Ayoub", "0606060606","mail@mail.com", "******", False)]
    )
my_cursor.executemany("""
    INSERT INTO Entreprise (name,place) VALUES (?,?)""",
    [("Urluberlu", "Lille"),
    ("Taratata", "Lens"),
    ("Turlututu", "Seclin"),
    ("Rondoudou", "Marcq-en-Bareuil")]
    )
my_cursor.executemany("""
    INSERT INTO Candidature (user_id,enterprise_id,contact) VALUES (?,?,?)""",
    [(0,0,"John Doe"),
    (1,1,"Robert"),
    (5,2,""),
    (1,1,"Patricia"),
    (7,2,"Brigitte"),
    (3,3,""),
    (0,0,"Patrick"),
    (1,3,"Jules")]
    )
conn.commit()
conn.close()
