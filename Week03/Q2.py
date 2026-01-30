cart = ["apple", "banana", "orange", "milk", "mango", "apple", "lemon"]
apple_count = cart.count("apple")
print(f"Number of apples in the cart: {apple_count}")
milk_position = cart.index("milk")
print(f"Position of milk in the cart: {milk_position}")
cart.remove("apple")
print(f"Removed item using pop: {cart.pop()}")
print(f"Is banana in the cart? {'banana' in cart}")
print(f"Final Cart: {cart}")

