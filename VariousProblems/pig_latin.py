def pig_latin(phrase):
    piggy = str()
    for word in phrase.split():
        piggy += word[1:] + word[0] + "ay "

    return piggy


print pig_latin("test mctesty face")
