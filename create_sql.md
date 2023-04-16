# Create Table Statements


## Lawyers Table
CREATE TABLE Lawyers(
    LawyerID CHAR(4) NOT NULL, -- L001, L002, L003, ...
    LastName VARCHAR(255) NOT NULL,
    FirstName VARCHAR(255) NOT NULL,
    Member_Of_Bar_Since YEAR NOT NULL,
    PRIMARY KEY(LawyerID)
);

## Clients Table
CREATE TABLE Clients(
    ClientID CHAR(6) NOT NULL,
    Company_Name VARCHAR(255) NOT NULL,
    Industry ENUM("Tech", "Healthcare", "Finance", "Energy and Utilities", "Transportation", "Education", "Automotive", "Defense", "Construction", "Other") NOT NULL,
    Client_Since YEAR NOT NULL,
    UNIQUE(Company_Name),
    PRIMARY KEY(ClientID)
);

## Cases Table
CREATE TABLE Cases(
    CaseID INT(255) AUTO_INCREMENT NOT NULL,
    LawyerID CHAR(4) NOT NULL,
    ClientID CHAR(6) NOT NULL,
    Ongoing BOOL NOT NULL,
    Judgement_Date DATE,
    Win BOOL, 
    PRIMARY KEY(CaseID),
    FOREIGN KEY(LawyerID) REFERENCES Lawyers(LawyerID),
    FOREIGN KEY(ClientID) REFERENCES Clients(ClientID)
);


## Billings Table
CREATE TABLE Billings(
    BillID INT(255) AUTO_INCREMENT NOT NULL,
    ClientID CHAR(6) NOT NULL,
    Earnings FLOAT(23) NOT NULL,
    Billed_on DATE NOT NULL,
    Reason VARCHAR(255) NOT NULL,
    PRIMARY KEY(BillID),
    FOREIGN KEY(ClientID) REFERENCES Clients(ClientID)
);