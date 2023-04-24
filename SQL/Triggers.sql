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
create trigger OngoingCase
before update on cases
for each row
begin
	if new.ongoing = false and (new.Judgement_date is null or new.win is NULL) then 
		signal sqlstate "45000"
			set message_text = "Judgement_date and Win cannot be NULL if Ongoing is False";
	end if;
end;

create trigger OngoingCase2
before insert on cases
for each row
begin
	if new.ongoing = false and (new.Judgement_date is null or new.win is NULL) then 
		signal sqlstate "45000"
			set message_text = "Judgement_date and Win cannot be NULL if Ongoing is False";
	end if;
end;

-- Last trigger: if a new client is signed, create a record in the billings table for their signing

create trigger NewClient
after insert on Clients
for each row 
begin
	insert billings (ClientID, Earnings, Billed_on, Reason)
	values (new.ClientID, 100000, CURRENT_DATE, "Signed a Client");
end;
