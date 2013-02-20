import csv

class Order:
    def __init__(self, order_id):
        self.items = []
        self.order_id = order_id

    def add_item(self, item):
        self.items.append(item)

    def total_price(self):
        total = 0
        for i in self.items:
            total += i.price
        return float(total)

    def total_items(self):
        return len(self.items)

    def __repr__(self):
        return "Order {0} ; {1} items (${2})".format(self.order_id, self.total_items(), self.total_price())

class Item:
    def __init__(self, item_price, item_name, purchase_date, category):
        self.price = float(item_price[1:])
        self.name = str(item_name)
        self.purchase_date = purchase_date
        self.category = category

    def __repr__(self):
        return "Item: {0} (${1})".format(self.name, self.price)


def load_orders_from_csv():
    csv_file = open('amazon.csv', 'rb')
    reader = csv.reader(csv_file)

    orders = {}

    first_row_skipped = False
    for row in reader:
        if not first_row_skipped:
            first_row_skipped = True
            continue
        
        order_id = row[1]
        i = Item(item_price=row[8], item_name=row[2], purchase_date=row[0], category=row[3])
        
        if not order_id in orders:
            orders[order_id] = Order(order_id)
        orders[order_id].add_item(i)
    return orders


orders = load_orders_from_csv()

total_sum = 0
breakdown = {}

for order in orders:
    total_sum += orders[order].total_price()
    for item in orders[order].items:
        if item.category not in breakdown:
            breakdown[item.category] = 0
        breakdown[item.category] += item.price


print breakdown
print total_sum