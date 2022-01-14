DROP DATABASE IF EXISTS Candidature_simplon;

CREATE DATABASE Candidature_simplon;

CREATE TABLE User (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    last_name VARCHAR(50) NOT NULL,
    first_name VARCHAR(50) NOT NULL,
    telephone_number VARCHAR(50),
    e_mail VARCHAR(50) NOT NULL,
    password VARCHAR(50) NOT NULL,
    is_admin BOOL NOT NULL
);

CREATE TABLE Entreprise (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(100) NOT NULL,
    place VARCHAR(50) NOT NULL
);

CREATE TABLE Candidature (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    enterprise_id INTEGER NOT NULL,
    contact VARCHAR(100),
    date_nomination DATE,
    status VARCHAR(50) NOT NULL
);

INSERT INTO User (last_name, first_name, telephone_number, e_mail, password, is_admin) VALUES 
("Bourez", "Rudy", "06.06.06.06.06","rudy@gmail.com", "mdp", false),
("Hamour", "Yanis", "06.06.06.06.06","mail@mail.com", "******", false),
("Durand", "Brune", "","brune@gmail.com", "Admin", true),
("Abgrall", "Floriant", "06.06.06.06.06","mail@mail.com", "******", false),
("Belarbi", "Safia", "","mail@mail.com", "******", true),
("Adeoye", "Gidéon", "06.06.06.06.06","mail@mail.com", "******", false),
("Druesne", "Steven", "06.06.06.06.06","mail@mail.com", "******", false),
("Haddou", "Ayoub", "06.06.06.06.06","mail@mail.com", "******", false);

INSERT INTO Entreprise (name, place) VALUES
("Urluberlu", "Lille"),
("Taratata", "Lens"),
("Turlututu", "Seclin"),
("Rondoudou", "Marcq-en-Bareuil");

INSERT INTO Candidature (user_id, enterprise_id, contact, date_nomination, status) VALUES
(2,1,"John Doe", DATE('2021-05-07'), "En cours"),
(1,1,"Robert",DATE('2021-05-07'), "En cours"),
(5,2,"",DATE('2021-05-07'), "En cours"),
(1,1,"Patricia",DATE('2021-05-07'), "En cours"),
(7,2,"Brigitte",DATE('2021-05-07'), "En cours"),
(3,3,"",DATE('2021-05-07'), "En cours"),
(1,1,"Patrick",DATE('2021-05-07'), "En cours"),
(2,3,"Jules",DATE('2021-05-07'), "En cours");