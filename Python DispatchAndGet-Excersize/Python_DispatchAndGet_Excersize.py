
"""Name: Marom Gigi, Dina Balouashvilli
    ID: 318888344, 302583380
    Task: 4
    """


class Item:
    def __init__(self, name='unknown', price=0, calories=0):
        self.name = name
        self.price = price
        self.calories = calories

    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.calories})"

    def __str__(self):
        return f"({self.name}:{self.price}$:{self.calories}cal)"

    def print_item(self):
        return print(repr(self))


class Order:
    def __init__(self, name='unknown', order_list=None, index=None):
        self.name = name
        self.order_list = order_list or []
        if index is not None:
            self.order_list = []
            self.add_items(order_list, [i - 1 for i in index])

    def __repr__(self):
        return f"Order('{self.name}', [{', '.join([repr(item) for item in self.order_list])}])"

    def total(self):
        total = sum([item.price for item in self.order_list])
        print(f"Total: {total}$")

    def calories(self):
        total = sum([item.calories for item in self.order_list])
        print(f"Calories: {total}cal")

    def __str__(self):
        if self.order_list is None:
            return "Order is Empty"
        if self.order_list:
            totalPrice = sum([item.price for item in self.order_list])
            totalCal = sum([item.calories for item in self.order_list])
        else:
            totalPrice = 0
            totalCal = 0
        if self.order_list:
            itemsString = ', '.join([str(item) for item in self.order_list])
            return f"({self.name}, ({itemsString}), total:{totalPrice}$,calories:{totalCal}cal)"
        else:
            return f"({self.name}, no items, total:0$,calories:0cal)"

    def add_items(self, menu, indexesss):
        for index in indexesss:
            if index < 0 or index >= len(menu):
                return print("Error: wrong index")
            else:
                self.order_list.append(menu[index])

    def remove_item(self, index):
        if isinstance(index, list):
            for i in index:
                if 0 <= i < len(self.order_list):
                    del self.order_list[i]
                    print(f"Removed item: {self.order_list[i]}")
        elif 0 <= index < len(self.order_list):
            print(f"Removed item: {self.order_list[index - 1]}")
            del self.order_list[index - 1]

        else:
            print("Error!")



class Restaurant:
    def __init__(self, name='unknown', menu=None, orders=None):
        self.name = name
        self.menu = menu or []
        self.orders = orders or []

    def __repr__(self):
        return f"Restaurant('{self.name}', {self.menu}, {self.orders})"

    def __str__(self):
        return f"Restaurant('{self.name}', {self.menu}, {self.orders})"

    def add_menu(self, item):
        self.menu.append(item)

    def remove_menu(self, index):
        if 0 <= index < len(self.menu):
            removed_item = self.menu.pop(index - 1)
            print(f"Removed item from menu: {removed_item}")
        else:
            print("Error: Invalid index")

    def print_menu(self):
        print("Menu: ")
        for index, item in enumerate(self.menu):
            print(f"{index + 1}) {item.name} {item.price}$ {item.calories}cal")

    def add_orders(self, *orders):
        for a in orders:
            if isinstance(a, Order):
                self.orders.append(a)
            elif isinstance(a, tuple):
                if len(a) == 2:
                    n, i = a
                    self.orders.append(Order(*a))
                else:
                    print(f"Invalid argument: {a}")

            else:
                print(f"Invalid argument: {a}")

    def print_orders(self):
        for order in self.orders:
            print(order)


def min_calories(resturante):
    if not resturante.orders:
        return None
    minimumCaloriesInOrder = resturante.orders[0]
    minimumCalories = sum(item.calories for item in minimumCaloriesInOrder.order_list)
    for order in resturante.orders:
        calories = sum(item.calories for item in order.order_list)
        if calories < minimumCalories:
            minimumCaloriesInOrder = order
            minimumCalories = calories
    return minimumCaloriesInOrder


"""-------------------------------------------------------------------------------------"""
class ItemClass:
    def __init__(self, name, price, calories):
        self.name = name
        self.price = price
        self.calories = calories

    def __str__(self):
        return f'{self.name} - Price: {self.price}$ - Calories: {self.calories}'

    def get(self, prop):
        if prop == 'price':
            return self.price
        elif prop == '__str__':
            return self.__str__
        else:
            return 'Invalid property'

class OrderClass:
    def __init__(self, customer, menu=None, items=None):
        self.customer = customer
        if menu is not None and items is not None:
            self.items = [menu[i-1] for i in items]
        else:
            self.items = []

    def __str__(self):
        return f'Order for {self.customer}\n' + '\n'.join([str(item) for item in self.items])

    def get(self, msg):
        if msg == 'add_items':
            return self.add_items
        elif msg == 'remove_item':
            return self.remove_item
        elif msg == '__str__':
            return self.__str__
        else:
            return 'Invalid property'

    def new(self, name, price, calories):
        return self(name, price, calories)

    def add_items(self, menu, items):
        self.items.extend([menu[i-1] for i in items])

    def remove_item(self, index):
        self.items.pop(index-1)

