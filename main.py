import tkinter as tk
import math
from tkinter.ttk import Combobox


root = tk.Tk()
root.title("Kabelweerstand")
root.geometry("500x500")
root.resizable(0, 0)

tf = ("Arial", 13, "bold")
bg_color = "#C69012"
button_color = "#800000"




def bereken_kabelweerstand():
    try:
        printLabel = tk.Label(root, text=(str(kabellengte.get()) + str(kabeldikte.get()) + str(temperatuur.get()) + str(w.get())), font=tf, bg=bg_color, width=40)
        printLabel.pack()

    except :
        print("fout")




#label kabellengte
label_instructie = tk.Label(root, text="kabellengte in m", font=tf, bg=bg_color)
label_instructie.pack(pady=10)
#invoerveld kabellengte
kabellengte = tk.Entry(root, font=tf, width=10)
kabellengte.pack(pady=7)

#label kabeldikte
label_instructie = tk.Label(root, text="kabeldikte in mm²", font=tf, bg=bg_color)
label_instructie.pack(pady=10)
#invoerveld kabeldikte
kabeldikte = tk.Entry(root, font=tf, width=10)
kabeldikte.pack(pady=7)

#label omgevingstemperatuur
label_instructie = tk.Label(root, text="omgevingstemperatuur in  °C", font=tf, bg=bg_color)
label_instructie.pack(pady=10)
#invoerveld omgevingstemperatuur
temperatuur = tk.Entry(root, font=tf, width=10)
temperatuur.pack(pady=7)

#label kabelmateriaal
label_instructie = tk.Label(root, text="Materiaalselectie", font=tf, bg=bg_color)
label_instructie.pack(pady=10)
#selectieveld kabelmateriaal
choices = ['Koper', 'Aluminium', 'goud', 'zilver' ]
variable = tk.StringVar(root)

w = Combobox(root, values = choices)
w.pack()

#knop berekeningen uitvoeren
button_berekenen = tk.Button(root, text="bereken kabelweerstand",command=bereken_kabelweerstand, font=tf, bg=button_color)
button_berekenen.pack(pady=40)

#uitkomst weergeven in app

root.mainloop()



#kabel-lengte
#kabel-dikte
#kabel-materiaal
#omgevings-temperatuur