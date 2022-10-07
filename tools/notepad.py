import tkinter


class Notepad(object):
    def __init__(self, text: str) -> None:
        self.result = None
        self.text = text
        self.root = tkinter.Tk()
        self.variable = tkinter.Variable(self.root)
        self.variable.set(self.text)
        self.entry = tkinter.Entry(self.root, textvariable=self.variable)
        self.entry.pack()
        self.button = tkinter.Button(self.root, text="save", command=self.save)
        self.button.pack()

    def get_root(self) -> tkinter.Tk:
        return self.root

    def save(self) -> None:
        self.result = self.entry.get()
        self.root.destroy()

    def get_result(self) -> str:
        return self.result


if __name__ == '__main__':
    notepad = Notepad("小胖子")
    print(notepad.get_root().mainloop())
