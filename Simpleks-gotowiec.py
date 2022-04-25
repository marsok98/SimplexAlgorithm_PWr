import numpy as np
import sys
import matplotlib.pyplot as plt

from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

from tkinter import *
from tkinter.ttk import Combobox
import tkinter
import tkinter.font as font

okno = Tk()
okno.title("Metoda Simplex")
okno.geometry('1400x700')

brak_suma = 0
fx = 0
wektorx = 0

# Funkcja odpowiedzialna za wyświetlenie funkcji celu
def warunki_ograniczen():
    global tab_wier
    global ogr_wier
    global znak
    global kolum_ogr
    global wier_ogr
    global okresl_x
    global wierszfc

    kolum_ogr = Lista_wyboru.get()
    kolum_ogr = int(kolum_ogr)
    wier_ogr = Lista_wyboru_fc.get()
    wier_ogr = int(wier_ogr)
    a = wier_ogr
    opcje_znak = ['=<', '>=']
    znak = []
    ogr_wier = []
    tab_wier = []
    okresl_x = []

    wybierz_znak = Label(Ograniczenia_okno, text="Wybierz znak")
    wybierz_znak.grid(row=1, column=10, sticky="w")
    Ograniczenie = Label(Ograniczenia_okno, text="Wartość")
    Ograniczenie.grid(row=1, column=11, sticky="w")

    for widget in frame2.winfo_children():
        widget.destroy()

    # Funkcja celu
    wierszfc = []
    for l in range(0, wier_ogr):
        if wier_ogr > 0 and wier_ogr <= 10:
            frame2.grid(row=1, column=1 + l)
            pole = Entry(master=frame2, width=3)
            pole.pack(side=LEFT)
            if l == wier_ogr - 1:
                label = Label(master=frame2, text=f"X{l + 1}", bg='light grey')
                label.pack(side=LEFT)
            else:
                label = Label(master=frame2, text=f" X{l + 1} + ", bg='light grey')
                label.pack(side=LEFT)
            wierszfc.append(pole)
        else:
            break

    # Czyszczenie znaków ograniczen i wartosci ograniczen
    for widget in frame_znak.winfo_children():
        widget.destroy()
    for widget in frame_ogr.winfo_children():
        widget.destroy()

    for m in range(0, kolum_ogr):
        # Wybór znaku
        wpisz_znak = Combobox(master=frame_znak, values=opcje_znak, width=5)
        wpisz_znak.grid(row=2 + m, column=0)
        znak.append(wpisz_znak)
        # Okno wpiszania wartosci ograniczenia
        wpisz_ogr = Entry(master=frame_ogr, width=5)
        wpisz_ogr.grid(row=2 + m, column=1)
        ogr_wier.append(wpisz_ogr)

    # Czyszczenie kolejnych X-ów
    for widget in frame.winfo_children():
        widget.destroy()

    for i in range(wier_ogr):
        # Wyswietlenie kolejnych X-ów
        wypisywanie_x = Label(master=frame, text=f"X{i + 1}", width=7)
        wypisywanie_x.grid(row=1, column=i)

    # Czyszczenie tabeli
    for widget in frame1.winfo_children():
        widget.destroy()
    for widget in frame_x.winfo_children():
        widget.destroy()

    for j in range(wier_ogr):
        tab_kol = []
        for k in range(kolum_ogr):
            # Tabela do wpisywania ograniczeń
            wpisz_columna = Entry(master=frame1, width=7)
            wpisz_columna.grid(row=2 + k, column=j)
            tab_kol.append(wpisz_columna)
        tab_wier.append(tab_kol)
        # wybór x nalezy do R lub >=0
        opcje_x = [f'X{j + 1}>=0', f'X{j + 1} ∈ R']
        wybor_x = Combobox(master=frame_x, values=opcje_x, width=5)
        wybor_x.grid(row=0, column=j)
        okresl_x.append(wybor_x)


j = 0


# funkcja sprawdza czy wartosci w ostatniej prawej kolumnie sa >= 0
def kolumna_warun(matrix):
    zero = min(matrix[:-1, -1])
    if zero >= 0:
        return False
    else:
        return True


