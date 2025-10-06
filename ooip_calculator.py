# OOIP Calculator by Siddharth Gorai

# Rs -> Solution Gas-Oil Ratio (scf/STB)
# Rp -> Producing Gas-Oil Ratio (scf/STB)
# Np -> Cumulative Oil Production (STB)
# Wp -> Cumulative Water Production (STB)
# P  -> Reservoir Pressure (psia)
# Bo -> Oil Formation Volume Factor (RB/STB)
# Bg -> Gas Formation Volume Factor (RB/scf)
# Bw -> Water Formation Volume Factor (RB/STB)
# Boi-> Initial Oil Formation Volume Factor (RB/STB)
# Bgi-> Initial Gas Formation Volume Factor (RB/scf)
# Rsi-> Initial Solution Gas-Oil Ratio (scf/STB)  , Formation GOR
# Cf -> Formation Compressibility (1/psia)
# Cw -> Water Compressibility (1/psia)
# Swi-> Initial Water Saturation (fraction)
# Pi -> Initial Reservoir Pressure (psia)
# m  -> Ratio of Gas Cap Volume to Initial Oil Volume (fraction)
# We -> Cumulative Excess Water Injection (STB)
# Z  -> Gas Deviation Factor (dimensionless)

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from tkinter import Tk, Button, Label, filedialog, messagebox, Entry, ttk
import os 

def show_csv_files():
    files = []
    for i in os.listdir():
        if i.endswith(".csv"):
            files.append(i)
    return files

def calc_ooip(df):
    def calc_row(row):
        Np, Rp, Rs, Wp, P, Temp = row['Np'], row['Rp'], row['Rs'], row['Wp'], row['P (psia)'], row["Temp (°R)"]

        Bg = 0.0054 * Z * Temp / P 
        Eo = (Bo - Boi) + Bg * (Rsi - Rs)
        Eg = Boi * (Bg / Bgi - 1)
        Er = Boi * (Cf + Cw * Swi / (1 - Swi)) * (Pi - P)
        Enet = Eo + m * Eg + (1 + m) * Er + We

        F = Np * Bo + Np * (Rp - Rs) * Bg + Wp * Bw
        return pd.Series({"Enet": Enet, "F": F})

    df[['Enet', 'F']] = df.apply(calc_row, axis=1)
    slope, intercept = np.polyfit(df['Enet'], df['F'], 1)
    return df, slope, intercept


def plot_FvsEnet(F, Enet, slope, intercept):
    OOIP = slope
    plt.figure(figsize=(10,5))
    plt.plot(Enet, F, marker='o', label='F vs Enet')

    x_vals = np.array(Enet)
    y_vals = slope * x_vals + intercept
    plt.plot(x_vals, y_vals, color='red', linestyle='--', label=f'Regression Line\nSlope=OOIP={OOIP:.2f} STB')

    mid_idx = len(x_vals)//2
    plt.text(x_vals[mid_idx], y_vals[mid_idx], f'Slope (OOIP)={OOIP:.2f} STB', 
            fontsize=10, color='red', rotation=0, bbox=dict(facecolor='white', alpha=0.7))

    plt.xlabel('Enet')
    plt.ylabel('F')
    plt.title('Material Balance: F vs Enet')
    plt.grid(True)
    plt.legend()
    plt.show()


def submit():
    global Boi, Bo, Bgi, Bw, Rsi, Cf, Cw, Swi, Pi, m, We, Z

    try:
        for key in default_values:
            globals()[key] = float(entries[key].get())
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values for all properties.")
        return

    csv_file = data_combobox.get()
    if csv_file == "Select any one" or not os.path.exists(csv_file):
        messagebox.showerror("Input Error", "Please select a valid CSV file.")
        return

    df = pd.read_csv(csv_file)

    df_calculated, slope, intercept = calc_ooip(df)
    plot_FvsEnet(df_calculated["F"], df_calculated["Enet"], slope, intercept)


default_values = {
    "Boi": 1.1,
    "Bo": 1.2, 
    "Bgi": 0.006,
    "Bw": 1.0,
    "Rsi": 500,
    "Cf": 3e-6,
    "Cw": 3e-6,
    "Swi": 0.25,
    "Pi": 3000,
    "m": 0.2,
    "We": 0,
    "Z": 1.0,  
}

entries = {}

win = Tk()
win.title("OOIP Calculator")
win.resizable(False, False)

head_label = Label(win,text="OOIP Calculator from Material Balance",font=("Arial",10,"bold"))
head_label.grid(row=0,column=0,columnspan=4, padx=10, pady=10)

sub_head_label = Label(win,text="Enter Reservoir Properties",font=("Arial",9,"bold"))
sub_head_label.grid(row=1,column=0,columnspan=2,sticky="w")

for i, (key, val) in enumerate(default_values.items(), start=2):

    Label(win, text=key, font=("Arial", 12)).grid(row=i, column=0, pady=5, sticky="w")

    entry = Entry(win, font=("Arial", 12), width=10)
    entry.insert(0, str(val))
    entry.grid(row=i, column=1, pady=5)

    entries[key] = entry


data_label =  Label(win,text="Select CSV datafile")
data_label.grid(row=(len(default_values)//2),column=2)

data_options = show_csv_files()
data_combobox = ttk.Combobox(win, values=data_options, state="readonly")
data_combobox.set("Select any one") 
data_combobox.grid(row=(len(default_values)//2)+1, column=2)

submit_button = Button(win, text="Calculate OOIP", font=("Arial", 12, "bold"), command=submit)
submit_button.grid(row=(len(default_values)//2)+2, column=2, padx=20, pady=5, sticky="n")


win.mainloop()


