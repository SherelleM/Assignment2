
class SandwichMaker:
    def __init__(self, resources):
        self.machine_resources = resources

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        for ingredient in ingredients.keys() & self.machine_resources.keys(): # compares ingredient amt to resource amt
            if ingredients[ingredient] > self.machine_resources[ingredient]:
                print(f"Sorry, there is not enough {ingredient}.")
                return False
            else:
                continue
        return True

    def make_sandwich(self, sandwich_size, order_ingredients):
        for ingredient in order_ingredients.keys() & self.machine_resources.keys():
            self.machine_resources[ingredient] -= order_ingredients[ingredient]
        print(f"{sandwich_size} sandwich is ready. Bon appetit!")
