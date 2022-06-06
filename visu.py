from tkinter import *
import sys
from new_approach import Simplex
from tkinter.scrolledtext import ScrolledText


class PrintLogger(object):  # create file like object

    def __init__(self, textbox):  # pass reference to text widget
        self.textbox = textbox  # keep ref

    def write(self, text):
        self.textbox.configure(state="normal")  # make field editable
        self.textbox.insert("end", text)  # write text to textbox
        self.textbox.see("end")  # scroll to end
        self.textbox.configure(state="disabled")  # make field readonly

    def flush(self):  # needed for file like object
        pass


class Visu:
    def __init__(self,rows, columns,TkWindow):
        self.table_with_value = []
        self.rows_number = rows
        self.columns_number = columns
        self.window = TkWindow
        self.table_with_Entry = []
        self.log_widget = None



        label_variable_number = Label(self.window, text = "Ilosc zmiennych")
        label_variable_number.grid(row = 0, column = 0,padx = 2,pady = 5)

        self.entry_columns_number = Entry(self.window, width=5)
        self.entry_columns_number.grid(row=0, column=1, padx=2, pady=5)



        label_limitation_number = Label(self.window, text = "Ilosc ograniczen")
        label_limitation_number.grid(row = 2, column = 0,padx = 2,pady = 5)
        self.entry_rows_number = Entry(self.window, width=5)
        self.entry_rows_number.grid(row=2, column=1, padx=2, pady=5)


        button_generate_table = Button(self.window, command=self.create_table, width=10, text="Create Table")
        button_generate_table.grid(row = 3, column = 0,columnspan = 2,pady = 10)

        self.button_get_data = Button(self.window, command = self.get_data, width = 10, text = "Get Data")
        self.button_calculate = Button(self.window, command = self.calculate, width = 10, text = "Calculate")




        self.window.mainloop()





    def create_table(self):




        self.rows_number = int(self.entry_rows_number.get())
        self.columns_number = int(self.entry_columns_number.get())

        self.button_get_data.grid(row = 8 + self.rows_number, column = 0, columnspan = 5,pady = 10)

        self.button_calculate.grid(row= 9 + self.rows_number, column=0, columnspan=5, pady=10)

        self.log_widget = ScrolledText(self.window, height=11, width=75, font=("consolas", "8", "normal"))
        self.log_widget.grid(row=1, column=10,rowspan = 4)
        label_log_widget = Label(self.window, text="Prezentacja wynikow")
        label_log_widget.grid(row=0, column=10)


        single_row = [0] * (self.columns_number + 1)
        label_row = [0] * (self.columns_number + 1)

        for i in range(self.rows_number + 2):
            for j in range(self.columns_number + 1):
                if i == 0:
                    label_row[j] = Label(self.window, width=5, text="x" + str(j))
                    label_row[j].grid(row=4+i, column=j)
                if i == 1:
                    single_row[j] = Entry(self.window, width=5, bg='yellow')
                    single_row[j].grid(row=4+i, column=j)
                else:
                    single_row[j] = Entry(self.window, width=5)
                    single_row[j].grid(row=4+i +1, column=j)

            if i == 0:
                self.table_with_Entry.clear()
            else:
                self.table_with_Entry.append(single_row)
                single_row = [0] * (self.columns_number + 1)





















    def get_data(self):
        single_row_value = [0] * (total_columns + 1)
        for i in range(self.rows_number + 1):
            for j in range(self.columns_number + 1):
                single_row_value[j] = float(self.table_with_Entry[i][j].get())
            self.table_with_value.append(single_row_value)
            single_row_value = [0] * (self.columns_number + 1)
        print(self.table_with_value)

    def calculate(self):
        logger = PrintLogger(self.log_widget)
        sys.stdout = logger
        sys.stderr = logger
        S1 = Simplex(self.table_with_value)
        S1.calculate_simplex()
        #self.button_get_data.grid_remove()






if __name__ == '__main__':
    top = Tk()
    top.geometry("700x350")
    top.title("Dwufazowa metoda Simplex")

    total_rows = 1
    total_columns = 2

    V1 = Visu(total_rows,total_columns,top)

#Testy od dr Szlachcic
    Test1 = [[0,-2,-5],[6,1,1],[3,0,1],[9,1,2]]
    Test2 = [[0,-1,-1],[4,0,1]] # na tym sie wywalilo


    Test3 = [[0,-1,-1],[4,1,0]]

    Test4 = [[0,-1,-1],[10,-1,-1],[3,-1,1]]






