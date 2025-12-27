import tkinter as tk
from time import strftime
root=tk.Tk()
root.title('digital clock')

def time():
    string=strftime("%H:%M:%S %p\n %d %B,%Y")
    # string=strftime("%H:%M:%S %p\n %D") directly gives the date
    label.config(text=string)
    label.after(1000,time)
label=tk.Label(root,font=('arial','80','italic'),background='blue',foreground='green')
label.pack(anchor='center')
time()
root.mainloop()