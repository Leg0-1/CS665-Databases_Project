# INSERT commands to initially populate the tables:

## Lawyers Table
-- INSERT commands:
-- Lawyers Table:
INSERT INTO Lawyers(LawyerID, LastName, FirstName, Member_Of_Bar_Since)
VALUES ("L001", "Pearson", "Jessica", 1988);

INSERT INTO Lawyers(LawyerID, LastName, FirstName, Member_Of_Bar_Since)
VALUES ("L002", "Specter", "Harvey", 1991);

INSERT INTO Lawyers(LawyerID, LastName, FirstName, Member_Of_Bar_Since)
VALUES ("L003", "Litt", "Louis", 1991);

INSERT INTO Lawyers(LawyerID, LastName, FirstName, Member_Of_Bar_Since)
VALUES ("L004", "Ross", "Mike", 2007);

INSERT INTO Lawyers(LawyerID, LastName, FirstName, Member_Of_Bar_Since)
VALUES ("L005", "Bennet", "Katrina", 2003);

## Clients Table
-- Clients Table
INSERT INTO Clients(ClientID, Company_Name, Industry, Client_Since)
VALUES ("CLI001", "McKernon Motors", "Automotive", 1999);

INSERT INTO Clients(ClientID, Company_Name, Industry, Client_Since)
VALUES ("CLI002", "Pfizer", "Healthcare", 2005);

INSERT INTO Clients(ClientID, Company_Name, Industry, Client_Since)
VALUES ("CLI003", "Evergy", "Energy and Utilities", 2009);

INSERT INTO Clients(ClientID, Company_Name, Industry, Client_Since)
VALUES ("CLI004", "American Airlines", "Transportation", 2010);

INSERT INTO Clients(ClientID, Company_Name, Industry, Client_Since)
VALUES ("CLI005", "Samsung", "Tech", 2015);

## Cases Table
-- Cases Table
INSERT INTO Cases(LawyerID, ClientID, Ongoing, Judgement_Date, Win) -- CaseID = 1
VALUES("L002", "CLI001", 0, "2000-05-03", 1);

INSERT INTO Cases(LawyerID, ClientID, Ongoing, Judgement_Date, Win) -- CaseID = 2
VALUES("L003", "CLI004", 0, "2010-03-15", 1);

INSERT INTO Cases(LawyerID, ClientID, Ongoing, Judgement_Date, Win) -- CaseID = 3
VALUES("L004", "CLI005", 0, "2016-12-02", 1);

INSERT INTO Cases(LawyerID, ClientID, Ongoing, Judgement_Date, Win) -- CaseID = 4
VALUES("L003", "CLI002", 0, "2022-09-13", 0);

INSERT INTO Cases(LawyerID, ClientID, Ongoing, Judgement_Date, Win) -- CaseID = 5
VALUES("L005", "CLI005", 1, NULL, NULL);

## Billings Table
-- Billings Table: 
-- There will be a bill for a signing on fee ($100,000.00) and a bill per case (variable on the case), so there will initially by 10 records in this table.
-- Add a trigger later that says you cannot bill for a case that a client that does not exist
-- Add another trigger saying whenever a client is signed on, make another record on the billings table about their sign on fee.
INSERT INTO Billings(ClientID, Earnings, Billed_on, Reason) -- Bill ID = 1
VALUES("CLI001", 100000.00, "1999-11-17", "Signed a Client"); -- Earnings in US Dollar, Signed a Client

INSERT INTO Billings(ClientID, Earnings, Billed_on, Reason) -- Bill ID = 2
VALUES("CLI001", 300272.88, "2000-05-17", "Case");

INSERT INTO Billings(ClientID, Earnings, Billed_on, Reason) -- Bill ID = 3
VALUES("CLI002", 100000.00,"2005-02-10", "Signed a Client");

INSERT INTO Billings(ClientID, Earnings, Billed_on, Reason) -- Bill ID = 4
VALUES("CLI003", 100000.00, "2009-09-23", "Signed a Client");

INSERT INTO Billings(ClientID, Earnings, Billed_on, Reason) -- Bill ID = 5
VALUES("CLI004", 100000.00, "2010-01-07", "Signed a Client");

INSERT INTO Billings(ClientID, Earnings, Billed_on, Reason) -- Bill ID = 6
VALUES("CLI004", 525047.36, "2010-03-29", "Case"); 

INSERT INTO Billings(ClientID, Earnings, Billed_on, Reason) -- Bill ID = 7
VALUES("CLI005", 100000.00, "2015-04-29", "Signed a Client");

INSERT INTO Billings(ClientID, Earnings, Billed_on, Reason) -- Bill ID = 8
VALUES("CLI005", 305855.56, "2016-12-16", "Case");

INSERT INTO Billings(ClientID, Earnings, Billed_on, Reason) -- Bill ID = 9
VALUES("CLI005", 70000.00, "2022-09-27", "Case");