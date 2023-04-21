import tkinter as tk

window = tk.Tk()


buttonConfig = {
    "fg": "Black",
    "bg" : "SkyBlue",
    0: "Home",
    1: "Create",
    2: "Read",
    3: "Update",
    4: "Delete",
    "activebg" : "DeepSkyBlue",
    "width" : 15,
    "height" : 5,
    "relief": "raised"
}

for column in range(2):
    window.columnconfigure(column, weight=1, minsize=90)
    for row in range(5):
        window.rowconfigure(row,weight=3, minsize=75)

        frame = tk.Frame(
            master= window,
            width= 500,
            height= 100,
            relief = "flat"
        )
        if column == 0:
            frame.grid(row = row, column=column, padx=5, pady=5)
            Button = tk.Button(
                master=frame,
                fg=buttonConfig["fg"],
                bg=buttonConfig["bg"],
                activebackground= buttonConfig["activebg"],
                relief= buttonConfig["relief"],
                text=buttonConfig[row],
                width= buttonConfig["width"],
                height=buttonConfig["height"]
            )

            Button.bind("<Button-1>")
            Button.pack()
    


window.mainloop()