CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюіяєїґ"
TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "i", "ja", "je", "ji", "g")


TRANS = {}
for c, l in zip(CYRILLIC_SYMBOLS, TRANSLATION):
    TRANS[ord(c)] = l
    TRANS[ord(c.upper())] = l.upper()   
    


def normalize(phrase):
    trans_phrase = phrase.translate(TRANS)
    for i in trans_phrase:
        if not i.isalpha() and not i.isdigit():
            trans_phrase = trans_phrase.replace(i, '_')
    return trans_phrase

print(normalize('Разбор строк -- это очень частая задача, которая возникает перед разработчиком в любой сфере и области разработки.')) #для проверки
