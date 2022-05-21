from copy import deepcopy


class Simplex:
    def __init__(self, A):
        self.Y = A #Y cala tablica
        self.Y_new = deepcopy(self.Y) #potrzebne do zamian
        self.pivot_index_column = 0
        self.pivot_index_row = 0
        self.pivot_element = 0

        self.basic_variables = [""]  * (len(A)) #ilosc wierszy to zmienne podstawowe
        self.leaving_variables = [""] * (len(A[0])) #ilosc kolumn to zmienne wyjsciowe
        

        for i in range(len(self.basic_variables)):
            if i == 0:
                self.basic_variables[i] = "x0"
            else:
                self.basic_variables[i] = "x" + str(A[0].index(A[0][-1]) + i)

        for i in range(len(self.leaving_variables)):
            if i == 0:
                self.leaving_variables[i] = "x0"
            else:
                self.leaving_variables[i] = "x" + str(i)

        #numery zmiennych, np x3, x4,x5
        #zebYmy wiedzieli potem jak interpretowac wY_newik



    ####    Krok - 2    ####
    def check_admissibility(self):
        for i in range(len(self.Y)):
            if self.Y[i][0] < 0:
                return False
        return True


    ####    Krok - 3    ####
    def do_admissibility(self):

        ##    Krok - 3a)    ##
        previous_value = 9999
        index_min_value_in_0th_column = 0
        for i in range(len(self.Y)):
            if self.Y[i][0] < 0:
                current_value = self.Y[i][0]
                if current_value < previous_value:
                    index_min_value_in_0th_column = i
                    previous_value = current_value

        ##    Krok - 3b)    ##
        previous_value = 9999
        for i in range(len(self.Y[index_min_value_in_0th_column])):
            if i != 0:
                if self.Y[index_min_value_in_0th_column][i] < previous_value:
                    self.pivot_index_column = i
                    previous_value = self.Y[index_min_value_in_0th_column][i]

        ##    Krok - 3c)    ##
        list_of_out_criteria = []
        for i in range(len(self.Y)):
            if self.Y[i][self.pivot_index_column] > 0 and self.Y[i][0] != 0 and i != 0:
                list_of_out_criteria.append(self.Y[i][0] / self.Y[i][self.pivot_index_column])
            else:
                list_of_out_criteria.append(99999)  # gdyby chcial dzielic przez 0 to wstaw tam duza liczbe zamiast dzielenia

        min_value = min(list_of_out_criteria)


        ##    Krok - 3d)    ##
        self.pivot_index_row = list_of_out_criteria.index(min_value)
        self.pivot_element = self.Y[self.pivot_index_row][self.pivot_index_column]

        ##    Krok - 3e)    ##
        self.pivot_step()


    ####    Krok - 4    ####
    def can_be_improved(self):
        return any(x < 0 for x in self.Y[0])

    ####    Krok - 5    ####
    def get_pivot_position(self):

        ##    Krok - 5a)    ##
        min_value = min(self.Y[0])
        self.pivot_index_column = self.Y[0].index(min_value)

        ##    Krok - 5b)    ##
        list_of_out_criteria = []
        for i in range(len(self.Y)):
            if self.Y[i][self.pivot_index_column] > 0 and self.Y[i][0] != 0 and i != 0:
                list_of_out_criteria.append(self.Y[i][0] / self.Y[i][self.pivot_index_column])
            else:
                list_of_out_criteria.append(99999)
        min_value = min(list_of_out_criteria)

        ##    Krok - 5c)    ##
        self.pivot_index_row = list_of_out_criteria.index(min_value)
        self.pivot_element = self.Y[self.pivot_index_row][self.pivot_index_column]

    ####    Krok - 6   ####
    def pivot_step(self):
        for k in range(len(self.Y)):
            for l in range(len(self.Y[0])):
                ##    Krok - 6a)    ##
                if k == self.pivot_index_row and l == self.pivot_index_column:
                    self.Y_new[k][l] = 1 / self.pivot_element
                ##    Krok - 6b)    ##
                elif k == self.pivot_index_row and l != self.pivot_index_column:
                    self.Y_new[k][l] = self.Y[k][l]/self.pivot_element
                ##    Krok - 6c)    ##
                elif k != self.pivot_index_row and l == self.pivot_index_column:
                    self.Y_new[k][l] = (-1) * self.Y[k][l]/self.pivot_element
                ##    Krok - 6d)    ##
                else:
                    self.Y_new[k][l] = (self.Y[k][l] - (self.Y[k][self.pivot_index_column] * self.Y[self.pivot_index_row][l])/self.pivot_element)

        self.Y = deepcopy(self.Y_new)

        ##    Krok - 6e)    ##
        to_basic_variable = self.leaving_variables[self.pivot_index_column]
        to_leaving_variable = self.basic_variables[self.pivot_index_row]
        self.leaving_variables[self.pivot_index_column] = to_leaving_variable
        self.basic_variables[self.pivot_index_row] = to_basic_variable

    ####    Krok - 8    ####
    def show_optimal_solution(self):
        print("-----Rozwiazanie optymalne-----")
        for i in range(len(self.basic_variables)):
            print(str(self.basic_variables[i]) + ":" + str(round(self.Y[i][0],2)))

