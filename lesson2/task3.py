import yaml

data = {
    '1': [1, 's'],
    '2': 2,
    '3': {'€': 3.1, '¢': 3.2}
}

with open('file.yaml', 'w', encoding='utf-8') as f:
    yaml.dump(data, f, default_flow_style=True, allow_unicode=True)

with open('file.yaml', 'r', encoding='utf-8') as f:
    content = yaml.load(f, Loader=yaml.FullLoader)
    print(content)

print(data == content)