from tkinter import * 
import csv

class App(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.output()

    def output(self):
         
        Label(text='Sleep time?').pack(side=LEFT,padx=5,pady=5)
        self.e1 = Entry(root, width=10)
        self.e1.pack(side=LEFT,padx=5,pady=5)
        
        Label(text='Wake up time?').pack(side=LEFT,padx=5,pady=5)
        self.e2 = Entry(root, width=10)
        self.e2.pack(side=LEFT,padx=15,pady=15)
        
        Label(text='Study?').pack(side=LEFT,padx=5,pady=5)
        self.e3 = Entry(root, width=10)
        self.e3.pack(side=LEFT,padx=5,pady=5)
        
        Label(text='Family?').pack(side=LEFT,padx=5,pady=5)
        self.e4 = Entry(root, width=10)
        self.e4.pack(side=LEFT,padx=5,pady=5)

        self.b = Button(root, text='Submit', command=self.writeToFile)
        self.b.pack(side=RIGHT,padx=5,pady=5)

    def writeToFile(self):
        with open('WorkOrderLog.csv', 'a') as f:
            w=csv.writer(f, quoting=csv.QUOTE_ALL)
            t=[self.e1.get(),self.e2.get(),self.e3.get(),self.e4.get()]
            w.writerow(t)

if __name__ == "__main__":
    root=Tk()
    root.title('Auto Logger')
    root.geometry('1000x100')
    app=App(master=root)
    app.mainloop()
    root.mainloop()