words = ['attribute', 'класс', 'функция', "type"]

for word in words:
    try:
        byte_word = eval(f"b'{word}'")
        print(byte_word)
        print(type(byte_word))
    except SyntaxError:
        print("Слово не может быть представлено в виде байт строки")