import sys
from tools import file
import os
import tqdm
import json
import Exceptions
import tools
import typing

FileAlreadyExistsException = Exceptions.Exceptions.FileAlreadyExistsException(name="FileAlreadyExists",
                                                                              message="File already exists")
default_file_editor = "notepad"


class Path(object):
    def __str__(self) -> str:
        return self.name

    def __init__(self, name: str, father) -> None:

        self.name = name
        self.children = []
        self.files = []
        if father:
            self.disk = False
            self.fathers = [father]
            self.pre_read = False
        else:
            print("father", father)
            self.disk = True
            self.fathers = []
            self.absolute_path = name
            self.read()
            self.pre_read = True
            print("write_self")
            self.write_self()
            print("log")

        if not self.disk:
            print("disk", self.disk)

            while True:
                if not self.fathers[-1].disk:
                    self.fathers += self.fathers[-1].fathers
                else:
                    break
            self.absolute_path = ""
            self.fathers.reverse()
            for father in self.fathers:
                self.absolute_path += str(father) + "/"

    def read(self) -> None:
        self.pre_read = True
        result = tools.file.safe_read(self.absolute_path)
        print("result: ", result)
        for child in result[0]:
            print("log")
            self.children.append(Path(name=child, father=self))
        for file in result[1]:
            self.files.append(File(name=file, path=self))
        print('readed')
        print(self.children, self.files)

    def search_children(self, name: str):
        if not self.pre_read:
            self.read()
        for i in self.children:
            if i.name == name:
                print(i)
                return i
        return False

    def write_self(self) -> None:
        print(self.name)

        tools.file.safe_mkdir(['..', 'data', 'tree'], self.name)

    # TODO:add real operation to fake path system
    def mkdir(self, name: str):
        if not self.pre_read:
            self.read()
        print("log mk")
        if self.search_children(name):
            print("log")
            raise Exceptions.Exceptions.FileAlreadyExistsException().raise_error()
        else:
            child = self.write_child_directory(name)
            self.children.append(child)
            return child

    def write_child_directory(self, name: str):
        if not self.pre_read:
            self.read()
        construct = "../data/tree/"
        for i in self.fathers:
            if i == self:
                continue
            construct += str(i) + "/"

        if os.path.exists(construct + self.name + '/' + name):
            pass
        else:
            os.mkdir(construct + self.name + '/' + name)

        return Path(name=name, father=self)


class File(object):
    def __str__(self) -> str:
        return self.name

    def __init__(self, name, path: Path, extension=".txt") -> None:
        self.name = name
        self.path = path
        self.contents = ''''''
        self.extension = extension
        self.absolute_path = '../data/tree/' + self.path.absolute_path + self.path.name + '/' + self.name + \
                             self.extension

    def read(self) -> str:
        with open(self.absolute_path, 'r') as f:
            result = f.readlines()
            for line in result:
                self.contents += line + "\n"
            f.close()
        return self.contents
        # TODO:finish reading files

    def edit(self) -> None:
        print("notepad '{}'".format(self.absolute_path))
        os.system("{} '{}'".format(default_file_editor, self.absolute_path))

    def write_self(self) -> None:
        with open(self.absolute_path, 'w') as f:
            f.write(self.contents)


if __name__ == '__main__':
    C = Path(name="C", father=None)
    PF = C.search_children("Program Files")
    TP = PF.mkdir("Test Program")
    print(TP.absolute_path)
    TF = File(name="test_file", path=TP, extension=".txt")
    TF.read()
    print('contents', TF.contents)
    TF.edit()
    TF.read()
    print('contents', TF.contents)
