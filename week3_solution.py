class FileReader(object):
    def __init__(self, path):
        self.path = path

    def read(self):
        try:
            with open(self.path, 'r') as f:
                output = f.read()
        except IOError:
            output = ""
        return output