# funkcja sprawdza czy wartosci w wierszu funkcji celu sa >=0
def wiersz_warun(matrix):
    wiersz = len(matrix[:, 0])
    zero = min(matrix[wiersz - 1, :-1])
    if zero >= 0:
        return False
    else:
        return True


def lokalizacja_kolumna(matrix):
    kolumna = len(matrix[0, :])
    m = min(matrix[:-1, kolumna - 1])
    if m <= 0:
        n = np.where(matrix[:-1, kolumna - 1] == m)[0][0]
    else:
        n = None
    return n


def lokalizacja_wiersz(matrix):
    wiersz = len(matrix[:, 0])
    m = min(matrix[wiersz - 1, :-1])
    if m <= 0:
        n = np.where(matrix[wiersz - 1, :-1] == m)[0][0]
    else:
        n = None
    return n


def lok_element_kolumna(matrix):
    total = []
    r = lokalizacja_kolumna(matrix)
    row = matrix[r, :-1]
    m = min(row)
    c = np.where(row == m)[0][0]
    col = matrix[:-1, c]
    for i, b in zip(col, matrix[:-1, -1]):
        if i != 0 and b / i > 0:
            total.append(b / i)
        else:
            total.append(0)
    element = max(total)
    for t in total:
        if t > 0 and t < element:
            element = t
        else:
            continue

    index = total.index(element)
    return [index, c]


def lok_element_wiersz(matrix):
    if wiersz_warun(matrix):
        total = []
        n = lokalizacja_wiersz(matrix)
        for i, b in zip(matrix[:-1, n], matrix[:-1, -1]):
            if i != 0 and b / i > 0:
                total.append(b / i)
            else:
                total.append(0)
        element = max(total)
        for t in total:
            if t > 0 and t < element:
                element = t
            else:
                continue

        index = total.index(element)
        return [index, n]


def zerowanie(row, col, matrix):
    wiersz = len(matrix[:, 0])
    kolumna = len(matrix[0, :])
    t = np.zeros((wiersz, kolumna))
    pr = matrix[row, :]
    global j
    global wymiartabela
    global brak_suma
    j += 1
    if matrix[row, col] != 0:  # new

        e = 1 / matrix[row, col]
        r = pr * e
        for i in range(len(matrix[:, col])):

            k = matrix[i, :]
            c = matrix[i, col]
            if list(k) == list(pr):
                continue
            else:
                t[i, :] = list(k - r * c)

        t[row, :] = list(r)

        print("Iteracja nr.", j)
        print(t)

        # Brak wybrania zmiennej wchodzącej do bazy
        brak_warun = 0
        for k in range(0, kolum_ogr + 1):
            brak_suma = brak_suma + t[k, 0]
            brak_warun = brak_warun + t[k, 0]

        if j == 5 and (brak_suma / (j - 1)) == brak_warun:
            T.insert(END, "\nBrak wybrania zmiennej wchodzącej do bazy!")
            return False

        # Pusty zbior
        for g in range(0, wymiartabela):
            z = 0
            z_kolumna = 0
            for n in range(0, kolum_ogr + 1):
                if t[n, g] < 0:
                    z += 1
                if z == kolum_ogr + 1:
                    for y in range (0, wymiartabela):
                        if t[n,y] < 0:
                            z_kolumna += 1
                            if z_kolumna == 1:
                                T.insert(END, "\nZbiór rozwiązań jest pusty!")
                                return False

        T.insert(END, f"\nIteracja nr.{j}\n")
        T.insert(END, t)
        return t
    else:
        print('Błąd. Nie można tego przeliczyć.')
        T.insert(END, "\nBłąd. Nie można tego przeliczyć.")


# generowanie tablicy wyników
def tablica_wynik(matrix):
    kolumna = len(matrix[0, :])
    wiersz = len(matrix[:, 0])
    var = kolumna - wiersz - 1
    wynik = []
    for i in range(var):
        wynik.append('x' + str(i + 1))
    return wynik


