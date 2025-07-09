# Billing System using Tuples

# Fixed product list (tuple of tuples)
products = (
    ("Apple", 30),
    ("Milk", 45),
    ("Shampoo", 120),
    ("Jeans", 1500),
    ("Book", 250),
    ("Phone Charger", 600)
)

# Print product catalog
print("🛍️  Available Products:")
for name, price in products:
    print(f"- {name}: ₹{price}")

# Ask user to enter items they bought
selected_items = input("\nEnter items bought (comma-separated): ").split(",")

# Clean input
selected_items = [item.strip().title() for item in selected_items]

# Initialize bill
total = 0
bought = []

# Match items and calculate total
for name, price in products:
    if name in selected_items:
        total += price
        bought.append((name, price))

# Print final bill
print("\n🧾 Your Bill:")
for name, price in bought:
    print(f"{name}: ₹{price}")

print(f"Total: ₹{total}")

# Show expensive items (> ₹500)
print("\n💸 Expensive Items (₹500+):")
for name, price in bought:
    if price >= 500:
        print(f"{name}: ₹{price}")
