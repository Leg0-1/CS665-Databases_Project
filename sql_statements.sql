CREATE TABLE Lawyers(
    LawyerID char(4) PRIMARY KEY,
    LastName varchar(255),
    FirstName varchar(255)
)

CREATE TABLE Clients(
    ClientID Char(6) PRIMARY KEY,
    Company_Name varchar(255)
)

CREATE TABLE Billings(
    BillID int AUTO_INCREMENT PRIMARY KEY,
    CaseID int FOREIGN KEY REFERENCES Cases(CaseID),
    ClientID char(6) FOREIGN KEY REFERENCES Clients(ClientID),
    Earnings float(23),
    Billed_on DATE
)