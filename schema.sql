create database pontest;
use pontest;

CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(50),
    email VARCHAR(100)
);

INSERT INTO usuarios (nome, email) VALUES ("Josué", "josue@email.com");
INSERT INTO usuarios (nome, email) VALUES ("Kayke", "kayke@gmail.com");