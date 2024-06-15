from tkinter import *
from tkinter.ttk import *

root = Tk()
root.title('Kalkulatori')
root.geometry('450x300')
naslov = Label(root, text = 'ГЛАВНИ МЕНИ')
naslov.pack()

def Aktivna():
    aktivna = Toplevel(root)
    aktivna.title('Калкулатор активне материје')
    aktivna.geometry('500x350')

    Legenda = Label(aktivna, text = f'm - Измерена маса\nC - Чистоћа стандарда\nV - Запремина суда')
    Legenda.pack()

    aktiv_m_l = Label(aktivna, text = 'm =')
    aktiv_m_l.place(x = 15, y = 50)
    aktiv_g_l = Label(aktivna, text = 'g')
    aktiv_g_l.place(x = 173, y = 50)
    aktiv_m_tb = Entry(aktivna)
    aktiv_m_tb.config(state = NORMAL)
    aktiv_m_tb.place(x = 45, y = 50)

    aktiv_c_l = Label(aktivna, text = 'C =')
    aktiv_c_l.place(x = 15, y = 75)
    aktiv_pos_l = Label(aktivna, text = '%')
    aktiv_pos_l.place(x = 173, y = 75)
    aktiv_c_tb = Entry(aktivna)
    aktiv_c_tb.config(state = NORMAL)
    aktiv_c_tb.place(x = 45, y = 75)

    aktiv_v_l = Label(aktivna, text = 'V =')
    aktiv_v_l.place(x = 15, y = 100)
    aktiv_ml_l = Label(aktivna, text = 'ml')
    aktiv_ml_l.place(x = 173, y = 100)
    aktiv_v_tb = Entry(aktivna)
    aktiv_v_tb.config(state = NORMAL)
    aktiv_v_tb.place(x = 45, y = 100)

    def racunanje_aktiv():
        a = aktiv_m_tb.get()
        b = aktiv_c_tb.get()
        c = aktiv_v_tb.get()
        a_con = float(a)
        b_con = float(b)
        c_con = int(c)
        resenje_aktiv = (round((((a_con) * (b_con)) * 10) / c_con, 4))
        rezultat_aktiv = round(resenje_aktiv * 1000, 2)
        rezultat_aktiv_l = Label(aktivna, text = f'Концентрација активне материје је: {rezultat_aktiv} mg/l.', font = ('Arial', 12, 'bold'))
        rezultat_aktiv_l.place(x = 90, y = 200)

    def brisanje_aktiv():
        aktiv_m_tb.delete(0, END)
        aktiv_c_tb.delete(0, END)
        aktiv_v_tb.delete(0, END)
    
    dug_rac_akt = Button(aktivna, text = 'ИЗРАЧУНАЈ', command = racunanje_aktiv)
    dug_rac_akt.place(x = 27, y = 130)
    dug_clr_akt = Button(aktivna, text = 'CE', command = brisanje_aktiv)
    dug_clr_akt.place(x = 105, y = 130)

Dugme = Button(root, text = 'Активна материја', command = Aktivna)
Dugme.place(x = 15, y = 50)



mainloop()