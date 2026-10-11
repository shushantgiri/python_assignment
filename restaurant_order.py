# Restaurant Order System

menu = {
    "momo": 150,
    "chowmein": 120,
    "pizza": 450,
    "burger": 250,
    "dal bhat": 300,
    "fried rice": 200,
    "tea": 30,
    "coffee": 80
}

order = []


def show_menu():
    print("\nRestaurant Menu")

    for item in menu:
        print(item, "- Rs", menu[item])


def add_item(item, qty):
    order.append([item, qty])
    print(item, "added to order")


def show_bill():
    subtotal = 0

    print("\nYour Order")

    for item in order:
        price = menu[item[0]]
        qty = item[1]
        total = price * qty

        print(item[0], "-", qty, "x Rs", price, "=", total)
        subtotal = subtotal + total

    tax = subtotal * 13 / 100
    total_bill = subtotal + tax

    print("\nSubtotal: Rs", subtotal)
    print("Tax (13%): Rs", tax)
    print("Total Bill: Rs", total_bill)


show_menu()

while True:
    item = input("\nEnter food item (done to stop): ").lower()

    if item == "done":
        break

    if item in menu:
        qty = int(input("Enter quantity: "))

        if qty > 0:
            add_item(item, qty)
        else:
            print("Quantity must be greater than 0")
    else:
        print("Item not in menu")

show_bill()