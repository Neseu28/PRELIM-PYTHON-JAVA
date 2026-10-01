# USD to EUR conversion for six products

products = [
    ("Product 1", 25.00),
    ("Product 2", 40.00),
    ("Product 3", 55.00),
    ("Product 4", 75.00),
    ("Product 5", 100.00),
    ("Product 6", 150.00),
]

# Update this rate when the current exchange rate changes.
usd_to_eur = 0.92

print("\n==============================")
print(" USD TO EUR PRICE CONVERTER")
print("==============================")
print("Exchange rate: 1 USD = {:.2f} EUR\n".format(usd_to_eur))
print("{:<15} {:>12} {:>12}".format("Product", "USD Price", "EUR Price"))
print("-" * 41)

for product_name, usd_price in products:
    euro_price = usd_price * usd_to_eur
    print("{:<15} ${:>11.2f} €{:>11.2f}".format(
        product_name, usd_price, euro_price
    ))