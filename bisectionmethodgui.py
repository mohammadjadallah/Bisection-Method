# function to calculate equation

def Bisection_Method(equation, a, b, given_error):  # function, boundaries, Es

        li_a = deque()  # a
        li_b = deque()  # b
        li_c = deque()  # x root -> c
        li_fc = deque()  # f(xr)
        li_fa = deque()  # f(a)
        li_fb = deque()  # f(b)
        li_Ea = deque()  # estimated error

        data = {
            'Xl': li_a,
            'Xu': li_b,
            'Xr': li_c,
            'f(Xl)': li_fa,
            'f(Xu)': li_fb,
            'f(Xr)': li_fc,
            'Ea%': li_Ea,
        }

        global c

        def f(x):
            F = eval(equation)  # the x here when we f(a) a will be instead of x
            return F

        # substitute boundaries in function
        if f(a)*f(b) >= 0:
            showerror('Error', 'Bisection method is fail')
            quit()

        # elif we have a different sign
        else:
            Estimated_Error = 0

            while Estimated_Error/100 <= given_error:
                c = (a + b) / 2
                if Estimated_Error == 0:
                    li_a.append(a)
                    li_b.append(b)
                    li_c.append(c)
                    li_fa.append(f(a))
                    li_fb.append(f(b))
                    li_fc.append(f(c))
                    li_Ea.append(None)

                if f(a)*f(c) < 0:
                    b = c
                    c1 = (a + b)/2
                    Estimated_Error = abs((c1 - c)/c1) * 100 # b became the old root and c1 became the new root ((current - previous)/current) * 100

                elif f(b)*f(c) < 0:
                    a = c
                    c1 = (a + b) / 2
                    Estimated_Error = abs((c1 - c) / c1) * 100

                else:
                    showerror('Error', 'something is wrong!')

            else:
                while Estimated_Error/100 >= given_error:
                    c = (a + b) / 2

                    # append data to to the list

                    li_a.append(a)
                    li_b.append(b)
                    li_c.append(c)
                    li_fa.append(f(a))
                    li_fb.append(f(b))
                    li_fc.append(f(c))
                    li_Ea.append('%.5f' % Estimated_Error+'%')

                    if f(a) * f(c) < 0:
                        b = c
                        c1 = (a + b) / 2
                        Estimated_Error = abs((c1 - c) / c1) * 100  # b became the old root and c1 became the new root ((current - previous)/current) * 100
                    elif f(b) * f(c) < 0:
                        a = c
                        c1 = (a + b) / 2
                        Estimated_Error = abs((c1 - c) / c1) * 100

                    else:
                        showerror('Error', 'something is wrong!')
                else:
                    c = (b + a)/2
                    li_a.append(a)
                    li_b.append(b)
                    li_c.append(c)
                    li_fa.append(f(a))
                    li_fb.append(f(b))
                    li_fc.append(f(c))
                    li_Ea.append('%.5f' % Estimated_Error+'%')
                    label3.config(text='The text file downloaded inside the project, you can see the data...')

                    with open('BisectionMethodData2.txt', 'w', encoding="utf-8") as f:
                        f.write(tabulate(data, headers='keys', tablefmt='fancy_grid', showindex=True))


def draw_function():
    try:
        def f(x):
            return eval(str(entry_equation.get()))
        x = linspace(float(entry_a.get()), float(entry_b.get()))
        y = f(x)

        #fig = figure()
        #ax = fig.add_subplot(1, 1 , 1)
        #ax.spines['left'].set_position('center')
        #ax.spines['bottom'].set_position('center')
        plot(x, y, 'r')
        plot(c, f(c), 'bo')  # نجحت لإني عرفت ال c كمتغير عالمي عام وين ما بدي بستخدمه

        show()

    #هذا الكلام استخدمته عشان إذا البيانات معبأة ولكن لم يتم جلب الحل أي البيانات سيتم عرض هذه حتى لايكون لدينا خطأأوإستثناء
    except NameError:
        label3.config(text='Get Data in the first')


def placeholder1(event):
    if entry_equation.get() == '                          Enter the function here':
        entry_equation.delete(0, END)


def placeholder2(event):
    if entry_a.get() == '      x lower':
        entry_a.delete(0, END)


def placeholder3(event):
    if entry_b.get() == '      x upper':
        entry_b.delete(0, END)


def placeholder4(event):
    if entry_given_error.get() == '   Given Error':
        entry_given_error.delete(0, END)


def check_for_space(event):
    if entry_equation.get() == "":
        entry_equation.insert(0, " ")
    elif entry_equation.get()[0] != " ":
        entry_equation.insert(0, " ")

    if entry_a.get() == "":
        entry_a.insert(0, " ")
    elif entry_a.get()[0] != " ":
        entry_a.insert(0, " ")

    if entry_b.get() == "":
        entry_b.insert(0, " ")
    elif entry_b.get()[0] != " ":
        entry_b.insert(0, " ")

    if entry_given_error.get() == "":
        entry_given_error.insert(0, " ")
    elif entry_given_error.get()[0] != " ":
        entry_given_error.insert(0, " ")


