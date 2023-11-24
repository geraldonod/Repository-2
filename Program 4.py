def calculate_max_apples_and_oranges(money, apple_price, orange_price):
    max_apples = money / apple_price
    max_oranges = money / orange_price
    remaining_money = money % apple_price
    return max_apples, max_oranges, remaining_money

def main():
    try:
        money_available = float(input("Welcome to the Gerald's Fruit Store! How much money do you have? "))
        apple_cost = float(input("Great! Now, how much does each apple cost? "))
        orange_cost = float(input("Nice! And how much does each orange cost? "))

        max_apples, max_oranges, remaining_money = calculate_max_apples_and_oranges(
            money_available, apple_cost, orange_cost
        )

        print(f"With {money_available} pesos, you can buy a maximum of:")
        print(f"- {max_apples} apples or")
        print(f"- {max_oranges} oranges.")

        buy_decision = input("Would you like to buy some apples and oranges? (yes or no): ").lower()

        if buy_decision == "yes":
            print(f"Thank you for your purchase! You now have {remaining_money} pesos remaining. Enjoy your fruits!")
        elif buy_decision == "no":
            print("No worries! If you change your mind, we're here. Have a great day!")
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

    except ValueError:
        print("Invalid input. Please enter a valid amount.")

main()