def maksymalizacja(matrix):
    global ilosc_x
    global wier_ogr
    global tab_x
    global wyswietlwynik


    while kolumna_warun(matrix) == True:
        matrix = zerowanie(lok_element_kolumna(matrix)[0], lok_element_kolumna(matrix)[1], matrix)

    while wiersz_warun(matrix) == True:
        matrix = zerowanie(lok_element_wiersz(matrix)[0], lok_element_wiersz(matrix)[1], matrix)

    kolumna = len(matrix[0, :])
    wiersz = len(matrix[:, 0])
    var = kolumna - wiersz - 1
    i = 0
    val = {}
    wyswietlwynik = np.zeros((1, wier_ogr + ilosc_x))
    for i in range(var):
        col = matrix[:, i]
        s = sum(col)
        m = max(col)
        if float(s) == float(m):
            loc = np.where(col == m)[0][0]
            val[tablica_wynik(matrix)[i]] = matrix[loc, -1]
            wyswietlwynik[0, i] = matrix[loc, -1]
            print(val)
        else:
            val[tablica_wynik(matrix)[i]] = 0
            wyswietlwynik[0, i] = 0
            print(val)

    val['Wartość maksymalizacji funkcji:'] = matrix[-1, -1]
    for k, v in val.items():
        val[k] = round(v, 6)

    r = 0
    for i in range(0, wier_ogr):
        if tab_x[0, i] == 1:
            r = r + 1
            wyswietlwynik[0, i] = wyswietlwynik[0, i] - wyswietlwynik[0, (r + wier_ogr - 1)]

        print("Wartość współczynnika x" + str(i + 1) + " = %.2f" % wyswietlwynik[0, i])
        T.insert(END, "\n")
        T.insert(END, "Wartość współczynnika x" + str(i + 1) + " = %.2f" % wyswietlwynik[0, i])

    for i in range(0, wiersz):
        print(matrix[i, -1])
    print(matrix[-1, -1])
    T.insert(END, "\nWartość maksymalizacji funkcji: ")
    T.insert(END, matrix[-1, -1])

    wynik = str(val)
    print(wynik)


def minimalizacja(matrix):
    global ilosc_x
    global wier_ogr
    global tab_x
    global wyswietlwynik

    matrix[-1, :-2] = [-1 * i for i in matrix[-1, :-2]]
    matrix[-1, -1] = -1 * matrix[-1, -1]
    za_duzo = 0
    while kolumna_warun(matrix) == True:
        matrix = zerowanie(lok_element_kolumna(matrix)[0], lok_element_kolumna(matrix)[1], matrix)
        # To dołożyłem żeby zatrzymać iteracje do nieskończoności
        za_duzo = za_duzo + 1
        if za_duzo == 1000:
            print("Wyznaczono 1000 iteracji")
            break

    while wiersz_warun(matrix) == True:
        matrix = zerowanie(lok_element_wiersz(matrix)[0], lok_element_wiersz(matrix)[1], matrix)

    kolumna = len(matrix[0, :])
    wiersz = len(matrix[:, 0])
    var = kolumna - wiersz - 1
    i = 0
    val = {}
    wyswietlwynik = np.zeros((1, wier_ogr + ilosc_x))
    for i in range(var):
        col = matrix[:, i]
        s = sum(col)
        m = max(col)
        if float(s) == float(m):
            loc = np.where(col == m)[0][0]
            val[tablica_wynik(matrix)[i]] = matrix[loc, -1]
            wyswietlwynik[0, i] = matrix[loc, -1]
        else:
            val[tablica_wynik(matrix)[i]] = 0
            wyswietlwynik[0, i] = 0

        print("Wartość współczynnika x" + str(i + 1) + " = %.2f" % wyswietlwynik[0, i])
    r = 0
    for i in range(0, wier_ogr):
        if tab_x[0, i] == 1:
            r = r + 1
            wyswietlwynik[0, i] = wyswietlwynik[0, i] + (-1) * wyswietlwynik[0, (r + wier_ogr - 1)]

        print("Wartość współczynnika x" + str(i + 1) + " = %.2f" % wyswietlwynik[0, i])
        T.insert(END, "\n")
        T.insert(END, "Wartość współczynnika x" + str(i + 1) + " = %.2f" % wyswietlwynik[0, i])

    val['Wartość minimalizacji funkcji:'] = matrix[-1, -1] * -1
    for k, v in val.items():
        val[k] = round(v, 6)
    print(wyswietlwynik)

    T.insert(END, "\nWartość minimalizacji funkcji: ")
    T.insert(END, matrix[-1, -1] * -1)

    wynik = str(val)
    print(wynik)