def link(url):
    open_new_tab(url)


if __name__ == '__main__':
    from tkinter import *
    from tkinter.messagebox import showerror
    from collections import deque
    from tabulate import tabulate
    from io import open
    from numpy import linspace, cos, tan, sin, tanh, cosh, sinh
    from matplotlib.pyplot import plot, show
    from webbrowser import open_new_tab

    root = Tk()
    root.title('                                                    '
               '                                                     '
               '                                       Bisection Method')
    root.geometry('1050x600')
    root.resizable(0, 0)
    root.config(bg='#C4DBE0')
    # create tow labels
    label1 = Label(root, font=('Normal 13 bold'),
                    text='Note: This program help you to find the root to the function'
                         ' as well as you can draw the function that you want.',
                    bg='#C4DBE0',
                   )
    label2 = Label(root, font=('Normal 14 bold'),
                         text="""- What is the bisection method?  the bisection method is a root-finding method that 
                  applies to any continuous functions for which one knows two values with opposite signs.""",
                    bg='#C4DBE0',
                   fg='#0C6980'
                   )

    label3 = Label(root,font=('Normal 14 bold'),
                   bg='#C4DBE0',
                   fg='#0C6980',

                   )

    label4 = Label(root, font=('Normal 12 bold'),
                   bg='#C4DBE0',
                   fg='#0C6980',
                   text='                                               - Addition >> (+)           - subtraction >> (-)\n'
                   '          - Multiplication >> (*)\n- Power >> (**) \n- Division >> (/)'
                   )

    label5 = Label(root, font=('Normal 14 bold'),
                   bg='#C4DBE0',
                   fg='#1463e4',
                   cursor='hand2',
                   text='Bisection Method?'
                   )

    entry_equation = Entry(root, font='Normal 20 bold',
                  bg='#2EB5E0',
                  relief=FLAT,
                  insertbackground='#F8D210')


    entry_a = Entry(root, font='Normal 20 bold',
                  bg='#2EB5E0',
                  relief=FLAT,
                  insertbackground='#F8D210')

    entry_b = Entry(root, font='Normal 20 bold',
                  bg='#2EB5E0',
                  relief=FLAT,
                  insertbackground='#F8D210')


    entry_given_error = Entry(root, font='Normal 20 bold',
                  bg='#2EB5E0',
                  relief=FLAT,
                  insertbackground='#F8D210')

    btn1 = Button(root, text='Draw function',
                  font='Normal 20 bold',
                  bg='#2EB5E0',
                  relief=GROOVE,
                  activebackground='#2EB5E0',
                  cursor="hand2",
                  command=lambda: draw_function()
                  )
    btn2 = Button(root, text='Get the data',
                  font='Normal 20 bold',
                  bg='#2EB5E0',
                  relief=GROOVE,
                  activebackground='#2EB5E0',
                  cursor="hand2",
                  command=lambda: Bisection_Method(str(entry_equation.get()),
                                                   float(entry_a.get()),
                                                   float(entry_b.get()),
                                                   float(entry_given_error.get())/100)
                  )

    # setup labels
    label1.place(x=50, y=10)
    label2.place(x=50, y=50)
    label3.place(x=150, y=500)
    label4.place(x=50, y=100)
    label5.place(x=240, y=50)
    label5.bind('<Button-1>', lambda e: link('https://en.wikipedia.org/wiki/Bisection_method'))

    # setup entries
    entry_equation.insert(0, '                          Enter the function here')
    entry_a.insert(0, '      x lower')
    entry_b.insert(0, '      x upper')
    entry_given_error.insert(0, '   Given Error')
    entry_given_error.bind('<Button>', placeholder4)
    entry_b.bind('<Button>', placeholder3)
    entry_a.bind('<Button>', placeholder2)
    entry_equation.bind('<Button>', placeholder1)
    entry_equation.bind('<Key>', check_for_space)
    entry_a.bind('<Key>', check_for_space)
    entry_b.bind('<Key>', check_for_space)
    entry_given_error.bind('<Key>', check_for_space)
    entry_equation.place(x=150, y=250, width=700, height=100)
    entry_a.place(x=150, y=190, width=200, height=50)
    entry_b.place(x=400, y=190, width=200, height=50)
    entry_given_error.place(x=650, y=190, width=200, height=50)

    # setup buttons

    btn1.place(x=150, y=360, width=340, height=100)
    btn2.place(x=510, y=360, width=340, height=100)

    root.mainloop()