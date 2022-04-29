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



















# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    A = [[1,1,0,1],[2,1,1,0]]
    B = [8,10]
    C = [1,1,0,0]
    D = [0,0]
    E = [0,0,0,0]
    t = 0
    c = []
    #zdefiniowane tabele do rozwiazania
    print(A[0][2])

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
