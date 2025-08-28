def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        return price - (price * discount_percent / 100)
    else:
        return price

price = float(input("Enter original price: "))
discount_percent = float(input("Enter discount percentage: "))

final = calculate_discount(price, discount_percent)
print("Final price:", final)