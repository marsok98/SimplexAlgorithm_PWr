import numpy as np



class SimplexTable:
    def __init__(self, n, m, price, main, side, optimal_indicators, current_target_function, limitation, out_criteria, coefficients):
        self.n = n
        self.m = m
        self.price = price
        self.main = main
        self.side = side
        self.optimal_indicators = optimal_indicators
        self.current_target_function = current_target_function
        self.limitation = limitation
        self.out_criteria = out_criteria
        self.coefficients_current_solution = coefficients


    def calculate_optimal_indicators(self):
        for i in range(self.n+self.m):
            for j in range(self.m):
                self.side[i] = self.main[j][i]



    def find_and_calculate_max(self):
        pass

    def find_out_criteria_and_replace_variable(self):
        pass

    def determine_if_solution_is_optimal(self):
        pass

    def calculate_new_table(self):
        pass



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


    S1=Simplex(A,B,C)

    napis = S1.can_be_improved()
    print(napis)
    print("################################")
    S1.get_pivot_position()
    print("################################")

    for i in range(len(C)):
        for j in range(len(D)):
            t += A[j][i]*D[j]
        print(t)
        E[i] = C[i] - t
        t =0
    print(E)

    max_value = max(E)
    max_index_column = E.index(max_value)
    print(max_index_column)

    for i in range(len(B)):
        c.append(B[i]/A[i][max_index_column])

    print(c)
    min_value = min(c)
    min_index_row = c.index(min_value)
    print(min_index_row)
    #max_index_column opisuje to co wejdzie do podstawy - ktora kolumna
    #min_index_row opisuje to co wyjdzie z podstawy  - ktory wiersz

    pivot_element = A[min_index_row][max_index_column]
    print(pivot_element)

    #sekcja wejscia do podstawy
    #najpierw wejscie do kolumny Cb inaczej D
    D[min_index_row]=C[max_index_column] #przepisanie do tablicy D
    #teraz najwiekszy myk trzeba bedzie zrobic
    #z zrobieniem nowej macierzy
    print(B[min_index_row])
    B[min_index_row] = B[min_index_row] / pivot_element

    print(A[min_index_row])

    for j in range(len(A[min_index_row])):
        A[min_index_row][j] /=pivot_element

    print(A[min_index_row])

#zalatwiony jest wiersz tam gdzie byl pivot, ale
#teraz nalezy wszystkie pozostale wiersze ogarnac
#i przemienic tak, aby mozna bylo policzyc wskazniki optymalnosci
#trzeba by bylo wydzielic tablice cala poza tym wierszem pivota.
    print(A)
    for i in range(len(A)):
        if i != min_index_row: #pod warunkiem, ze nie jestesmy w wierszu z min_index_row
            var = A[i][max_index_column] #wspolczynnik przez ktory mnozymy, zeby zerowac pozycje nad pivotem
            for j in range(len(A[0])):
                A[i][j] = A[i][j] - A[min_index_row][j]*var
            B[i] = B[i] - B[min_index_row] * var

    print(A)
    print(B)
    ##teraz nalezy policzyc wskazniki optymalnosci dla nowej tabeli

    for i in range(len(C)):
        for j in range(len(D)):
            t += A[j][i]*D[j]
        print(t)
        E[i] = C[i] - t
        t =0
    print(E)
##pierwsze przejscie przez program jest zrobione
##teraz kolejna iteracja programu
##nalezy pozamykac wszystko w funkcje










    pass
