import json

class InventoryManager:
    def __init__(self):
        self.inventory = self.load_inventory()

    def load_inventory(self):
        try:
            with open("inventory.json", "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    def save_inventory(self):
        with open("inventory.json", "w") as file:
            json.dump(self.inventory, file, indent=2)

    def display_inventory(self):
        print("\nCurrent Inventory:")
        for item, quantity in self.inventory.items():
            print(f"{item}: {quantity}")

    def add_item(self, item, quantity):
        if item in self.inventory:
            self.inventory[item] += quantity
        else:
            self.inventory[item] = quantity
        self.save_inventory()
        print(f"\nAdded {quantity} {item}(s) to the inventory.")

    def sell_item(self, item, quantity):
        if item in self.inventory and self.inventory[item] >= quantity:
            self.inventory[item] -= quantity
            self.save_inventory()
            print(f"\nSold {quantity} {item}(s).")
        else:
            print(f"\nInsufficient stock of {item}.")

def main():
    manager = InventoryManager()

    while True:
        print("\nOptions:")
        print("1. Display Inventory")
        print("2. Add Item to Inventory")
        print("3. Sell Item")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            manager.display_inventory()
        elif choice == "2":
            item = input("Enter item name: ")
            quantity = int(input("Enter quantity to add: "))
            manager.add_item(item, quantity)
        elif choice == "3":
            item = input("Enter item name: ")
            quantity = int(input("Enter quantity to sell: "))
            manager.sell_item(item, quantity)
        elif choice == "4":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()

