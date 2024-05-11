from tkinter import * 
from tkinter import ttk


def calculate(*args):
    try:
        value = float(feet.get())
        meters.set(int(0.3048 * value * 10000.0 + 0.5)/10000.0)
    except ValueError:
        pass



root = Tk()
root.title("Feet to Meters Example")

main_frame = ttk.Frame(root, padding="50")
main_frame.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

feet = StringVar()
feet_entry = ttk.Entry(main_frame, width=7, textvariable=feet)
feet_entry.grid(column=2, row=1, sticky=(W, E))

ttk.Button(main_frame, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W)

meters = StringVar()
ttk.Label(main_frame, textvariable=meters).grid(column=2, row=2, sticky=(W, E))

ttk.Label(main_frame, text='feet').grid(column=3, row=1, sticky=W)
ttk.Label(main_frame, text='is equivalent to').grid(column=1, row=2, sticky=E)
ttk.Label(main_frame, text='meters').grid(column=3, row=2, sticky=W)

root.mainloop()