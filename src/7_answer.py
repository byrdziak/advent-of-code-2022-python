# https://adventofcode.com/2022/day/5


import os
from typing import Union
from functions import read_file

from pprint import pprint as pp
from dataclasses import dataclass


class FolderAlreadyExistException(Exception):
    pass


class MissingFolderException(Exception):
    pass


class Filesystem:
    def __init__(self):
        self._dirs = {'/': Directory([])}
        self._current_path = '/'

    @property
    def dirs(self):
        return self._dirs

    def ls(self):
        child_keys = list(
            filter(lambda x: self._current_path in x and self._current_path != x, self._dirs.keys()))
        for key in child_keys:
            splited = key.split(self._current_path)
            value = splited[1]
            if value != '':
                pp(f'd {splited[1]}')
            if self._current_path != '/':
                pp('..')
        pp('.')

        for file in self._dirs[self._current_path].content:
            pp(f'f {file.name}')

    def pwd(self):
        pp(self._current_path)

    def cd(self, path: str):
        if path[0] != '/' and path != '..':
            path_to_set = self._current_path + path + '/'
        elif path[0] == '/':
            path_to_set = path
            if path[-1] != '/':
                path_to_set += '/'
        elif path == '.':
            pass
        elif path == '..':
            current_path_splitted = self._current_path.split('/')
            filtered = list(filter(None, current_path_splitted))

            if len(filtered) > 1:
                path_to_set = '/' + '/'.join(filtered[:-1]) + '/'
            elif len(filtered) == 1:
                path_to_set = '/'
            else:
                raise MissingFolderException

        if path_to_set in self._dirs.keys():
            self._current_path = path_to_set
        else:
            raise MissingFolderException

    def mkdir(self, path: str, safe: bool = False):
        dir_to_create_path = self._current_path + path + '/'
        if dir_to_create_path not in self._dirs.keys():
            self._dirs[dir_to_create_path] = Directory([])
        elif dir_to_create_path in self._dirs.keys() and safe:
            raise FolderAlreadyExistException
        else:
            pass

    def touch(self, name: str, size: int):
        self._dirs[self._current_path].content.append(File(name, size))
        self._dirs[self._current_path].content = list(
            set(self._dirs[self._current_path].content))


@dataclass
class File:
    name: str
    size_bytes: int

    def __hash__(self):
        return hash((self.name, self.size_bytes))


@dataclass
class Directory:
    # content: list[Union[File, 'Directory']]
    content: list[File]

    def get_total_size(self):
        total_size = 0

        for element in self.content:
            total_size += element.size_bytes
            # if type(element) == File:
            #     total_size += element.size_bytes

            # elif type(element) == Directory:
            #     total_size = element.get_total_size()

        return total_size

    def ls(self):
        return self.content


def parse_commands(rows):
    pass


def main():
    file = read_file('src/7_input.txt')
    rows = file.split(os.linesep)

    fs = Filesystem()

    fs.mkdir('bcfwbq')
    fs.touch('cmss', 14779)
    fs.mkdir('ctctt')
    fs.touch('gpbswq.njr', 101350)
    fs.touch('mglrchsr', 270744)
    fs.touch('qtvftbl', 260405)

    fs.cd('bcfwbq')
    fs.mkdir('gpbswq')
    fs.touch('lpn.qjd', 172204)

    fs.mkdir('abc')
    fs.cd('abc')

    # fs.cd('/lol')
    # fs.mkdir('ctctt')

    pp('aaa')
    fs.ls()
    pp('xxxx')
    fs.pwd()
    pp('bbb')

    total_size = 0
    for k, v in fs.dirs.items():
        size = v.get_total_size()
        if size > 100000 and k != '/':
            print(k)
            print(size)

    z = [File('aa', 22), File('aa', 22)]
    print(set(z))

    fs.pwd()
    fs.cd('..')
    fs.pwd()

    fs.cd('..')
    fs.pwd()

    # print(rows)


if __name__ == '__main__':
    main()