def rysowanie_warstwicy(matrix):

    root = tkinter.Tk()
    root.wm_title("Rysowanie warstwicy")
    root.geometry('1000x700')

    global wyswietlwynik
    global wektorx
    global fx
    global kolum_ogr
    global ilosc_x

    tabx = matrix[:-1, 0]
    taby = matrix[:-1, 1]
    wartosc = matrix[:-1, -1]
    znak = wyswietlznak
    fcelu = wyswietlwynik[-1, :]

    print("Rysowanie warstwicy")
    print(fcelu)
    wektorx = np.linspace(-fcelu[-1] - 10, fcelu[-1] + 20)

    fig = Figure(figsize=(5, 5), dpi=100)

    #dzieki temu mozna normalnie sobie ogarniac rysunek w oknie a nie w pycharmie
    a = fig.add_subplot()

    for i in range(0, kolum_ogr):

        fx = (tabx[i] * wektorx - 1 * wartosc[i]) / (-1 * taby[i])

        if znak[0, i] == 1:
            tabx[i] = -1 * tabx[i]
            taby[i] = -1 * taby[i]
            wartosc[i] = -1 * wartosc[i]

        if znak[0, i] == 0:

            if np.sign(taby[i]) == 1:
                a.plot(wektorx, fx, label=r'$' + str(tabx[i]) + 'x +' + str(taby[i]) + 'y' + '\leq' + str(wartosc[i]) + '$')
            else:
                a.plot(wektorx, fx, label=r'$' + str(tabx[i]) + 'x' + str(taby[i]) + 'y' + '\leq' + str(wartosc[i]) + '$')

        else:
            a.plot(wektorx, fx, label=r'$' + str(tabx[i]) + 'x +' + str(taby[i]) + 'y' + '\geq' + str(wartosc[i]) + '$')

        # rysowanie wyniku + zaznaczenie punktu
        a.plot(fcelu[0], fcelu[1], 'ro')


    if fcelu[1] == 0:
        fxwynik = (fcelu[0] * wektorx - 1 * fcelu[-1]) / 1
    else:
        fxwynik = (fcelu[0] * wektorx - 1 * fcelu[-1]) / (-1 * fcelu[1])

    if fcelu[1] < 0:
        a.plot(wektorx, fxwynik, label=r'%.2fx  %.2fy = %.2f ' % (fcelu[0], fcelu[1], fcelu[-1]))
    else:
        a.plot(wektorx, fxwynik, label=r'%.2fx + %.2fy = %.2f ' % (fcelu[0], fcelu[1], fcelu[-1]))


    #tutaj ogarniamy rysunek

    a.text(fcelu[0], fcelu[1], r'(%.2f,%.2f)' % (fcelu[0], fcelu[1]))
    a.legend(bbox_to_anchor=(0.8, 1), loc=2, borderaxespad=0)
    a.set_title("Graficzna metoda simpleks", fontsize=12)
    a.set_ylabel("Y", fontsize=10)
    a.set_xlabel("X", fontsize=10)
    a.grid(True)


    a.spines['left'].set_position('zero')
    a.spines['right'].set_color('none')
    a.spines['bottom'].set_position('zero')
    a.spines['top'].set_color('none')

    canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea.
    canvas.draw()
    canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

    toolbar = NavigationToolbar2Tk(canvas, root)
    toolbar.update()
    canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)





def min_max(m):
    global start
    # minimum
    if m == 1:
        start = 1
    # maximum
    elif m == 2:
        start = 2


