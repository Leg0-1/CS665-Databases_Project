# An Alternate Approach

Instead of creating many buttons that clutter the application that would each have its own command for CRUD, I decided to make a text box to allow the user to input whatever CRUD commands they wanted.

This provided two extremely useful things:
* Increased flexibility for the user, so the user may essentially input any valid MySQL command and it should alter / query the DB accordingly and successfully.

* It was much simpler to code rather than making a ton of buttons.

## Code (python):
querySet = {"SHOW", "SELECT"}

def submit(inputbox : tk.Text, displaybox : tk.Text):
    command = inputbox.get("1.0", tk.END) # get the command from the user
    sql = connect() # connect to db
    idx = command.find(" ") # find index of " " so that program can determine the command
    commandStart = command[0:idx] # find the command
    if commandStart.upper() in querySet: # if the command is "show" or "select"
        df = pd.read_sql(command, sql) # read the result
        sql.close()
        string = df.to_string() # put it in string format
        # Now put it in the display box:
        displaybox.config(state="normal")
        displaybox.delete("1.0", tk.END)
        displaybox.insert("1.0", string)
        displaybox.config(state="disabled")
    else: # something other than retreiving data
        try:
            # Submit the command:
            cursor = sql.cursor()
            cursor.execute(command)
            sql.commit()
            sql.close()
            # Display whether it worked or not:
            displaybox.config(state="normal")
            displaybox.delete("1.0", tk.END)
            displaybox.insert("1.0", "Transaction completed and committed successfully.")
            displaybox.config(state="disabled")
        except Exception as e:
            displaybox.config(state="normal")
            displaybox.delete("1.0", tk.END)
            displaybox.insert("1.0", f"""An error occurred: {e}""")
            displaybox.config(state="disabled")