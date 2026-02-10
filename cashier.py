class Cashier:
    def __init__(self):
        pass

    def process_coins(self):
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""
        print("Please insert coins.")
        large_dollars = float(input("How many large dollars?: ")) * 1
        half_dollars = float(input("How many half dollars?: ")) * 0.5
        quarters = float(input("How many quarters?: ")) * 0.25
        nickels = float(input("How many nickels?: ")) * 0.05

        return large_dollars + half_dollars + quarters + nickels


def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""
        if coins < cost:
            print(f"Sorry, that is not enough money. Money refunded.")
            return False
        else:
            change = round((coins - cost), 2)
            print(f"Here is ${change} in change.")
            return True