def oblicz():
    global tab_wier
    global ogr_wier
    global fun_cel
    global wierszfc
    global znak
    global kolum_ogr
    global wier_ogr
    global wyswietlznak
    global matrix
    global start
    global okresl_x
    global ilosc_x
    global tab_x
    global wymiartabela
    print("\n wartości wpisane funkcji celu")
    fun_cel = []
    for col in wierszfc:
        fun_cel.append(col.get())
    for i in range(0, len(fun_cel)):
        fun_cel[i] = float(fun_cel[i])
    print(fun_cel)

    print("\n wartości wpisane zmiennych ograniczających")
    war_tab = []
    for i in tab_wier:
        war_poj = []
        for wart in i:
            war_poj.append(float(wart.get()))
        war_tab.append(war_poj)
    print(war_tab)

    print("\n wartości wpisane ograniczeń na końcu")
    war_ogr = []
    for col in ogr_wier:
        war_ogr.append(col.get())
    for i in range(0, len(war_ogr)):
        war_ogr[i] = float(war_ogr[i])
    print(war_ogr)

    print("\n wartości znaku")
    wart_znak = []
    for col in znak:
        wart_znak.append(col.get())
    print(wart_znak)

    print("\n wartości okreslające zmienne czy X >= 0 lub X należy do R")
    wyb_okresl_x = []
    for x in okresl_x:
        wyb_okresl_x.append(x.get())
    print(wyb_okresl_x)

    # Tworzenie tablicy SIMPLEX

    iloscfcelu = kolum_ogr

    iloscwarun = wier_ogr
    # Tablica wartości funkcji celu
    tabcelu = np.zeros((1, iloscfcelu))
    tabwarun = np.zeros((iloscwarun, iloscfcelu))
    tabwartosc = np.zeros((1, iloscwarun))

    for i in range(0, iloscfcelu):
        tabcelu[0, i] = fun_cel[i]
    # tablica warunkow
    for i in range(0, iloscwarun):
        for j in range(0, iloscfcelu):
            tabwarun[i, j] = war_tab[j][i]
    # Wartosci ograniczen na koncu
    for i in range(0, iloscwarun):
        tabwartosc[0, i] = war_ogr[i]

    tabznak = np.zeros((1, iloscwarun))

    for i in range(0, iloscwarun):
        if wart_znak[i] == '=<':
            tabznak[0, i] = 0
        elif wart_znak[i] == '>=':
            tabznak[0, i] = 1
        elif wart_znak[i] != '>=' or wart_znak[i] != '=<':
            sys.exit("Wpisz tylko '>=' lub '=<'")

    # obrocenie macierzy
    wyswietlznak = tabznak
    tabznak = np.reshape(tabznak, (iloscwarun, 1))

    # WPROWADZ CZY X JEST >=0 LUB NALEŻY DO R
    tab_x = np.zeros((1, iloscfcelu))
    ilosc_x = 0
    print("Jeśli x jest >= (wpisz 0), gdy nalezy do R (wpisz 1) ")
    for i in range(0, iloscfcelu):
        wp = 0
        if wyb_okresl_x[i] == f'X{i + 1} ∈ R':
            wp = 1
        if wp == 1:
            ilosc_x = ilosc_x + 1
        tab_x[0, i] = wp
    print(tab_x)

    tabcelu_nowe = np.zeros((1, iloscfcelu + ilosc_x))
    tabwarun_nowe = np.zeros((iloscwarun, iloscfcelu + ilosc_x))
    a = 0
    b = 0
    for i in range(0, iloscfcelu):
        tabcelu_nowe[0, i] = tabcelu[0, i]

    for i in range(0, iloscwarun):
        for j in range(0, iloscfcelu):
            tabwarun_nowe[i, j] = tabwarun[i, j]

    for i in range(0, iloscfcelu):
        if tab_x[0, i] == 1:
            tabcelu_nowe[0, a + iloscfcelu] = -tabcelu[0, i]
            a = a + 1

    for i in range(0, iloscwarun):
        b = 0
        for j in range(0, iloscfcelu):
            if tab_x[0, j] == 1:
                tabwarun_nowe[i, b + iloscfcelu] = -tabwarun[i, j]
                b = b + 1

    print("Nowe wartości dla zmiennych wprowadzonych należacych do R")
    print(tabcelu_nowe)
    print(tabwarun_nowe)
    print("\n")

    # obrocenie macierzy
    tabwartosc = np.reshape(tabwartosc, (iloscwarun, 1))

    for i in range(0, iloscwarun):
        if tabznak[i, 0] == 1:
            tabwarun_nowe[i, :] = -1 * tabwarun_nowe[i, :]
            tabwartosc[i, :] = -1 * tabwartosc[i, :]

    # glowna macierz
    wymiartabela = iloscfcelu + iloscwarun + 2 + ilosc_x

    # utworzenie dodatkowej macierzy celu wraz z dodatkowymi zmiennymi
    tabelacelu = np.zeros((1, wymiartabela))
    tabelacelu[0, 0:(iloscfcelu + ilosc_x)] = -1 * tabcelu_nowe
    tabcelu_nowe.astype(float)

    # wektor wyniku
    tabp = np.zeros((iloscwarun + 1, 1))
    tabp[-1, 0] = 1

    # utworzenie dodatkowej macierzy x3, x4, x5 itd - tyle ile warunkow
    tabprzekatna = np.identity(iloscwarun + 1)

    # od teraz wszystkie obliczenia na tablicy matrix
    T.insert(END, "\nPoczątek wyznaczania tabliczy Simpleks:\n")
    matrix = np.zeros((iloscwarun + 1, wymiartabela))
    T.insert(END, f"{matrix}\n")
    print(matrix)
    matrix[-1, 0:wymiartabela] = tabelacelu
    T.insert(END, f"{matrix}\n")
    print(matrix)
    matrix[0:iloscwarun + 1, iloscfcelu + ilosc_x:(iloscfcelu + iloscwarun + 1 + ilosc_x)] = tabprzekatna
    T.insert(END, f"{matrix}\n")
    print(matrix)
    matrix[0:iloscwarun, 0:(iloscfcelu + ilosc_x)] = tabwarun_nowe
    T.insert(END, f"{matrix}\n")
    print(matrix)
    matrix[0:iloscwarun, -1:] = tabwartosc
    T.insert(END, "Tablica Simpleks:\n")
    T.insert(END, matrix)
    print(matrix)

    print("Wprowadzona tabela simpleks:")

    print(matrix)

    # ROZPOCZĘCIE PROGRAMU
    if start == 1:

        print("mimimalizacja")
        minimalizacja(matrix)
    elif start == 2:

        print("maksymalizacja")
        maksymalizacja(matrix)


