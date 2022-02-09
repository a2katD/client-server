from chardet import detect
lines = ['сетевое программирование\n', 'сокет\n', 'декоратор\n']

with open('test_file.txt', 'w', encoding='utf-8') as f:
    f.writelines(lines)

# memory loss!
with open('test_file.txt', 'rb') as f:
    content = f.read()
encoding = detect(content)['encoding']

with open('test_file.txt', 'r', encoding=encoding) as f:
    for line in f:
        print(line, end="")
