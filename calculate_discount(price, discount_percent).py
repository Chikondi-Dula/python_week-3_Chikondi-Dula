# Step 1: Define the function to calculate discount
def calculate_discount(price, discount_percent):
    """
    Calculates the final price after applying a discount.
    If discount_percent >= 20, apply the discount.
    Otherwise, return the original price.
    """
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price

# Step 2: Prompt the user for input
original_price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))

# Step 3: Calculate the final price using the function
final_price = calculate_discount(original_price, discount_percent)

# Step 4: Print the result
if final_price < original_price:
    print(f"Discount applied! The final price is: {final_price}")
else:
    print(f"No discount applied. The price remains: {original_price}")

 # Example
 print("No discount applied. The price remains: {500}")