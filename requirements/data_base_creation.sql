SET GLOBAL validate_password.policy = LOW;
CREATE DATABASE IF NOT EXISTS edupathway_db;
CREATE DATABASE IF NOT EXISTS edupathway_test_db;
CREATE USER IF NOT EXISTS 'edupathway_user'@'localhost' IDENTIFIED BY 'edupathway_pwd';
GRANT ALL PRIVILEGES ON edupathway_db.* TO 'edupathway_user'@'localhost';
GRANT ALL PRIVILEGES ON edupathway_test_db.* TO 'edupathway_user'@'localhost';
FLUSH PRIVILEGES;
