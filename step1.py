import tkinter as tk
w=tk.Tk()
w.title('Hello Tusar')
w.geometry('300x200')
w.config(bg='cyan')
def fun1():
    w.config(bg='yellow')
b1=tk.Button(w,text='Change Colour',font=('Arial',15),bg='black',fg='white',command=fun1)
b1.place(x=30,y=30)
w.mainloop()
           
