DROP TABLE IF EXISTS people;
DROP TABLE IF EXISTS places;

CREATE TABLE places (
  id INT NOT NULL AUTO_INCREMENT,
  city NVARCHAR(100),
  county NVARCHAR(100),
  country NVARCHAR(100),
  PRIMARY KEY (id)
);

CREATE TABLE people (
  id INT NOT NULL AUTO_INCREMENT,
  given_name NVARCHAR(100),
  family_name NVARCHAR(100),
  date_of_birth DATE,
  place_of_birth NVARCHAR(100),
  place_id INT,
  FOREIGN KEY (place_id) references places(id),
  PRIMARY KEY (id)
);