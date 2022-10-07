import tools.file
import os
import tkinter


# with open('test2.py', 'w') as f:
#     f.write("def a():\n")
#     f.write("    print('Hello world!')")
# f.close()
# import test2
#
# test2.a()
def callback():
    print(entry.get('1.0', tkinter.END))


ROOT = tkinter.Tk()
var = tkinter.IntVar()
var.set(3)
button = tkinter.Button(text="aa", command=callback)
button.pack()
entry = tkinter.Text()
entry.pack()
ROOT.mainloop()
