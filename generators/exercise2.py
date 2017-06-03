class ReadVisits:
    def __init__(self, data_path):
        self.data_path = data_path

    def __iter__(self):
        with open(self.data_path) as f:
            for line in f:
                yield int(line)


if __name__ == '__main__':
    reader = ReadVisits('./data.txt')

    for line in reader:
        print(line)
