
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

2. Sprawdzenie dopuszczalnosci rozwiązania początkowego ustawienia tablicy Simplex (czy jesteśmy w jednym z wierzchołkow)
    a) Jeśli w 0th kolumnie pojawi sie jakas wartosc ujemna, znaczy ze rozwiazanie jest niedopuszczalne - GO TO KROK 3
    b) Jeśli w 0th kolumnie wszystkie wyrazy będą nieujemne ( 0 lub wiecej) znaczy ze rozwiazanie jest dopuszczalne
        - nasza tablica reprezentuje wierzcholek simplexa
        - GO TO KROK 4

3. Zrobienie dopuszczalnosci
    a) Znajdz minimum w 0th kolumnie i zapisz indeks tego wiersza
    b) Znajdz minimum w wierszu o indeksie wyliczonym w 3a)
        - zapewnij zeby nie wzial czegos z 0th kolumny (tam sa ograniczenia i bralismy juz stamtad minimum 3a))
        - weź indeks tej kolumny
        - ta zmienna ktora stoi nad ta kolumna bedzie wchodzic do bazy
    c) Wylicz dzielenie wyrazow z 0th kolumny(ograniczenia) przez kolejne wyrazy z kolumny o indeksie wyliczonym w 3b)
        - zabezpieczyc przed
            - wyrazy z kolumny z indeksem nie moga byc mniejsze od 0 ani 0
            - wyrazy z kolumny 0th nie moga byc 0
            - nie mozemy operowac na wierszu gdzie jest funkcja celu
        - weź z tego minimum
            - wez indeks  z wiersza gdzie bylo minimum
            - Zmienna stojaca przy tym wierszu wychodzi z bazy
     d) Okresl pivot
        - indeks z 3b) to indeks kolumny
        - indeks z 3c) to indeks wiersza
     e) Wylicz nową tablice Simplex - Skorzystaj z funkcji z KROKU 6
     f) GO TO Krok 2 - Ponowne sprawdzenie dopuszczalnosci

4. Sprawdzenie optymalnosci
    a) Jeśli w 0th wierszu (funkcja celu) jest cokolwiek mniejsze od 0 - mozna ulepszyc
    b) Jesli w 0th wierszu (funkcja celu) są wszystkie wyrazy są dodatnie - nie mozna ulepszyc - GO TO KROK 8

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

