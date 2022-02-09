words = ['разработка', 'администрирование', 'protocol', "standard"]

for word in words:
    byte_word = word.encode("utf-8")
    print(byte_word, type(byte_word))
    new_word = byte_word.decode("utf-8")
    print(new_word, type(new_word))