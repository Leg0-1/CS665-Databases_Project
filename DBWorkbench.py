import tkinter as tk
import mysql.connector as mysql
import pandas as pd


# Back-end =========================================================================================
def connect():
  LawyerDB = mysql.connect(
    host="localhost",
    user="root",
    password="project.Password01", # Just bc it's a password I'll never use doesn't mean I shouldn't make it strong
    database = 'LawyerDB'
  )
  return LawyerDB

def SelectAll(Table, inputbox, displaybox):
    command = f"""SELECT * FROM {Table};"""
    inputbox.delete("1.0", tk.END)
    inputbox.insert("1.0", command)
    sql = connect()
    df = pd.read_sql(command, sql)
    string = df.to_string()
    displaybox.config(state="normal")
    displaybox.delete("1.0", tk.END)
    displaybox.insert("1.0", string)
    displaybox.config(state="disabled")

def predefinedJoinLC(inputbox, displaybox): # Joins Lawyers and Cases
    sql = connect()
    command = f"""SELECT Lawyers.LawyerID, FirstName, LastName, CaseID
FROM Lawyers
JOIN Cases ON Lawyers.LawyerID = Cases.LawyerID
WHERE Ongoing = True;
    """
    inputbox.delete("1.0", tk.END)
    inputbox.insert("1.0", command)
    df = pd.read_sql(command, sql)
    string = df.to_string()
    displaybox.config(state="normal")
    displaybox.delete("1.0", tk.END)
    displaybox.insert("1.0", string)
    displaybox.config(state="disabled")

def predefinedJoinCB(inputbox, displaybox): # Joins Clients and Billings
    sql = connect()
    command = f"""SELECT Clients.ClientID, Company_Name, Industry, Earnings, Billed_On
FROM Clients
JOIN Billings ON Clients.ClientID = Billings.ClientID
ORDER BY Billed_On DESC;
    """
    inputbox.delete("1.0", tk.END)
    inputbox.insert("1.0", command)
    df = pd.read_sql(command, sql)
    string = df.to_string()
    displaybox.config(state="normal")
    displaybox.delete("1.0", tk.END)
    displaybox.insert("1.0", string)
    displaybox.config(state="disabled")



querySet = {"SHOW", "SELECT"}

def submit(inputbox : tk.Text, displaybox : tk.Text):
    command = inputbox.get("1.0", tk.END) # get the command from the user
    sql = connect() # connect to db
    idx = command.find(" ") # find index of " " so that program can determine the command
    commandStart = command[0:idx] # find the command
    if commandStart.upper() in querySet: # if the command is "show" or "select"
        df = pd.read_sql(command, sql) # query the db and put it in a dataframe
        sql.close() # don't need to connect any longer
        string = df.to_string() # put dataframe in string format
        # Now put result in the display box:
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
        
    

# GUI frontend (more or less) =====================================================================
# Configs ---------------------------------------
buttonConfig = {
    "fg": "Black",
    "bg" : "SkyBlue",
    "activebg" : "DeepSkyBlue",
    "width" : 15,
    "height" : 5,
    "relief": "raised"
}

# -----------------------------------------------

window = tk.Tk()

window.columnconfigure(1, weight=1, minsize=150)
# Output box: ------------------------------------------------------------
frame = tk.Frame(
            master= window,
            relief = "flat",
            borderwidth=1
        )
frame.grid(row=3, column = 1, rowspan = 4)
Outputlabel = tk.Label(
    master=frame,
    text="Output:"
)
Outputbox = tk.Text(
    master=frame,
    width = 80,
    height = 15,
    state= "disabled"
)
Outputlabel.pack(side="top")
Outputbox.pack()


# Input box: -------------------------------------------------------------
frame = tk.Frame(
            master= window,
            relief = "flat",
            borderwidth=1,
        )
frame.grid(row=0, column = 1, rowspan = 2)
Inputlabel = tk.Label(
    master=frame,
    text="Input your MySQL commands here:"
)
Inputbox = tk.Text(
    master = frame,
    width= 80,
    height= 15
    )
submitbutton = tk.Button(
        master=frame,
        fg=buttonConfig["fg"],
        bg=buttonConfig["bg"],
        activebackground= buttonConfig["activebg"],
        relief= buttonConfig["relief"],
        text="Submit",
        width= 10,
        height=1,
        command = lambda: submit(Inputbox, Outputbox)
)
Inputlabel.pack(side="top")
Inputbox.pack()
submitbutton.pack(side="bottom")

Inputbox.insert("1.0", """
                    Welcome to Aaron Isaacs' CS665 Project 1!
    I recommend "show tables" to start in order to get familiar with the tables.
    From there, "select * from <table>" is a great way to learn columns as well!
    When you're ready, delete the text in this box and get started!
""")

# Buttons: ---------------------------------------------------------------
DefaultConfig = {
    1 : ["Select Lawyers", lambda : SelectAll("Lawyers", Inputbox, Outputbox)],
    2 : ["Select Cases", lambda : SelectAll("Cases", Inputbox, Outputbox)],
    3 : ["Join Lawyers\nand Cases", lambda : predefinedJoinLC(Inputbox, Outputbox)],
    4 : ["Join Clients\nand Billings", lambda : predefinedJoinCB(Inputbox, Outputbox)],
}
window.columnconfigure(0, weight=1, minsize=90)
window.rowconfigure(0,weight=1, minsize=75)

frame = tk.Frame(
    master= window,
    width= 500,
    height= 100,
    relief = "flat"
)
frame.grid(row = 0, column=0, padx=5,pady=5)
label = tk.Label(master = frame, borderwidth=1, text = "Predefined SQL Statements")
label.pack()

for row in range(1,5):
    window.rowconfigure(0,weight=1, minsize=75)

    frame = tk.Frame(
        master= window,
        width= 500,
        height= 100,
        relief = "flat"
    )

    frame.grid(row = row, column=0, padx=5, pady=5)
    Button = tk.Button(
        master=frame,
        fg=buttonConfig["fg"],
        bg=buttonConfig["bg"],
        activebackground= buttonConfig["activebg"],
        relief= buttonConfig["relief"],
        text=DefaultConfig[row][0],
        width= buttonConfig["width"],
        height=buttonConfig["height"],
        command=DefaultConfig[row][1]
    )
    
    Button.pack()



window.mainloop()