def rysuj():
    global wier_ogr
    if wier_ogr == 2:
        rysowanie_warstwicy(matrix)


wektorx=0
fx=0

# Ramki

Funkcj_celu_okno = LabelFrame(master=okno, text="Funkcja celu", relief=SUNKEN)
Funkcj_celu_okno.grid(row=2, column=0, columnspan=12, padx=10, pady=10, sticky="w")
Ograniczenia_okno = LabelFrame(master=okno, text="Parametry ograniczające")
Ograniczenia_okno.grid(row=3, column=0, columnspan=12, padx=10, pady=10)
obsluga = LabelFrame(okno, width=1000, height=100)
obsluga.grid(row=0, column=0, columnspan=12, padx=10, pady=10)
Okno_rezultatów = Frame(okno, width=450, height=600, bg='light grey')
Okno_rezultatów.grid(row=0, column=12, rowspan=3, padx=10, pady=10, sticky="s")
Wykres = Frame(okno, width=450, height=340, bg='light grey')
Wykres.grid(row=3, column=12, rowspan=5, padx=10, pady=10, sticky="n")

kolorowe_okno = Canvas(obsluga, width=900, height=100, bg='light grey')
kolorowe_okno.grid(row=0, column=0, columnspan=12, rowspan=3)
kolorowe_okno1 = Canvas(Funkcj_celu_okno, width=900, height=60, bg='light grey')
kolorowe_okno1.grid(row=0, column=0, columnspan=12, rowspan=2)
kolorowe_okno2 = Canvas(Ograniczenia_okno, width=900, height=400, bg='light grey')
kolorowe_okno2.grid(row=0, column=0, columnspan=12, rowspan=13, )

frame_znak = Frame(master=Ograniczenia_okno, bg='light grey')
frame_znak.grid(row=3, column=10, sticky="w")
frame_ogr = Frame(master=Ograniczenia_okno, relief=RAISED, borderwidth=1, bg='light grey')
frame_ogr.grid(row=3, column=11, sticky="w")

frame = Frame(master=Ograniczenia_okno, relief=RAISED, borderwidth=1, bg='light grey')
frame.grid(row=1, column=0, sticky="w")

