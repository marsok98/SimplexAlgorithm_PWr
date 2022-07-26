Projekt na zaliczenie Teoria i Metody Optymalizacji - Studia Magisterskie - Automatyka i Robotyka




Postać gdy ograniczenia są mniejszościowe:
-------------------------------------------
Ponizsze ograniczenia wraz z funkcja celu:
   x1 + x2     <= 5
  -x1 + x2     <= 0
  6x1 + 2x2    <= 21

 maxx0 = 2x1 + x2

 Zapisujemy do postaci tablicy simplexowej:

                   x1      x2
   x0      0      -2      -1
   x3      5       1       1
   x4      0      -1       1
   x5     21       6       2

Lub w formie już skroconej
 A = [[0,-2,-1],[5,1,1],[0,-1,1],[21,6,2]]

Co wazne funkcja celu jest z wspolczynnikami ujemnymi
Wpisywana do tablicy simplexowej
=====================================================

Postać gdy ograniczenia są wiekszosciowe:
-----------------------------------------
Tam gdzie jest ograniczenie wiekszosciowe, nalezy wpisac do tablicy simplexowej ze zmienionymi wszystkimi
znakami za przeciwne.

  2x1 + 1x2     >= 2
  -x1 +  x2     <= 3
  1x1 + 1x2     <= 6

maxx0 = 1x1 + 6x2

          x0       x1      x2
   x0      0      -1      -6
   x3     -2      -2      -1
   x4      3      -1       1
   x5      6       1       1
=====================================================

Kroki rozwiazan simplexa (dwufazowa metoda)
-------------------------------------------
1. Zapis danych do tablicy simplexowej.

2. Sprawdzenie przypadku z ktorym mamy doczynienia (metoda: check_the_case)
    a) Sprawdzenie dopuszczalnosci rozwiazania początkowego ustawienia tablicy Simplex (czy jesteśmy w jednym z wierzchołkow)

        aa) Jeśli w 0th kolumnie pojawi sie jakas wartosc ujemna, znaczy ze rozwiazanie jest niedopuszczalne
            - Jesli biorac wiersz, gdzie znajduje sie ta wartosc ujemna:
                - wszystkie wspolczynniki w wierszu są dodatnie lub 0, znaczy ze zbior rozwiazan jest pusty
                - <STATUS 7>
            - Jesli biorac wiersz, gdzie znajduje sie ta wartosc ujemna:
                - jakikolwiek wspolczynnik w tym wierszu jest ujemny, znaczy ze tablica wymaga zrobienia dopuszczalnosci
                - <STATUS 1>
                - GOTO <KROK 3>

        ab) Jeśli w 0th kolumnie wszystkie wyrazy będą nieujemne ( 0 lub wiecej) znaczy ze rozwiazanie jest dopuszczalne
            - Nasza tablica reprezentuje wierzcholek simplexa
            - GO TO KROK xx

     b)  Sprawdzenie czy obecne rozwiazanie jest optymalne

        ba) Jeśli w 0th wierszu (funkcja celu) jest cokolwiek mniejsze od 0
            - cokolwiek pod znalezionym elementem jest wieksze od 0
            - to zadanie ma jedno rozwiazanie oraz mozna ulepszyc obecne rozwiazanie
            - <STATUS 2>
            - GO TO <KROK 5>
        bb) Jeśli w 0th wierszu (funkcja celu) jest wszystko dodatnie
            - koniec zadania
            - rozwiazanie optymalne zostalo osiagniete
            - <STATUS 3>

     c) Sprawdzenie: Zadanie nieograniczone z brakiem rozwiazania:

        ca) Jeśli w 0th wierszu (funkcja celu) jest cokolwiek mniejsze od 0
            - oraz wszystkie elementy ponizej tego znalezionego ujemnego wspolczynnika
            - sa mniejsze równe 0 (y<=0)  <NEW> zeby dobrze liczylo zmienilem na y<0 #jednak dalem spowrotem <=
            - zadanie jest nieograniczone i nie ma rozwiazania
            - <STATUS 4>

     d) Sprawdzenie: Zadanie nieskonczenie wiele rozwiazan na zbiorze ograniczonym:

        da) Jesli w 0th wierszu (funkcja celu) jest cokolwiek rowne 0
            - oraz w kolumnie ponizej tego 0 jest cokolwiek dodatniego
            - znaczy jest wiele rozwiazan na zbiorze ograniczonym
            - nalezy wyznaczyc drugi koniec odcinka
            - <STATUS 5>

     e)  Sprawdzenie: Zadanie nieskonczenie wiele rozwiazan na zbiorze nieograniczonym:

        ea) Jesli w 0th wierszu (funkcja celu) jest cokolwiek rowne 0
            - oraz w kolumnie ponizej tego 0 jest wszystko ujemne bądź rowne 0 (y <= 0)
            - znaczy ze jest nieskonczona ilosc rozwiazan optymalnych na zbiorze nieograniczonym
            - <STATUS 6>


