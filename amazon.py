import csv
import locale
from decimal import Decimal


locale.setlocale(locale.LC_ALL, '')


class Order:
    def __init__(self, order_id):
        self.items = []
        self.order_id = order_id

    def add_item(self, item):
        self.items.append(item)

    @property
    def total_price(self):
        total = 0
        for i in self.items:
            total += i.price * i.quantity
        return float(total)

    @property
    def total_items(self):
        return len(self.items)

    @property
    def order_date(self):
        return self.items[0].purchase_date

    @property
    def categories(self):
        return {i.category for i in self.items}

    def __repr__(self):
        return "Order {}, {} items (${}) [{}]\nItems: {}".format(
            self.order_date, self.total_items, self.total_price,
            ', '.join(self.categories),
            ', '.join([i.name for i in self.items]))


class Item:
    def __init__(self, item_price, item_name, purchase_date, category,
                 quantity):
        self.price = Decimal(item_price[1:])
        self.name = str(item_name)
        self.purchase_date = purchase_date
        self.category = category
        self.quantity = int(quantity)

    def __repr__(self):
        return "Item: {} (${}) x{}".format(self.name, self.price,
                                              self.quantity)


def load_orders_from_csv():
    csv_file = open('amazon.csv', 'r')
    reader = csv.DictReader(csv_file)

    orders = {}

    for row in reader:
        order_id = row['Order ID']
        i = Item(item_price=row['Purchase Price Per Unit'],
                 item_name=row['Title'],
                 purchase_date=row['Order Date'],
                 category=row['Category'],
                 quantity=row['Quantity'])

        if not order_id in orders:
            orders[order_id] = Order(order_id)
        orders[order_id].add_item(i)
    return orders


def main():
    orders = load_orders_from_csv()
    total_sum = 0
    breakdown = {}

    for order in orders:
        total_sum += orders[order].total_price

        for item in orders[order].items:
            if item.category not in breakdown:
                breakdown[item.category] = 0
            breakdown[item.category] += item.price

    print("\nCategory breakdown:")
    print("-------------------")
    for category, price in breakdown.items():
        if category == '':
            category = 'None'
        print("{}: {}".format(category, locale.currency(price,
                                                          grouping=True)))

    print("\nTotal spent:")
    print("------------")
    print("{}".format(locale.currency(total_sum, grouping=True)))

    print("\nOrders:")
    print("-------")
    for order in orders.values():
        print(order)
        print()


if __name__ == '__main__':
    main()
