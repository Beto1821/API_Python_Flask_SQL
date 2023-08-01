USE dbcarros;

CREATE TABLE Carros (
    id INTEGER NOT NULL auto_increment PRIMARY KEY,
    marca VARCHAR(100),
    modelo VARCHAR(100),
    ano INTEGER
);

SET CHARACTER_SET_CLIENT = utf8;
SET CHARACTER_SET_CONNECTIONS = utf8;
SET CHARACTER_SET_RESULTS = utf8;
SET COLLATION_CONNECTIONS = utf8_general_ci;

INSERT INTO Carros (marca, modelo, ano) VALUES ('Fiat', 'Marea', 1999);
INSERT INTO Carros (marca, modelo, ano) VALUES ('Fiat', 'Uno', 1992);
INSERT INTO Carros (marca, modelo, ano) VALUES ('Ford', 'Escort', 1985);
INSERT INTO Carros (marca, modelo, ano) VALUES ('Chevrolet', 'Chevette', 1978);
INSERT INTO Carros (marca, modelo, ano) VALUES ('Volkswagen', 'Fusca', 1962);