#create remote user with all access
create user 'app'@'%' IDENTIFIED WITH mysql_native_password BY 'app';
GRANT ALL PRIVILEGES ON *.* TO 'app'@'%';
FLUSH PRIVILEGES;


CREATE TABLE employees (
Name varchar(25) NOT NULL,
cpf  varchar(12) PRIMARY KEY,
address varchar(15) NOT NULL);
