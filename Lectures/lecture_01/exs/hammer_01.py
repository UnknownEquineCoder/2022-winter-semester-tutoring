cart = ["milk", "sugar", "milk", "x3", "sugar", "beer", "x12", "bread", "milk", "butter",
        "x2", "salad", "x3", "juice", "sugar", "x2", "juice", "butter", "sugar", "flour"]

pricelist = {"milk": 1.3, "sugar": 1.6, "beer": 1.25, "bread": 2.6,
             "butter": 1.99, "salad": 0.89, "flour": 1.2, "juice": 1.2}


cart_with_quantities = {}


# >>> letters = ['a', 'b', 'c']
# >>> enumerate(letter)
# [(0, 'a'), (1, 'b'), (2, 'c')]

for idx, item in enumerate(cart):
    if item.startswith('x'):
        prefix, *quantity = item
        quantity = ''.join(quantity)
        quantity = int(quantity)

        # access the value that came before item
        # increment its count by quantity
        cart_with_quantities[cart[idx - 1]] += quantity - 1
    else:
        # If the item is already present: increase the number by the quantity
        if item in cart_with_quantities:
            cart_with_quantities[item] += 1
        else:
            cart_with_quantities[item] = 1


total_price = 0

for item, quantity in cart_with_quantities.items():
    total_price += (pricelist[item] * quantity)

print(total_price)
