# Create Table Statements


## Lawyers Table
CREATE TABLE Lawyers(
    LawyerID CHAR(4) NOT NULL, -- L001, L002, L003, ...
    LastName VARCHAR(255) NOT NULL,
    FirstName VARCHAR(255) NOT NULL,
    Member_Of_Bar_Since YEAR NOT NULL, -- Cannot be uniquely determined by someone's name
    PRIMARY KEY(LawyerID)
);

## Clients Table

CREATE TABLE Clients(
    ClientID CHAR(6) NOT NULL,
    Company_Name VARCHAR(255) NOT NULL,
    Industry ENUM("Tech", "Healthcare", "Finance", "Energy and Utilities", "Transportation", "Education", "Automotive", "Defense", "Construction", "Other") NOT NULL,
    Lawsuits INT(255),
    UNIQUE(Company_Name),
    PRIMARY KEY(ClientID)
);
-- Create a Trigger that says whenever a new case is filed with a particular clientID, it must update that client's Lawsuit number

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
-- Create a Trigger that says if the ongoing bool is 1, Judgement_Date and Win are allowed to be NULL, otherwise if ongoing bool is 0, Judgement_Date and Win columns are NOT NULL

## Billings Table
CREATE TABLE Billings(
    BillID INT(255) AUTO_INCREMENT NOT NULL,
    ClientID CHAR(6) NOT NULL,
    Earnings DECIMAL(15,2) NOT NULL,
    Billed_on DATE NOT NULL,
    Reason VARCHAR(255) NOT NULL,
    PRIMARY KEY(BillID),
    FOREIGN KEY(ClientID) REFERENCES Clients(ClientID)
);

-- There will be a bill for a signing on fee ($100,000.00) and a bill per case (variable on the case), so there will initially 9 records in this table.
-- Add a trigger later that says you cannot bill for a case that a client that does not exist
-- Add another trigger saying whenever a client is signed on, make another record on the billings table about their sign on fee.