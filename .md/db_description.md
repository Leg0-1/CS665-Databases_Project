# CS 665 Project 1
## Description
This application is designed to rely a little more on user's knowledge of SQL to implement CRUD. The database this application uses is a database made for a mock Lawyer firm. There are four tables to look through, Lawyers, Clients, Cases, and Billings. The application contains four buttons that handle predefined SQL commands, two for just selecting all attributes from Lawyers and Cases, and two to perform JOIN commands. One for joining Lawyers with Cases, and another for joining Clients and Billings.

## Tables

### Lawyers
There are five lawyers in the lawyers table and the table has four attributes: LawyerID, LastName, FirstName, and Member_Of_Bar_Since. The first three are rather self explanitory, but the fourth one just indicates the year of which that lawyer became a member of the bar.
#### FD and Normalized form
In an attempt to keep all the tables in normalized form, I have attempted to keep fundamental dependencies to a minimum, where all attributes are dependent on the primary key. 

In the lawyers table, the first and last names cannot be uniquely determined by each other, as two lawyers might have the same last name, or more likely two lawyers might have the same first name. And while it may seem like you could determine when someone entered the bar by their name, I would argue that being a member of the bar cannot be uniquely determined by a full name alone. While unlikely, it is possible for two people of the same name to be members of the bar.

So, since no non-key attributes are depending on any partial primary keys or other non-key attributes, I believe the lawyers table qualifies under 3NF.

#### Constraints
LawyerID is the primary key, thus NOT NULL and UNIQUE.
LastName and FirstName are both NOT NULL but also not UNIQUE because several people with the same name could be lawyers at this firm.
Member_Of_Bar attribute is also NOT NULL as you must be a member of the bar in order to be a lawyer, but not unique because several lawyers could be entered into the bar in the same year.

### Clients
The clients table holds the information of the clients of the firm. The attributes of the table are ClientID, Company_Name, Industry, and Lawsuits. Industry is the main industry of the company, and lawsuits is the number of lawsuits this company has had.
#### FD and Normalized Form
To maintain the table in 3rd normalized form, the company name connot uniquely determine what industry its in because a company can be in multiple industries at once. And while it may seem like the company name determines how many lawsuits it has, the number of lawsuits it has is can be determined by any additional cases with the corresponding ClientID.

#### Constraints
ClientID is primary key so it is NOT NULL and UNIQUE.
Company_Name is NOT NULL and also UNIQUE because two companies with the same name is unlikely and a lawsuit waiting to happen.
Industry is NOT NULL but not UNIQUE either. Industry is of type ENUM as there is a big list of industries but not just anything can be an industry.
Lawsuits is NOT NULL but not UNIQUE either as many companies could have the same number of lawsuits.

### Cases
The cases table contains information about the cases that the firm has handled. The attributes of this table are CaseID, LawyerID, ClientID, Ongoing, Judgement_Date, and Win. LawyerID and ClientID are foreign keys for the Lawyers table and the Clients table respectively. Lawyers can have multiple cases, and Clients can have multiple cases, so neither are unique in this table as several lawyers could be working with the same client on separate cases. Ongoing is a boolean that coorelates to if the case is currently ongoing or if it is closed. Judgement date is the date in which a case has been closed. Win is a boolean value based on if a case was won or if a case was lost.

#### FD and Normalized Form
In an attempt to keep the table in 3rd Normalized Form, I've attempted to keep each attribute independent one another. LawyerID cannot be determined by ClientID and ClientID cannot be determined by LawyerID, likewise neither of them can determine or be determined by Ongoing, Judgement Date, and Win. Likewise whether a date is ongoing or not cannot determine the judgement date or the outcome of the case. And finally, judgement date and the outcome of the case cannot be determined one another because you cannot determine when a case was closed based solely on its outcome, and you cannot determine the outcome of a case solely on the date in which the case was closed.

#### Constraints
CaseID is the primary key so it is NOT NULL and UNIQUE.
LawyerID is a foreign key to the Lawyers table, so NOT NULL but not UNIQUE either.
ClientID is a foreign key to the Clients table, so NOT NULL but not UNIQUE either.
Ongoing is a boolean value that is NOT NULL and definitely not UNIQUE considering it's a 1 or 0 value.
Judgement_Date is a date value that can be NULL and not UNIQUE because if a case is ongoing there is no set judgement date because the case has not yet been closed.
Win is a boolean value as well, but it can be NULL and not UNIQUE because the outcome of a case cannot be determined if the case is currently ongoing.

### Billings
The billings table contains the information for earnings and how much money the firm earned from who. The attributes of the table are BillID, ClientID, Earnings, Billed_On, and Reasons. ClientID cannot determine Earnings because earnings don't uniquely depend on the client, but also the case. ClientID also cannot determine the date in which the bill was paid and it also cannot determine the reason why it was paid, likewise neither can determine the clientID as well. The amount of the bill cannot be determined by the reason it was paid and likewise neither can determine when it was paid.

#### Constraints
BillID is a primary key so NOT NULL and also UNIQUE,
ClientID is a foreign key of the Clients table, so NOT NULL because a client must be the source of the money and not UNIQUE because ideally a client will pay us a lot of money.
Earnings is NOT NULL and not UNIQUE because the client must pay something and sometimes they might pay the same or another company might pay the same.
Billed_On is when the bill was sent to the client and is NOT NULL and not UNIQUE as we could bill several clients in the same day.
Reasons is NOT NULL and type ENUM as the reason a client could be paying is because we just signed a client or we represented them in a case.

## Sample Data
### Lawyers
LawyerID LastName FirstName  Member_Of_Bar_Since
  L001  Pearson   Jessica                 1988
  L002  Specter    Harvey                 1991

### Clients
ClientID       Company_Name              Industry  Lawsuits
  CLI001    McKernon Motors            Automotive         2
  CLI002             Pfizer            Healthcare        14

### Cases
CaseID LawyerID ClientID  Ongoing Judgement_Date  Win
     1     L002   CLI001        0     2000-05-03  1.0
     2     L003   CLI004        0     2010-03-15  1.0

### Billings
BillID ClientID   Earnings   Billed_on           Reason
    1   CLI001  100000.00  1999-11-17  Signed a Client
    2   CLI001  300272.88  2000-05-17             Case