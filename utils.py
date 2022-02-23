class TxtFileParser:
    def __init__(self, file):
        self.file = file

    def parse(self):
        with open(self.file) as f:
            for line in range(5):
                email, _, password = f.readline().partition(":")
                print("{} {}".format(email, password))
