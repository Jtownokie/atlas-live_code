--sudo apt-install pkg-config

ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'insert_password';
FLUSH PRIVILEGES;

CREATE DATABASE livecode;

CREATE TABLE artists (
    ArtistID int,
    FullName varchar(255),
    Age int,
    PRIMARY KEY (ArtistID)
);

CREATE TABLE songs (
    Title varchar(255),
    ArtistID int,
    FOREIGN KEY (ArtistID),
);

INSERT INTO artists
VALUES (1, 'ArtistName', 20);

INSERT INTO artists
VALUES (2, 'ArtistName', 30);

INSERT INTO artists
Values (3, 'ArtistName', 40);

INSERT INTO songs
VALUES ('SongTitle', 1);

INSERT INTO songs
VALUES ('SongTitle', 1);

INSERT INTO songs
VALUES ('SongTitle', 1);

INSERT INTO songs
VALUES ('SongTitle', 2);

INSERT INTO songs
VALUES ('SongTitle', 2);

INSERT INTO songs
VALUES ('SongTitle', 2);

INSERT INTO songs
VALUES ('SongTitle', 3);

INSERT INTO songs
VALUES ('SongTitle', 3);

INSERT INTO songs
VALUES ('SongTitle', 3);

UPDATE songs
SET Title = 'SongTitle'
WHERE Title = 'SongTitle';

DELETE FROM songs
WHERE Title = 'SongTitle'
