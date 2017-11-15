import os
import tempfile

class File(object):
    def __init__(self, path):
        #self.path = path.encode('unicode_escape')
        self.path = path
        self.cur_pos = 0

    def write(self, data):
        with open(self.path, 'a') as f:
            s = str(data)
            f.write(s)

    def __add__(self, other):
        filenames = []
        new_file_path = os.path.join(tempfile.gettempdir(), 'file.txt')
        new_file = File(new_file_path)
        filenames.append(self)
        filenames.append(other)
        with open(new_file_path, 'w') as new:
            for f in filenames:
                with open(f.path) as infile:
                    for line in infile:
                        new.write(line)
        return new_file

    def __iter__(self):
        return self

    def __next__(self):
        with open(self.path) as f:
            f.seek(self.cur_pos)
            res = f.readline()
            if res == '':
                self.cur_pos = 0
                raise StopIteration
            self.cur_pos = f.tell()
            return res

    def __str__(self):
        return self.path
