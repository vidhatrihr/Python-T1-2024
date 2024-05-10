string_1 = "dog"
string_2 = "cat"

# pair of letters
[string_1[i] + string_2[i] for i in range(len(string_1))]


# ordinal differnce of both the string
[ord(string_1[i]) - ord(string_2[i]) for i in range(len[string_1])]

# odinal diff btw string
sum(ord(string_1[i]) - (ord(string_2[i])) for i in range((len(string_1))))

# ordinal difference btw 2 strn
sum(ord(string_1[i]) - (ord(string_2[i])) for i in range((len(string_1))))

# similarly

def distance(word_1, word_2):
    if len(word_1) != len(word_2):
        return -1
    sum(ord(word_1[i]) - (ord(word_2[i])) for i in range((len(word_1))))