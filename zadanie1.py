import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
import requests
import os

PLIK_KURSOW = "kursy.csv"
URL_NBP = "https://api.nbp.pl/api/exchangerates/tables/A?format=json"

def pobierz_kursy():
    try:
        odpowiedz = requests.get(URL_NBP)
        odpowiedz.raise_for_status()
        dane = odpowiedz.json()[0]
        kursy = pd.DataFrame(dane['rates'])
        kursy = kursy[['code', 'currency', 'mid']]
        kursy.to_csv(PLIK_KURSOW, index=False)
        return kursy
    except Exception as e:
        print(f"Błąd pobierania danych: {e}")
        if os.path.exists(PLIK_KURSOW):
            return pd.read_csv(PLIK_KURSOW)
        else:
            messagebox.showerror("Błąd", "Brak dostępu do Internetu i zapisanych kursów.")
            exit()

def przelicz():
    try:
        kwota = float(entry_kwota.get())
        waluta_z = combo_z.get()
        waluta_do = combo_do.get()
        kurs_z = kursy.loc[kursy['code'] == waluta_z, 'mid'].values[0]
        kurs_do = kursy.loc[kursy['code'] == waluta_do, 'mid'].values[0]
        wynik = kwota * kurs_z / kurs_do
        label_wynik.config(text=f"{wynik:.3f} {waluta_do}")
    except ValueError:
        messagebox.showerror("Błąd", "Wpisz poprawną kwotę.")
    except Exception as e:
        messagebox.showerror("Błąd", f"Wystąpił błąd: {e}")

# Wczytanie danych
kursy = pobierz_kursy()
waluty = kursy['code'].tolist()

# GUI
root = tk.Tk()
root.title("Przelicznik Walut")
root.geometry("450x250+500+250")
root.resizable(False, False)
root.configure(bg="pink")

frame = tk.Frame(root, padx=9, pady=9)
frame.configure(bg="pink")
frame.pack()

tk.Label(frame, text="Waluta źródłowa:", bg = "pink" , font=("Arial", 16)).grid(row=0, column=0, sticky = "w")
combo_z = ttk.Combobox(frame, values=waluty, font=("Arial", 12))
combo_z.grid(row=0, column=1)
combo_z.set("EUR")

tk.Label(frame, text="Waluta docelowa:", bg = "pink" , font=("Arial", 16)).grid(row=1, column=0, sticky='w')
combo_do = ttk.Combobox(frame, values=waluty, font=("Arial", 12))
combo_do.grid(row=1, column=1)
combo_do.set("USD")

tk.Label(frame, text="Kwota:", bg = "pink" , font=("Arial", 16)).grid(row=2, column=0, sticky='w')
entry_kwota = tk.Entry(frame,font=("Arial", 12))
entry_kwota.grid(row=2, column=1)

tk.Button(frame, text="Przelicz", command=przelicz, bg = "mediumvioletred", font=("Arial", 16) ).grid(row=3, column=0, columnspan=2, pady=10)

label_wynik = tk.Label(frame, text="Wynik pojawi się tutaj", font=("Arial", 16), bg = "pink")
label_wynik.grid(row=4, column=0, columnspan=2)

ttk.Button(frame, text="Zamknij", command=root.quit).grid(row=5, column=0, columnspan=2, pady=5)

root.mainloop()