frame1 = Frame(master=Ograniczenia_okno, relief=RAISED, borderwidth=1, bg='light grey')
frame_x = Frame(master=Ograniczenia_okno, relief=RAISED, borderwidth=1, bg='light grey')
frame1.grid(row=3, column=0, columnspan=10, sticky="w")
frame_x.grid(row=2, column=0, columnspan=10, sticky="w")

frame2 = Frame(master=Funkcj_celu_okno, relief=RAISED, bg='light grey')

# Przełącznik wyboru opcji Maximum Minimum
i = IntVar()

minimum = Radiobutton(obsluga, text="minimum", value=1, variable=i, bg='light grey', command=lambda: min_max(i.get()))
maximum = Radiobutton(obsluga, text="maksimum", value=2, variable=i, bg='light grey', command=lambda: min_max(i.get()))

minimum.grid(row=1, column=4, sticky="nesw")
maximum.grid(row=2, column=4, sticky="nesw")

# Wybór ilości zmiennych ograniczających
Lista_wyboru_fc = Spinbox(obsluga, from_=0, to=10, width=5, command=warunki_ograniczen)
Lista_wyboru_fc.grid(row=1, column=2, sticky="s")

# Wybór liczby ograniczeń
Lista_wyboru = Spinbox(obsluga, from_=0, to=10, width=5, command=warunki_ograniczen)
Lista_wyboru.grid(row=2, column=2, sticky="n")

# Opisy wyświetlane w GUI

Funkcjon = Label(Funkcj_celu_okno, text="Wprowadź wartości zmiennych funkcji celu", bg='light grey', relief=RAISED,
                 width=100)
Funkcjon.grid(row=0, column=0, columnspan=12)
f_c = Label(master=Funkcj_celu_okno, text="f(x) = ", bg='light grey')
f_c.grid(row=1, column=0, sticky="w")
lista_fc = Label(obsluga, text="Wybierz liczbe zmiennych funkcji celu", bg='light grey')
lista = Label(obsluga, text="Wybierz liczbę ograniczeń", bg='light grey')
metoda_simplex = Label(obsluga, text="METODA SIMPLEX", bg='light grey', relief=RAISED, width=100)
lista_fc.grid(row=1, column=0, columnspan=2, sticky="s")
lista.grid(row=2, column=0, columnspan=2, sticky="n")
metoda_simplex.grid(row=0, column=0, columnspan=10, sticky="n")

# Napisy ograniczenia
parametry = Label(Ograniczenia_okno, text="Wprowadz wartości zmiennych ograniczających", width=100, relief=RAISED,
                  bg='light grey')
parametry.grid(row=0, column=0, columnspan=12, sticky="n")
Opis_rysunek = Label(Wykres, text="Rysunek warstwic", bg='light grey', relief=RAISED, width=50)
Opis_rysunek.grid(row=0, column=0, sticky="n")
Opis_wynikow = Label(okno, text="Otrzymane rezultaty", bg='light grey', relief=RAISED, width=50)
Opis_wynikow.grid(row=0, column=12, sticky="n")

# Przyciki
my_font = font.Font(size=30)
oblicz = Button(obsluga, text="Oblicz", width=10, height=2, fg="black", command=oblicz)
wczytaj = Button(obsluga, text="Wczytaj", width=10, height=2, fg="black")
zapisz = Button(obsluga, text="Zapisz", width=10, height=2, fg="black")
wyjscie = Button(obsluga, text="Exit", width=5, height=2, fg="red", command=okno.quit)
wyjscie['font'] = my_font
Rysuj = Button(obsluga, text="Rysuj", width=10, height=2, fg="black", command=rysuj)

oblicz.grid(row=1, column=7, sticky="se")
wczytaj.grid(row=1, column=8, sticky="sw")
zapisz.grid(row=2, column=8, sticky="nw")
wyjscie.grid(row=1, column=9, sticky="w", rowspan=2)
Rysuj.grid(row=2, column=7, sticky="ne")

# Wyświetlanie wyników obliczeń i tabeli
S = Scrollbar(Okno_rezultatów, troughcolor='black')
T = Text(Okno_rezultatów, height=15, width=60, borderwidth=3, bg='light grey')
S.pack(side=RIGHT, fill=Y)
T.pack(side=LEFT, fill=Y)
S.config(command=T.yview)
T.config(yscrollcommand=S.set)

okno.mainloop()
