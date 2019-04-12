
def checker(filename):
    with open(filename) as f:
        for line in f:
            line = line.strip()
            print(line if line[0] == line[0].lower() else 1)
    pass

checker('quotes.txt')