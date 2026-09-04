CREATE DATABASE AeroGuard;
USE AeroGuard;

CREATE TABLE Localizacao (
    idLocalizacao INT PRIMARY KEY AUTO_INCREMENT,
    estado VARCHAR(45),
    cidade VARCHAR(45),
    cep CHAR(8),
    numero VARCHAR(10)
);

CREATE TABLE Aeroporto (
    idAeroporto INT PRIMARY KEY AUTO_INCREMENT,
    cnpj CHAR(14),
    nomeFantasia VARCHAR(45),
    email VARCHAR(45),
    telefone VARCHAR(15),
    nome VARCHAR(45),
    codigoIATA CHAR(3),
    fkLocalizacao INT,
    codigo CHAR(5),
    CONSTRAINT fk_Aeroporto_Localizacao 
        FOREIGN KEY (fkLocalizacao) REFERENCES Localizacao(idLocalizacao)
);

CREATE TABLE User (
    idUser INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(45),
    cargo VARCHAR(45),
    email VARCHAR(45),
    senha VARCHAR(45),
    cpf CHAR(11),
    fkAeroportoUsuario INT,
    CONSTRAINT fk_User_Aeroporto 
        FOREIGN KEY (fkAeroportoUsuario) REFERENCES Aeroporto(idAeroporto)
);

CREATE TABLE Maquina (
    idMaquina INT PRIMARY KEY AUTO_INCREMENT,
    hostname VARCHAR(45),
    fkUser INT,
    so VARCHAR(45),
    macAddress VARCHAR(45),
    CONSTRAINT fk_Maquina_User 
        FOREIGN KEY (fkUser) REFERENCES User(idUser)
);

CREATE TABLE Metrica (
    idMetrica INT PRIMARY KEY AUTO_INCREMENT,
    Metrica VARCHAR(45),
    unidadeMedida VARCHAR(45)
);

CREATE TABLE ParametroMonitoramento (
    fkMaquina INT,
    fkMetrica INT,
    limite DOUBLE,
    PRIMARY KEY (fkMaquina, fkMetrica),
    CONSTRAINT fk_Parametro_Maquina 
        FOREIGN KEY (fkMaquina) REFERENCES Maquina(idMaquina),
    CONSTRAINT fk_Parametro_Metrica 
        FOREIGN KEY (fkMetrica) REFERENCES Metrica(idMetrica)
);

CREATE TABLE HistoricoLeitura (
    idLeitura INT PRIMARY KEY AUTO_INCREMENT,
    fkMetricas INT,
    fkMaquina INT,
    fkParametroMonitoramento INT,
    valorCapturado FLOAT,
    horario DATETIME,
    CONSTRAINT fk_Historico_Metrica 
        FOREIGN KEY (fkMetricas) REFERENCES Metrica(idMetrica),
    CONSTRAINT fk_Historico_Maquina 
        FOREIGN KEY (fkMaquina) REFERENCES Maquina(idMaquina)
);