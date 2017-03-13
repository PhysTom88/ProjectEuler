def ispalindrome(word):
    return word == word[::-1]


def ispalindrome_other(word):
    iterate = len(word) / 2 if len(word) % 2 == 0 else (len(word) / 2) + 1
    for i in xrange(iterate):
        if word[i] == word[(i + 1) * -1]:
            continue
        return False

    return True


# Shorter pythonic function
print ispalindrome('test')
print ispalindrome('racecar')
print ispalindrome('saippuakivikauppias')
# Longer more involved function
print ispalindrome_other('test')
print ispalindrome_other('racecar')
print ispalindrome_other('saippuakivikauppias')
