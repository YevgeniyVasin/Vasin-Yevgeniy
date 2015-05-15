# Vasin-Yevgeniy
CREATE TABLE IF NOT EXISTS Person (
  idPerson INT NOT NULL AUTO_INCREMENT,
  Name  VARCHAR(45) NULL,
  Сitizenship  VARCHAR(45) NULL,
  SerialNumberPassport  VARCHAR(45) NULL,
  Adress  VARCHAR(45) NULL,
  Birthday  DATE NULL,
  BirthPlace  VARCHAR(45) NULL,
  p_idMarriage  INT NULL,
  IssueBy  VARCHAR(45) NULL,
  DateOfIssue  DATE NULL,
  PRIMARY KEY ( idPerson ));

CREATE TABLE IF NOT EXISTS Marriage (
  idMarriage INT NOT NULL AUTO_INCREMENT,
  m_idFiance INT NULL,
  m_idFiancee INT NULL,
  OldSurnameM VARCHAR(45) NULL,
  NewSurnameM VARCHAR(45) NULL,
  OldSurnameW VARCHAR(45) NULL,
  NewSurnameW VARCHAR(45) NULL,
  Organization  VARCHAR(45) NULL,
  СertificateSerialNumber  VARCHAR(45) NULL,
  PRIMARY KEY ( idMarriage ),
  INDEX  m_idFiance_idx  ( m_idFiance  ASC),
  INDEX  m_idFiancee_idx  ( m_idFiancee  ASC),
  CONSTRAINT  m_idFiance 
    FOREIGN KEY ( m_idFiance )
    REFERENCES    Person  ( idPerson ),
  CONSTRAINT  m_idFiancee 
    FOREIGN KEY ( m_idFiancee )
    REFERENCES    Person  ( idPerson ));

CREATE TABLE IF NOT EXISTS  Application  (
  idApplication  INT NOT NULL AUTO_INCREMENT,
  ApplicationNumber  DECIMAL NULL,
  Date  DATE NULL,
  app_idPerson  INT NULL,
  Act  VARCHAR(45) NULL,
  PRIMARY KEY ( idApplication ),
  INDEX  app_idPerson_idx  ( app_idPerson  ASC),
  CONSTRAINT  app_idPerson 
    FOREIGN KEY ( app_idPerson )
    REFERENCES    Person  ( idPerson ));

CREATE TABLE IF NOT EXISTS    Burn  (
  idBurn  INT NOT NULL AUTO_INCREMENT,
  b_idApplication  INT NULL,
  Name  VARCHAR(45) NULL,
  Date  DATE NULL,
  PlaceBurn  VARCHAR(45) NULL,
  Livestillborn  TINYINT(1) NULL,
  b_idNameFather  INT NULL,
  b_idNameMother  INT NULL,
  b_idPerson  INT NULL,
  СertificateSerialNumber  VARCHAR(45) NULL,
  PRIMARY KEY ( idBurn ),
  INDEX  b_idApplication_idx  ( b_idApplication  ASC),
  INDEX  b_idNameFather_idx  ( b_idNameFather  ASC),
  INDEX  b_idNameMother_idx  ( b_idNameMother  ASC),
  INDEX  b_idPerson_idx  ( b_idPerson  ASC),
  CONSTRAINT  b_idApplication 
    FOREIGN KEY ( b_idApplication )
    REFERENCES    Application  ( idApplication ),
  CONSTRAINT  b_idNameFather 
    FOREIGN KEY ( b_idNameFather )
    REFERENCES    Person  ( idPerson ),
  CONSTRAINT  b_idNameMother 
    FOREIGN KEY ( b_idNameMother )
    REFERENCES    Person  ( idPerson ),
  CONSTRAINT  b_idPerson 
    FOREIGN KEY ( b_idPerson )
    REFERENCES    Person  ( idPerson ));

CREATE TABLE IF NOT EXISTS    Die  (
  idDie  INT NOT NULL AUTO_INCREMENT,
  d_idApplication  INT NULL,
  d_idPerson  INT NULL,
  Date  DATE NULL,
  Place  VARCHAR(45) NULL,
  Reason  VARCHAR(45) NULL,
  d_idApplicant  INT NULL,
  СertificateSerialNumber  VARCHAR(45) NULL,
  PRIMARY KEY ( idDie ),
  INDEX  d_idApplication_idx  ( d_idApplication  ASC),
  INDEX  d_idPerson_idx  ( d_idPerson  ASC),
  INDEX  d_idApplicant_idx  ( d_idApplicant  ASC),
  CONSTRAINT  d_idApplication 
    FOREIGN KEY ( d_idApplication )
    REFERENCES    Application  ( idApplication ),
  CONSTRAINT  d_idPerson 
    FOREIGN KEY ( d_idPerson )
    REFERENCES    Person  ( idPerson ),
  CONSTRAINT  d_idApplicant 
    FOREIGN KEY ( d_idApplicant )
    REFERENCES    Person  ( idPerson ));

CREATE TABLE IF NOT EXISTS  ChangeName  (
  idChangeName  INT NOT NULL AUTO_INCREMENT,
  ch_idPerson  INT NULL,
  NewName  VARCHAR(45) NULL,
  ch_idBurn  INT NULL,
  PRIMARY KEY ( idChangeName ),
  INDEX  ch_idPerson_idx  ( ch_idPerson  ASC),
  INDEX  ch_idBurn_idx  ( ch_idBurn  ASC),
  CONSTRAINT  ch_idPerson 
    FOREIGN KEY ( ch_idPerson )
    REFERENCES    Person  ( idPerson ),
  CONSTRAINT  ch_idBurn 
    FOREIGN KEY ( ch_idBurn )
    REFERENCES    Burn  ( idBurn ));

