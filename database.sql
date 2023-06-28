CREATE DATABASE crud_usuarios;

USE crud_usuarios;

CREATE TABLE users (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  cpf VARCHAR(14) NOT NULL,
  login VARCHAR(255) NOT NULL,
  password VARCHAR(255) NOT NULL
);

SELECT * FROM crud_usuarios.users;

INSERT INTO `users` (`name`, `cpf`, `login`, `password`) VALUES
('teste um', '111111111-11', 'teste1@gmail.com', '111'),
('teste dois', '222222222-22', 'teste2@gmail.com', '222'),
('teste tres', '333333333-33', 'teste3@gmail.com', '333'),
('teste quatro', '444444444-44', 'teste4@gmail.com', '444');
