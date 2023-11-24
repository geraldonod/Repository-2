def calculate_total_amount(apple_quantity, orange_quantity):
    apple_price = 20
    orange_price = 25
    total_amount = (apple_quantity * apple_price) + (orange_quantity * orange_price)
    return total_amount

def main():
    try:
        user_name = input("Hi there! Welcome to Gerald's Fruit Store! What's your name? ")

        apple_qty = int(input(f"Nice to meet you {user_name}! How many apples would you like to buy?: "))
        orange_qty = int(input("Now, how many oranges would you want to buy?: "))

        total_payment = calculate_total_amount(apple_qty, orange_qty)

        confirm_purchase = input(f"{user_name}, the price of the fruits you want to buy is {total_payment} pesos. Are you sure you want to purchase these fruits? (yes or no): ").lower()

        if confirm_purchase == 'yes':
            print(f"Thank you for your purchase {user_name}! Enjoy your fruits!")
        elif confirm_purchase == 'no':
            print(f"No problem, {user_name}. Feel free to explore more about the world of fruits!")
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

    except ValueError:
        print("Invalid input. Please enter a valid response.")

main()