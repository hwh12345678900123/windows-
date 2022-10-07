import tkinter


class Notepad(object):
    def __init__(self, text: str) -> None:
        self.result = None
        self.text = text
        self.root = tkinter.Tk()
        self.entry = tkinter.Text(self.root, exportselection=False)
        self.entry.insert("insert", self.text)
        self.entry.pack()
        self.button = tkinter.Button(self.root, text="save", command=self.save)
        self.button.pack()

    def get_root(self) -> tkinter.Tk:
        return self.root

    def save(self) -> None:
        self.result = self.entry.get('1.0', tkinter.END)
        self.root.destroy()

    def get_result(self) -> str:
        return self.result


if __name__ == '__main__':
    notepad = Notepad("小胖子\nabc")
    notepad.get_root().mainloop()
    print(notepad.get_result().rstrip(), 'end')
