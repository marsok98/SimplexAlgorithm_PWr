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
    pass
