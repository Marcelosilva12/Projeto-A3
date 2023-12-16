-- Criação do Banco de Dados
CREATE DATABASE IF NOT EXISTS loja;
USE loja;

-- Criação da Tabela de Produtos
CREATE TABLE IF NOT EXISTS produtos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    estoque INT NOT NULL,
    quantidadeVendida INT NOT NULL
);

-- Inserção de Dados na Tabela de Produtos
INSERT INTO produtos (nome, estoque, quantidadeVendida) VALUES
    ('Smartphone', 50, 10),
    ('Notebook', 30, 5),
    ('TV 4K', 20, 8),
    ('Câmera DSLR', 40, 12),
    ('Fone de Ouvido Bluetooth', 60, 15),
    ('Console de Videogame', 25, 7),
    ('Impressora Multifuncional', 35, 20),
    ('Tablet', 45, 18),
    ('Monitor Ultrawide', 55, 25),
    ('Drone', 15, 3),
    ('Computador', 10, 9),
    ('Iphone', 4, 24),
    ('Câmera', 5, 37)
    ;

-- Criação da Tabela de Clientes
CREATE TABLE IF NOT EXISTS clientes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL
);

-- Inserção de Dados na Tabela de Clientes
INSERT INTO clientes (nome, email) VALUES
    ('João Silva', 'joao.silva@example.com'),
    ('Ana Oliveira', 'ana.oliveira@example.com'),
    ('Carlos Santos', 'carlos.santos@example.com'),
    ('Camila Lima', 'camila.lima@example.com'),
    ('Roberto Pereira', 'roberto.pereira@example.com');
