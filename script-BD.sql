-- ============================================
-- CRIAÇÃO DO BANCO DE DADOS
-- ============================================
CREATE DATABASE sistema_votacao;
USE sistema_votacao;


-- ============================================
-- TABELA ELEITOR
-- Guarda eleitores e mesários
-- A autenticação usa:
-- titulo_eleitor + cpf_quatro_primeiros + chave_acesso
-- ============================================
CREATE TABLE eleitor (
    id_eleitor INT AUTO_INCREMENT UNIQUE,
    nome_completo VARCHAR(150) NOT NULL,
    cpf VARCHAR(255) PRIMARY KEY NOT NULL UNIQUE,
    titulo_eleitor VARCHAR(20) NOT NULL UNIQUE,
    chave_acesso VARCHAR(255) NOT NULL UNIQUE,
    eh_mesario BOOLEAN NOT NULL DEFAULT FALSE,
    ja_votou BOOLEAN NOT NULL DEFAULT FALSE
    
);

INSERT INTO eleitor
(nome_completo, cpf, titulo_eleitor, chave_acesso, eh_mesario, ja_votou)
VALUES
('Lucas Marassi', '10987654321', '123456789012', 'LUM1234', TRUE, FALSE),
('Ana Souza', '12345678901', '111122223333', 'ANS5678', FALSE, FALSE),
('Carlos Lima', '98765432100', '444455556666', 'CAL9012', FALSE, FALSE),
('Mariana Costa', '45678912300', '777788889999', 'MAC3456', FALSE, FALSE);


-- ============================================
-- TABELA CANDIDATO
-- Guarda candidatos da eleição
-- ============================================
CREATE TABLE candidato (
    id_candidato INT AUTO_INCREMENT UNIQUE,
    nome VARCHAR(150) NOT NULL,
    numero INT PRIMARY KEY NOT NULL UNIQUE,
    partido VARCHAR(50) NOT NULL

);
INSERT INTO candidato (nome, numero, partido)
VALUES
('João Silva', 50, 'ABC'),
('Maria Souza', 20, 'XYZ'),
('Carlos Oliveira', 30, 'DEF'),
('Fernanda Lima', 40, 'QWE');

INSERT INTO candidato (nome, numero, partido)
VALUES
('João Silva', 10, 'ABC'),
('Maria Souza', 20, 'XYZ'),
('Carlos Lima', 30, 'DEF');

-- ============================================
-- TABELA SESSAO_VOTACAO
-- Controla abertura e encerramento da eleição
-- ============================================
CREATE TABLE sessao_votacao (
    id_sessao INT PRIMARY KEY AUTO_INCREMENT UNIQUE,
    aberta BOOLEAN NOT NULL DEFAULT FALSE,
    data_abertura DATETIME NULL,
    data_encerramento DATETIME NULL
);
DELETE FROM sessao_votacao
WHERE id_sessao = 6;

-- ============================================
-- TABELA VOTO
-- Guarda os votos da eleição
-- id_candidato pode ser NULL para voto nulo
-- ============================================
CREATE TABLE voto (
    id_voto INT PRIMARY KEY AUTO_INCREMENT UNIQUE,
    numero_candidato INT NULL,
    id_sessao INT NOT NULL,
    data_hora DATETIME NOT NULL,
    protocolo VARCHAR(255) NOT NULL UNIQUE,


    CONSTRAINT fk_voto_candidato
        FOREIGN KEY (numero_candidato)
        REFERENCES candidato(numero),

    CONSTRAINT fk_voto_sessao
        FOREIGN KEY (id_sessao)
        REFERENCES sessao_votacao(id_sessao)
);
select * from voto;
DELETE FROM voto
WHERE id_sessao = 6;

drop database sistema_votacao;