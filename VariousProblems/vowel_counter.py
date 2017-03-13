
def vowel_counter(word):
    vowels = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    for letter in word:
        if letter in vowels.keys():
            vowels[letter] += 1

    return vowels


print vowel_counter("Counting all the vowels")
