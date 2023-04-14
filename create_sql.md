# Create SQL commands:

## Table 1 (Lawyers)
CREATE TABLE Lawyers(
    LawyerID CHAR(4) NOT NULL,
    LastName VARCHAR(255) NOT NULL,
    FirstName VARCHAR(255) NOT NULL,
    Member_Of_Bar_Since YEAR NOT NULL,
    PRIMARY KEY(LawyerID)
);

## Table 2 (Clients)
CREATE TABLE Clients(
    ClientID CHAR(6) NOT NULL,
    Company_Name VARCHAR(255) NOT NULL,
    Industry ENUM("Tech", "Healthcare", "Finance", "Energy and Utilities", "Transportation", "Education", "Automotive", "Defense", "Construction", "Other") NOT NULL,
    Client_Since DATE NOT NULL,
    UNIQUE(Company_Name),
    PRIMARY KEY(ClientID)
);

## Table 3 (Cases)
CREATE TABLE Cases(
    CaseID INT AUTO_INCREMENT NOT NULL,
    LawyerID CHAR(4) NOT NULL,
    ClientID CHAR(6) NOT NULL,
    Ongoing BOOL NOT NULL,
    Judgement_Date DATE, --can be NULL because case may be ongoing
    Win BOOL, -- can be NULL because case may be ongoing
    PRIMARY KEY(CaseID),
    FOREIGN KEY(LawyerID) REFERENCES Lawyers(LawyerID),
    FOREIGN KEY(ClientID) REFERENCES Clients(ClientID)
);

## Table 4 (Billings)
CREATE TABLE Billings(
    BillID INT AUTO_INCREMENT NOT NULL,
    ClientID CHAR(6) NOT NULL,
    CaseID INT NOT NULL,
    Earnings FLOAT(23) NOT NULL,
    Billed_on DATE NOT NULL,
    PRIMARY KEY(BillID),
    FOREIGN KEY(ClientID) REFERENCES Clients(ClientID),
    FOREIGN KEY(CaseID) REFERENCES Cases(CaseID)
);