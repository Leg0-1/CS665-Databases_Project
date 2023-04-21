create trigger updateLawsuits
after insert on cases
for each row
begin 
	update clients 
	set Lawsuits = Lawsuits + 1
	where clients.ClientID = new.ClientID;
end;
-- This trigger updates the client's lawsuit number whenever a new case with the same clientID is inserted
-- the following trigger is very similar, but it decreases number of lawsuits if a case is deleted
 create trigger updateLawsuits2
 after delete on cases
 for each row
 begin
	update clients
	set Lawsuits = Lawsuits - 1
	where clients.ClientID = old.ClientID;
end;


-- Next set of triggers, these are for the cases table with regards to if the case is ongoing or not. ###########################