3. Zrobienie dopuszczalnosci
    a) Znajdz minimum w 0th kolumnie i zapisz indeks tego wiersza
        - <NEW> nie moze wziac jako minimum elementu o indeksie (0,0)
    b) Znajdz minimum w wierszu o indeksie wyliczonym w 3a)
        - zapewnij zeby nie wzial czegos z 0th kolumny (tam sa ograniczenia i bralismy juz stamtad minimum 3a))
        - weź indeks tej kolumny
        - ta zmienna ktora stoi nad ta kolumna bedzie wchodzic do bazy
    c) Wylicz dzielenie wyrazow z 0th kolumny(ograniczenia) przez kolejne wyrazy z kolumny o indeksie wyliczonym w 3b)
        - zabezpieczyc przed
            - wyrazy z kolumny z indeksem nie moga byc mniejsze od 0 ani 0
            - wyrazy z kolumny 0th nie moga byc 0
            - nie mozemy operowac na wierszu gdzie jest funkcja celu
            - <NEW?> nie mozemy operowac na wierszu z ktorego bralismy minimum
        - weź z tego minimum
            - wez indeks  z wiersza gdzie bylo minimum
            - Zmienna stojaca przy tym wierszu wychodzi z bazy
     d) Okresl pivot
        - indeks z 3b) to indeks kolumny
        - indeks z 3c) to indeks wiersza
     e) Wylicz nową tablice Simplex - Skorzystaj z funkcji z KROKU 6
     f) GO TO Krok 2 - Ponowne sprawdzenie dopuszczalnosci


5. Pobranie pozycji pivota
    a) Weź indeks wyrazu minimum z 0th wiersza (funkcja celu) - to jest indeks kolumny pivota
        - ta zmienna ktora stoi nad ta kolumna bedzie wchodzic do bazy
    b) Wylicz dzielenie wyrazow z 0th kolumny(ograniczenia) przez kolejne wyrazy z kolumny o indeksie wyliczonym w 5a))
        - zabezpieczyc przed
            - wyrazy z kolumny z indeksem nie moga byc  0
            - wyrazy z kolumny 0th nie moga byc 0
            - nie mozemy operowac na wierszu gdzie jest funkcja celu
            - <NEW> wyrazy z kolumny z indeksem nie moga byc ujemne (podobno to sie nie liczy dla nas)
        - weź z tego minimum
            - wez indeks  z wiersza gdzie bylo minimum
            - Zmienna stojaca przy tym wierszu wychodzi z bazy
     c) Okresl pivot
        - indeks z 5a) to indeks kolumny
        - indeks z 5b) to indeks wiersza

6. Wylicz nowa tablice Simplex - krok ten pokazuje wszystkie operacje, ktore nalezy wykonac
    a) liczony element jest ma takie same indeksy jak pivot
        - Warunek: k == pivot_index_row and l == pivot_index_column:
        - Wzor: Y_new[k][l] = 1 / pivot_element
    b) liczone elementy są w tym samym wierszu co pivot
        - Warunek: k == pivot_index_row and l != pivot_index_column:
        - Wzor: Y_new[k][l] = Y[k][l]/pivot_element
    c) liczone elementy są w tej samej kolumnie co pivot:
        - Warunek: k != pivot_index_row and l == pivot_index_column:
        - Wzor: Y_new[k][l] = (-1) * Y[k][l]/pivot_element
    d) wszystko inne, czyli w innej kolumnie i w innym wierszu
        - Warunek: else
        - Wzor: Y_new[k][l] = (Y[k][l] - (Y[k][pivot_index_column] * Y[pivot_index_row][l])/pivot_element)

    e) Zamien oznaczenia zmiennych bazowych i wyjsciowych w pomocniczych tablicach
    f) - Dodatek - Jak latwiej zlapac regule do liczenia nowej tablicy Simplex?

           |p    q|   =>   |    1/p         q/p     |
           |r    s|   =>   |    -r/p     s - rq/p   |
           Zawsze dzielimy przez Pivot


7. GO TO Krok 4


8. Pokazanie rozwiazania

Statusy z metody check_the_case
 0 - default
 1 - require adminisibility
 2 - can be improved
 3 - is optimal
 4 - unlimited task no solution
 5 - infinite number of solution on limited area
 6 - infinite number of solution on unlimited area
 7 - empty set
