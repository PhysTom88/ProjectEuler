
def word_counter(phrase, file=False):
    if not file:
        return len(phrase.split())

    with open(phrase, 'rb') as f:
        return len(f.readlines())


print word_counter("reverse.py", file=True)
