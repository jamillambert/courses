def reverseWordsInString(string):
    # Write your code here.
    new_string = ""
    if string == "":
        return string
    word = string[0]
    for a in string[1:]:
        if (a == " ") == (word[0] == " "):
            word += a
        else:
            new_string = add_word(word, new_string)
            word = a
    new_string = add_word(word, new_string)
    return new_string


def add_word(word, string):
    if string == "":
        return word
    else:
        return word + string
