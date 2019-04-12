# Main function

def random_quote(filename):
    import random
    with open(filename) as f:
        quotes = [line.strip() for line in f]
    print()
    print(random.choice(quotes))

random_quote('quotes.txt')