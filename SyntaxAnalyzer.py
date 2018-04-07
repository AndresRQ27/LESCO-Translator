def endWord(sentence):
    sentence.append(" ")
    return sentence


def wrongWord(word):
    flag = False
    exceptions = ["UCR", "FM", "ADN", "HP", "FMI", "ITCR", "CPP", "OMS", "ISR", "ETS", "BCR", "BN", "BM", "CCSS",
                   "AYA", "ONG"]

    for exc in exceptions:
        print(exc)
        if exc == word:
            flag = True
        else:
            print("No es palabra" + exc)
    return flag

# Doesn't work if at time of printing the conversation this substitutions appear
"""
def fixWord(word):
    y = ""
    exceptions = ["UCR", "FM", "ADN", "HP", "FMI", "ITCR", "CPP", "OMS", "ISR", "ETS", "BCR", "BN", "BM", "CCSS",
                   "AYA", "ONG"]
    pron = ["u ce erre", "efe eme", "adeene", "achepe", "efeemei", "iteceerre", "cepepe", "oemeese", "ieseerre",
            "eteese", "beceerre", "beene", "be eme", "cece ese ese", "a y a", "oenege"]
    for x in range(0, 16):
        if exceptions[x] == word:
            y = pron[x]
    return y
"""