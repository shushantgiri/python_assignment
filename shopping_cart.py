# Shopping Cart

products = {
    "apple": {"price": 50, "qty": 10},
    "banana": {"price": 10, "qty": 20},
    "milk": {"price": 120, "qty": 5},
    "bread": {"price": 80, "qty": 3},
    "rice": {"price": 150, "qty": 8},
    "eggs": {"price": 20, "qty": 30}
}

cart = {}


def add_to_cart(item, qty):
    if qty <= products[item]["qty"]:
        products[item]["qty"] = products[item]["qty"] - qty

        if item in cart:
            cart[item] = cart[item] + qty
        else:
            cart[item] = qty

        print(item, "added to cart")
    else:
        print("Only", products[item]["qty"], item, "available")


def show_cart():
    total = 0

    print("\nYour Shopping Cart")

    for item in cart:
        price = products[item]["price"]
        qty = cart[item]
        amount = price * qty

        print(item, "-", qty, "x Rs", price, "=", amount)
        total = total + amount

    print("Total Bill: Rs", total)


print("Available Products:")

for item in products:
    print(item, "- Rs", products[item]["price"],
          "- Stock:", products[item]["qty"])


while True:
    item = input("\nEnter product name (done to stop): ").lower()

    if item == "done":
        break

    if item in products:
        qty = int(input("Enter quantity: "))

        if qty > 0:
            add_to_cart(item, qty)
        else:
            print("Quantity must be greater than 0")
    else:
        print("Product not found")


show_cart()