if __name__ == '__main__':
    #TODO
    #  - dodac nazwy zmiennych w bazie i sledzenie ich
    #  x obsluzyc minimalizacje funkcji celu
    #  - przetestowac z odpowiedziami poszczegolne przejscia i kolejne tablice simplexowe
    # najlepiej z wykladem
    # dopuszczanie do rozwiazania, jak i potem szukanie rozwiazan
    # sprawdzic dla wiekszych instancji jak sie zachowuje algorytm
    # obsluzyc sytuacje wyjatkowe: te wszystkie zbiory puste i inne ( opisane na wykladzie)
    # stworzyc wizu
    # parsing danych z wizu
    # - obslugiwanie minimum/maximum, ograniczenia wiekszosciowe, mniejszosciowe
    # - odpowiednie mnozenie przez minus
    # testy wizu
    # rysowanie wykresow dla 2 zmiennych



    A1 = [[7,0.33,-0.33],[1.5,-0.16,0.66],[3.5,0.16,1.33],[3.5,0.16,0.33]]

    A2 = [[0,-40,-30],[12,1,1],[16,2,1]]

    A3 = [[0,-2,-5],[24,1,4],[21,3,1],[9,1,1]]
    A4 = [[0,-2,-5],[6,1,1],[3,0,1],[9,1,2]]

    #dla B dziala robienie dopuszczalnego rozwiazania
    B = [[0,-1,-6],[-2,-2,-1],[3,-1,1],[6,1,1]]

    #dla C nie dziala, ale to jest min, plus same wiekszosciowe ograniczenia
    C = [[0,1,1],[-8,-1,-2],[-6,-2,-1],[-5,-1,-1]]


    #Testy
    #Ograniczenia mniejszosciowe, max funckji celu
    A = [[0, -2, -1], [5, 1, 1], [0, -1, 1], [21, 6, 2]]  # dziala
    A1 = [[0,-16,-12],[720,8,6],[1280,8,16],[960,12,8],[900,4,8]] #dziala ok
    A2 = [[0,-1,-3,-2],[5,1,2,1],[4,1,1,1],[1,0,1,2]] #dziala ok
    A3 = [[0,-1,-4],[4,-1,2],[1,-1,1],[36,4,5]] # dziala


    # Z pliku
    E1 = [[0,-1,1],[3,-2,1],[6,1,1],[20,5,2]]
    E3 = [[0,-1,-2],[3,-2,1],[6,1,1],[20,5,2]]
    E9 = [[0,-1,-2],[100,1,1],[720,6,9],[60,0,1]]
    E8 = [[0,-2100,-1200],[-2,2,-1],[-2,-1,2]]
    #Ograniczenia mniejszosciowe, min funkcji celu
    #test oblany, bo tego nie trzeba
    B = [[0,1,1],[4,1,1],[2,-1,1]]


    S1 = Simplex(E8)

    print(S1.check_admissibility())
    S1.do_admissibility()
    print(S1.pivot_index_row,S1.pivot_index_column,S1.pivot_element)
    print(S1.Y)


    #S1.get_pivot_position()
    #print(S1.pivot_index_row,S1.pivot_index_column,S1.pivot_element)
    #S1.pivot_step()
    #print(S1.Y)
    #S1.show_optimal_solution()
    #print("########################")
    #S1.get_pivot_position()
    #print(S1.pivot_index_row, S1.pivot_index_column, S1.pivot_element)
    #S1.pivot_index_row = 1
    #S1.pivot_element = 1
    #S1.pivot_step()
    #print(S1.Y)
    #S1.show_optimal_solution()

   #while S1.can_be_improved():
   #    S1.get_pivot_position()
   #    S1.pivot_step()
   #    print(S1.Y)
   #S1.show_optimal_solution()

