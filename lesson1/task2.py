words = ['class', 'function', 'method']

for word in words:
    byte_word = eval(f"b'{word}'")
    print(byte_word)
    print(len(byte_word))
    print(type(byte_word))