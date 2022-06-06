from tkinter import *
import new_approach

class Visu:
    def __init__(self,rows, columns,TkWindow):
        self.table_with_value = []
        self.rows_number = rows
        self.colums_number = columns
        self.window = TkWindow
        self.table_with_Entry = []

        single_row = [0] * (total_columns + 1)
        label_row = [0] * (total_columns + 1)

        for i in range(self.rows_number + 2):
            for j in range(self.colums_number + 1):
                if i == 0:
                    label_row[j] = Label(self.window, width=5, text="x" + str(j))
                    label_row[j].grid(row=i, column=j)
                if i == 1:
                    single_row[j] = Entry(self.window, width=5, bg='yellow')
                    single_row[j].grid(row=i, column=j)
                else:
                    single_row[j] = Entry(self.window, width=5)
                    single_row[j].grid(row=i + 1, column=j)

            if i == 0:
                self.table_with_Entry.clear()
            else:
                self.table_with_Entry.append(single_row)
                single_row = [0] * (total_columns + 1)

        Button_Confirm = Button(self.window, command=self.GetData, width=6)
        Button_Confirm.grid(row=0, column=0)
        self.window.mainloop()




    def GetData(self):
        single_row_value = [0] * (total_columns + 1)
        for i in range(total_rows + 1):
            for j in range(total_columns + 1):
                single_row_value[j] = float(self.table_with_Entry[i][j].get())
            self.table_with_value.append(single_row_value)
            single_row_value = [0] * (total_columns + 1)
        print(self.table_with_value)




top = Tk()
top.geometry("1000x500")

#Input_frame = Frame(top)
#Input_frame.grid(row =4,column= 4)


total_rows = 2
total_columns = 2

V1 = Visu(total_rows,total_columns,top)



