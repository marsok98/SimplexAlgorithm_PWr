import numpy as np

#https://www.geeksforgeeks.org/simplex-algorithm-tabular-method/
class Simplex:
    def __init__(self, A,XB,Z):
        self.A_equations = A
        self.XB_limits = XB
        self.Z_target_function = Z
        self.CB_coefficients_basis_variable = [0]*len(XB)
        self.CZ_relative_profit = [0] * len(Z)
        self.pivot_index_column_max = 0
        self.pivot_index_row_min = 0


    def can_be_improved(self):
        i=0
        j=0
        t=0
        for i in range(len(self.Z_target_function)):
            for j in range(len(self.CB_coefficients_basis_variable)):
                t += self.A_equations[j][i] * self.CB_coefficients_basis_variable[j]
            print(t)
            self.CZ_relative_profit[i] = self.Z_target_function[i] - t
            t = 0
        print(self.CZ_relative_profit)
        return any(x > 0 for x in self.CZ_relative_profit[:-1])
        #jesli cokolwiek jest wieksze od 0 to znaczy ze mozna ulepszyc

    def get_pivot_position(self):
        #obliczanie indeksu dla zmiennej wejsciowej
        max_value = max(self.CZ_relative_profit)
        self.pivot_index_column_max = self.CZ_relative_profit.index(max_value)
        print(self.pivot_index_column_max)

        #obliczanie indeksu dla zmiennej wyjsciowej
        list_of_out_criteria = []
        for i in range(len(self.XB_limits)):
            list_of_out_criteria.append(self.XB_limits[i] / self.A_equations[i][self.pivot_index_column_max])

        print(list_of_out_criteria)
        min_value = min(list_of_out_criteria)
        self.pivot_index_row_min = list_of_out_criteria.index(min_value)
        print(self.pivot_index_row_min)
        # max_index_column opisuje to co wejdzie do podstawy - ktora kolumna
        # min_index_row opisuje to co wyjdzie z podstawy  - ktory wiersz

        pivot_element = self.A_equations[self.pivot_index_row_min][self.pivot_index_column_max]
        print(pivot_element)

    def pivot_step(self):
        # sekcja wejscia do podstawy
        # najpierw wejscie do kolumny Cb inaczej D
        self.CB_coefficients_basis_variable[self.pivot_index_row_min] = \
            self.Z_target_function[self.pivot_index_column_max]  # przepisanie do tablicy Cb

        # teraz najwiekszy myk trzeba bedzie zrobic
        # z zrobieniem nowej macierzy
        print(self.XB_limits[self.pivot_index_row_min])
        pivot_element = self.A_equations[self.pivot_index_row_min][self.pivot_index_column_max]
        self.XB_limits[self.pivot_index_row_min] /= pivot_element
        #podzielono liczbe z kolumny XB, teraz trzeba pozostaly wiersz w kolumnie A
        print(self.A_equations[self.pivot_index_row_min])

        for j in range(len(self.A_equations[self.pivot_index_row_min])):
            self.A_equations[self.pivot_index_row_min][j] /= pivot_element
        #zostal podmieniony wiersz ktory zawieral pivot
        print(self.A_equations[self.pivot_index_row_min])

        #teraz nalezy zadbac o pozostala macierz, zerujac wspolczynniki bedace nad
        #wierszem z pivotem

        # zalatwiony jest wiersz tam gdzie byl pivot, ale
        # teraz nalezy wszystkie pozostale wiersze ogarnac
        # i przemienic tak, aby mozna bylo policzyc wskazniki optymalnosci
        # trzeba by bylo wydzielic tablice cala poza tym wierszem pivota.
        print("########################")
        print(A)
        for i in range(len(self.A_equations)):
            if i != self.pivot_index_row_min:  # pod warunkiem, ze nie jestesmy w wierszu z min_index_row
                var = A[i][self.pivot_index_column_max]  # wspolczynnik przez ktory mnozymy, zeby zerowac pozycje nad pivotem
                for j in range(len(self.A_equations[0])):
                    self.A_equations[i][j] = self.A_equations[i][j] - self.A_equations[self.pivot_index_row_min][j] * var
                self.XB_limits[i] = self.XB_limits[i] - self.XB_limits[self.pivot_index_row_min] * var

        print(self.A_equations)
        print(self.XB_limits)
        ##teraz nalezy policzyc wskazniki optymalnosci dla nowej tabeli


        pass


    def get_solution(self):
        return self.XB_limits













# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    A = [[1,1,0,1],[2,1,1,0]]#glowna tabela, jeden wiersz symbolizuje jedno rownanie
    B = [8,10] #ograniczenia
    C = [1,1,0,0] ##funkcja celu
    D = [0,0] # wspolczynniki przy zmiennych bazowych
    E = [0,0,0,0] #wskazniki pomocnicze
    t = 0
    c = []
    #zdefiniowane tabele do rozwiazania
    print(A[0][2])

    A1 = [[1,1,1,0,0],[0,1,0,1,0],[1,2,0,0,1]]
    B1 = [6,3,9]
    C1 = [2,5,0,0,0]

    S1=Simplex(A,B,C)
    #dziala narazie tylko dla 2 wymiarow
    #celem jest zrobic dla 3
    while S1.can_be_improved():
        print("################################")
        S1.get_pivot_position()
        print("################################")
        S1.pivot_step()
        print("################################")

    result = S1.get_solution()
    print(result)







