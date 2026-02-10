import data
from sandwich_maker import SandwichMaker
from cashier import Cashier


# Make an instance of other classes here
resources = data.resources
recipes = data.recipes
sandwich_maker_instance = SandwichMaker(resources)
cashier_instance = Cashier()



def main():
    # Take users input
    while True:
        user_input = input("What would you like? (small/ medium/ large/ off/ report): ")

        if user_input in recipes.keys():
            ingredients = recipes[user_input]["ingredients"]
            if sandwich_maker_instance.check_resources(ingredients):  # inputs list of ingredients for selected size
                if cashier_instance.transaction_result(cashier_instance.process_coins(), recipes[user_input]["cost"]):
                    sandwich_maker_instance.make_sandwich(user_input, ingredients)

        if user_input == "report":
            print(f"Bread: {resources["bread"]} slices(s)")
            print(f"Ham: {resources["ham"]} slices(s)")
            print(f"Cheese: {resources["cheese"]} ounces(s)")

        if user_input == "off":
            break

if __name__=="__main__":
    main()
