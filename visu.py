from tkinter import *
def GetData():
    #trzeba rozwiazac ten problem
    print(table[0][0].get())
    #table_with_value = []
    #single_row_value = [0] * (total_columns + 1)
    #for i in range(total_rows + 1):
    #    for j in range(total_columns + 1):
    #       single_row_value[j] = table1[i][j].get()
    #    table_with_value.append(single_row_value)
    #print(table_with_value)

top = Tk()
top.geometry("1000x500")

# the label for user_name 
#user_name = Label(top,
#                  text="Username").place(x=40,
#                                         y=60)

# the label for user_password  
#user_password = Label(top,
#                      text="Password").place(x=40,
#                                             y=100)

Input_frame = Frame(top)
Input_frame.grid(row =4,column= 4)


total_rows = 4
total_columns = 2

single_row = [0] * (total_columns+1)
label_row = [0] * (total_columns+1)

table = []
for i in range(total_rows+2):
    for j in range(total_columns+1):
        if i == 0:
            label_row[j] = Label(Input_frame,width = 5,text = "x"+str(j))
            label_row[j].grid(row = i, column = j)
        if i == 1:
            single_row[j] = Entry(Input_frame, width=5,bg = 'yellow')
            single_row[j].grid(row=i, column=j)
        else:
            single_row[j] = Entry(Input_frame, width=5)
            single_row[j].grid(row=i+1, column=j)

    if i==0:
        table.clear()
    else:
        table.append(single_row)

print(table)

Button_Confirm = Button(top,command = GetData,width = 6)
Button_Confirm.grid(row =0,column= 0)







top.mainloop() 