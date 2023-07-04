name = input("Welcome to the Fruit Market! What is your name? ")

fruit_prices = {
    "Apple": 2,
    "Grape": 1,
    "Orange": 3
}

fruit_inventory = {
    "Apple": 0,
    "Grape": 0,
    "Orange": 0
}

while True:
    print("\nFruit List:")
    for fruit, price in fruit_prices.items():
        print(f"{fruit}: ${price}")

    selected_fruit = input("Which fruit would you like to buy? ")

    if selected_fruit not in fruit_prices:
        print("Invalid fruit selection. Please try again.")
        continue

    quantity = int(input("How many would you like to buy? "))

    fruit_inventory[selected_fruit] += quantity

    buy_more = input("Do you want to buy more fruit? (Yes/No) ")

    if buy_more.lower() in ["no", "n"]:
        break

print(f"\nReceipt for {name}:")
subtotal = 0

for fruit, quantity in fruit_inventory.items():
    price = fruit_prices[fruit]
    if quantity > 0:
        print(f"{fruit}: {quantity} x ${price} = ${quantity * price}")
        subtotal += quantity * price

tax = subtotal * 0.05
total = subtotal + tax

print(f"\nSubtotal: ${subtotal}")
print(f"Tax (5%): ${tax}")
print(f"Total: ${total}")