class RestaurantClass:
    def __init__(self, name, menu=None, orders=None):
        self.name = name
        if menu is not None:
            self.menu = menu
        else:
            self.menu = []
        if orders is not None:
            self.orders = orders
        else:
            self.orders = []

    def __str__(self):
        return f'{self.name} menu:\n' + '\n'.join([str(item) for item in self.menu])

    def get(self, prop):
        if prop == 'add_menu':
            return self.add_menu
        elif prop == 'remove_menu':
            return self.remove_menu
        elif prop == 'print_menu':
            return self.print_menu
        elif prop == 'add_orders':
            return self.add_orders
        elif prop == 'print_orders':
            return self.print_orders
        elif prop == '__str__':
            return self.__str__
        elif prop == 'menu':
            return self.menu
        else:
            return 'Invalid property'

    def add_menu(self, item):
        self.menu.append(item)

    def remove_menu(self, index):
        self.menu.pop(index-1)

    def print_menu(self):
        print(self)

    def add_orders(self, *orders):
        for order in orders:
            self.orders.append(order)

    def print_orders(self):
        if self.orders:
            print("Orders:")
            for i, order in enumerate(self.orders):
                print(f"{i+1}. {order}")
        else:
            print("No orders found!")

def min_calories1(restaurant):
    orders = restaurant.orders
    if not orders:
        print("No orders found!")
        return
    minimum_cal = float('inf')
    minimum_order = None
    for order in orders:
        calories = sum([item.calories for item in order.order_list])
        if calories < minimum_cal:
            minimum_cal = calories
            minimum_order = order
    return minimum_order




def main():
    print("-------------- Home Work 4: --------------")
    print("Question 1:")
    print('\n\n')
    # Question 1:
    item1 = Item('Big Mac', 10, 550)
    print(item1.price)
    item1.print_item()
    print(item1)
    item2 = eval(repr(item1))
    item2.print_item()
    menu = [Item('McDouble', 10, 400), Item('Big_Mac', 12, 550),
            Item("McChicken", 10, 400), Item('Fries', 5, 320),
            Item('Cappuccino', 3, 160), Item('Coca-Cola', 5, 210)]
    order1 = Order('David')
    order1.add_items(menu, (1, 3, 5))
    print(order1)
    order1.remove_item(1)
    order2 = eval(repr(order1))
    order2.name = 'Tali'
    print(order2)
    order3 = Order('Jim', menu, (2, 4, 5, 6))
    print(order3)
    rest1 = Restaurant('BurgerPoint', menu)
    print(rest1)
    rest1.add_menu(Item('Green_Salad', 12, 434))
    rest1.remove_menu(1)
    rest2 = eval(repr(rest1))
    rest2.name = 'BurgerSheva'
    print(rest2)
    rest1.print_menu()
    rest1.add_orders(Order('David', rest1.menu, (2, 4, 5, 6)))
    rest1.add_orders((Order('Tali', rest1.menu, (1, 3, 5))))
    rest1.add_orders((Order('Jim', rest1.menu, (1, 2, 3, 5))))
    rest1.print_orders()
    print(min_calories1(rest1))
    print("------------------------------------------")
    print("Question 2:")
    print('\n\n')
    # Question 2:
    item1 = ItemClass['new']('Big Mac', 10, 550)
    item1['get']('price')
    item1['get']('__str__')()
    menu1 = [ItemClass['new']('McDouble', 10, 400), ItemClass['new']('Big_Mac', 12, 550),
             ItemClass['new']('McChicken', 10, 400), ItemClass['new']('Fries', 5, 320),
             ItemClass['new']('Cappuccino', 3, 160), ItemClass['new']('Coca-Cola', 5, 210)]
    order1 = OrderClass['new']('David')
    order1['get']('add_items')(menu1, (1, 3, 5))
    order1['get']('__str__')()
    order1['get']('remove_item')(1)
    order1['get']('__str__')()
    order2 = OrderClass['new']('Tali', menu1, (2, 4, 5, 6))
    order2['get']('__str__')()
    rest1 = RestaurantClass['new']('BurgerPoint', menu1)
    rest1['get']('__str__')()
    rest1['get']('add_menu')(ItemClass['new']('Green_Salad', 12, 434))
    rest1['get']('remove_menu')(1)
    rest1['get']('print_menu')()
    rest1['get']('add_orders')(OrderClass['new']('David', rest1['get']('menu'), (2, 4, 5, 6)))
    rest1['get']('add_orders')((OrderClass['new']('Tali', rest1['get']('menu'), (1, 3, 5)),
                                OrderClass['new']('Jim', rest1['get']('menu'), (1, 2, 3, 5))))
    rest1['get']('print_orders')()
    min_calories1(rest1)['get']('__str__')()

main()
