import json


def write_order_to_json(item, quantity, price, buyer, date):
    data_dict = {
        'item': item,
        'quantity': quantity,
        'price': price,
        'buyer': buyer,
        'date': date
    }

    with open('orders.json', 'w', encoding='utf-8') as f:
        dump = json.dumps(data_dict, indent=4)
        f.write(dump)


write_order_to_json('Beer', 3, 150.00, 'Jon', '19.02.2022')
