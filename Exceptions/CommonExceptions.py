import os
import sys
import time

sys.path.append("../tools")
import tools


class CommonExceptions(object):
    def __init__(self, name="BaseException", message="BaseException"):
        self.name = name
        self.message = message

    def raise_error(self, description=""):
        return Exception(self.name + ":" + self.message + description)


class LoggedCommonExceptions(CommonExceptions):
    def __init__(self, name="BaseLoggedException", message="BaseLoggedException"):
        super().__init__(name, message)
        self.name = name
        self.message = message

    def raise_error(self, description="", path=None, filename='test.log'):
        if path is None:
            path = ['./log', 'test']
        path_construct = ''
        message = self.name + ":" + self.message + description
        for i in path:
            path_construct += i + '/'
        tools.file.safe_mkdir(path, time.strftime("%Y%m%d", time.localtime()))
        with open("log/test/" + str(time.strftime("%Y%m%d", time.localtime()) + '/test.log'), 'a') as f:
            f.write(message)
            f.write('\n')
        return Exception(message)


class FileAlreadyExistsException(LoggedCommonExceptions):
    def __init__(self, name="BaseFileAlreadyExistsException", message="BaseFileAlreadyExistsException"):
        super().__init__(name=name, message=message)

    def raise_exception(self, description="", path=None, filename='test.log'):
        return super().raise_error(description=description + 'file already exists', path=path, filename=filename)


class FileNotFoundException(LoggedCommonExceptions):
    def __init__(self, name="BaseFileNotFoundException", message="BaseFileNotFoundException"):
        super().__init__(name=name, message=message)

    def raise_exception(self, description="", path=None, filename='test.log'):
        return super().raise_error(description=description + 'file not found', path=path, filename=filename)


if __name__ == '__main__':
    logging = LoggedCommonExceptions()
    logging.raise_error()
