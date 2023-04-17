create trigger updateLawsuits
after insert on cases
for each row
begin 
	update clients 
	set Lawsuits = Lawsuits + 1
	where clients.ClientID = new.ClientID;
end;

