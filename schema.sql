create database ponto;
use ponto;

CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    foto VARCHAR(150) DEFAULT "https://i.ibb.co/WW3BbPfY/default.png",
    nome VARCHAR(75) UNIQUE NOT NULL,
    senha VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    pontuacao INT DEFAULT 0
);

CREATE TABLE ranking (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario_id INT NOT NULL UNIQUE,
    posicao INT NOT NULL,

    FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
);

CREATE TABLE historico (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario_id INT NOT NULL UNIQUE,
    vitorias INT DEFAULT 0,
    derrotas INT DEFAULT 0,
    palavras INT DEFAULT 0,
    ultima_palavra VARCHAR(5),

    FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
);

INSERT INTO usuarios (nome, senha, email)
VALUES ("Josué", "admin123", "josuealexandre69@gmail.com"),
       ("Kayke", "000145", "kayke00@gmail.com");