from copy import deepcopy
class Simplex:
    def __init__(self, A):
        self.YS = A #Y stare
        self.YN = deepcopy(self.YS)

        #Y nowe
        self.pivot_index_column = 0
        self.pivot_index_row = 0
        self.pivot_element = 0
        self.B_basis_variable_number = [0] * (len(A[0]) - 1)

        for i in range (len(self.B_basis_variable_number)):
            self.B_basis_variable_number[i] = A[0].index(A[0][-1]) + i

        #numery zmiennych, np x3, x4,x5
        #zebysmy wiedzieli potem jak interpretowac wynik

    #sprawdzenie czy pierwsza kolumna ma wszystkie elementy dodatnie
    def check_admissibility(self):
        for i in range(len(self.YS)):
            if self.YS[i][0] < 0:
                return False
        return True


    def do_admissibility(self):

        #znaleźć wiersz, ktory ma ujemna wartosc w ograniczeniach
        #--done__
        #znaleźć min w tym wierszu ale bez 0 elementu
        #spisac index tej kolumny
        #--done

        #wyliczyc wspolczynniki, ale ominac wyrazy ujemny
        #wziac minimum z tych wspolczynnikow a nastepnie z tego index
        #indexy wziete to indeks naszego pivota

        previous_value = 9999
        row_min_value = 0
        pivot_column_index = 0
        pivot_row_index = 0
        for i in range(len(self.YS)):
            if self.YS[i][0] < 0:
                current_value = self.YS[i][0]
                if current_value < previous_value:
                    row_min_value = i
                    previous_value = current_value

        previous_value = 9999
        for i in range(len(self.YS[row_min_value])):
            if i != 0:
                if self.YS[row_min_value][i] < previous_value:
                    pivot_column_index = i
                    previous_value = self.YS[row_min_value][i]



        list_of_out_criteria = []

        for i in range(len(self.YS)):
            if self.YS[i][pivot_column_index] > 0 and self.YS[i][0] != 0 and i != 0: #wszystkie zabezpieczenia
                list_of_out_criteria.append(self.YS[i][0] / self.YS[i][pivot_column_index])
            else:
                list_of_out_criteria.append(99999)  # gdyby chcial dzielic przez 0 to wstaw tam duza liczbe zamiast dzielenia

        # print(list_of_out_criteria)
        min_value = min(list_of_out_criteria)
        pivot_row_index = list_of_out_criteria.index(min_value)

        print(pivot_row_index)
        print(pivot_column_index)


        self.pivot_index_column = pivot_column_index
        self.pivot_index_row = pivot_row_index
        self.pivot_element = self.YS[pivot_row_index][pivot_column_index]








    def can_be_improved(self):
        return any(x < 0 for x in self.YS[0])
    #jesli cokolwiek jest mniejsze od 0 we wspolczynnikach funkcji celu


    def get_pivot_position(self):
        min_value = min(self.YS[0])
        self.pivot_index_column = self.YS[0].index(min_value)

        list_of_out_criteria = []
        for i in range(len(self.YS)):
            if self.YS[i][self.pivot_index_column] != 0 and self.YS[i][0] != 0 and i != 0:
                list_of_out_criteria.append(self.YS[i][0] / self.YS[i][self.pivot_index_column])
            else:
                list_of_out_criteria.append(99999)  # gdyby chcial dzielic przez 0 to wstaw tam duza liczbe zamiast dzielenia

        #print(list_of_out_criteria)
        min_value = min(list_of_out_criteria)
        self.pivot_index_row = list_of_out_criteria.index(min_value)
        self.pivot_element = self.YS[self.pivot_index_row][self.pivot_index_column]

    def pivot_step(self):
        for k in range(len(self.YS)):
            for l in range(len(self.YS[0])):
                if k == self.pivot_index_row and l == self.pivot_index_column:
                    self.YN[k][l] = 1 / self.pivot_element

                elif k == self.pivot_index_row and l != self.pivot_index_column:
                    self.YN[k][l] = self.YS[k][l]/self.pivot_element

                elif k != self.pivot_index_row and l == self.pivot_index_column:
                    self.YN[k][l] = (-1) * self.YS[k][l]/self.pivot_element

                else:
                    a = self.YS[k][l]
                    b = self.YS[k][self.pivot_index_column]
                    c = self.YS[self.pivot_index_row][l]
                    d = self.pivot_element
                    self.YN[k][l] = (self.YS[k][l] - (self.YS[k][self.pivot_index_column] * self.YS[self.pivot_index_row][l])/self.pivot_element)

        self.YS = deepcopy(self.YN)

    def show_optimal_solution(self):
        print(self.YS)


if __name__ == '__main__':
    A = [[0,-2,-1],[5,1,1],[0,-1,1],[21,6,2]]
    A1 = [[7,0.33,-0.33],[1.5,-0.16,0.66],[3.5,0.16,1.33],[3.5,0.16,0.33]]

    A2 = [[0,-40,-30],[12,1,1],[16,2,1]]

    A3 = [[0,-2,-5],[24,1,4],[21,3,1],[9,1,1]]
    A4 = [[0,-2,-5],[6,1,1],[3,0,1],[9,1,2]]

    B = [[0,-1,-6],[-2,-2,-1],[3,-1,1],[6,1,1]]


    S1 = Simplex(B)

    print(S1.check_admissibility())
    S1.do_admissibility()
    S1.pivot_step()
    print(S1.can_be_improved())
    S1.get_pivot_position()
    S1.pivot_step()
    print(S1.can_be_improved())


    print(S1.YS)


   # while S1.can_be_improved():
    #    S1.get_pivot_position()
     #   S1.pivot_step()
    #S1.show_optimal_solution()

