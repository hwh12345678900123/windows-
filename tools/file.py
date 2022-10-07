import os


def safe_mkdir(path: list, name: str) -> None:
    construct = '.'
    for i in path:
        if not os.path.exists(construct + "/" + i):
            os.mkdir(construct + "/" + i)
        construct += '/' + i
    if not os.path.exists(construct + "/" + name):
        os.mkdir(construct + "/" + name)


'''
    usage:
    safe_read(path.absolute_path)
'''


def safe_read(path: str) -> list:
    dirs = os.listdir('../data/tree/' + path)
    result = [[], []]
    for file_or_path in dirs:
        if os.path.isdir(file_or_path):
            result[1].append(file_or_path)
        else:
            result[0].append(file_or_path)
    return result


if __name__ == '__main__':
    safe_mkdir(path=['test', 'test'], name='test')
