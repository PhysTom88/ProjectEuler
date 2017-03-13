
def reverse(word):
    return word[::-1]


def recursive_reverse(word):
    if len(word) <= 1:
        return word

    return recursive_reverse(word[1:]) + word[0]


print reverse("test")
print recursive_reverse("test")
