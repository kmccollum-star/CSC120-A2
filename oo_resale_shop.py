from typing import Dict
from computer import Computer

# contains the methods that allow the resale shop to buy, sell, refurbish, and store inventory
class ResaleShop:

    inventory : list
    new_price = int

    
    def __init__(self):
        self.inventory = [] 

# updates the computer's OS and price in one method and prints error if inventory is empty
    def refurbish(self, computer_1: Computer):
        if computer_1 in self.inventory:
            print("Refurbishing: ", computer_1.description)
            computer_1.update_OS(computer_1) 
            computer_1.update_price(computer_1)
        else: 
            print("Error.")


# checks that inventory has items in it and prints the description of these items
    def print_inventory(self, computer_1: Computer):
        if len(self.inventory) != 0 :
            for self.item in self.inventory:
                print(f"Item Description: - {(self.item.description)}")
        else:
            print("No inventory to display.")
    
# buys computer and adds to resale shop inventory
    def buy(self, computer_1: Computer):
        self.inventory.append(computer_1)
        print("Buying", computer_1.description)
        print("Adding to inventory...")
        print("Done.\n")
        return self.inventory.index(computer_1)


# sells computer and removes from resale shop inventory
    def sell(self, computer_1: Computer):
        print("Selling Item:", computer_1.description)
        self.inventory.remove(computer_1)

# stores computer class and resale shop class and runs different methods
def main():
    mystore = ResaleShop()
    computer_1 = Computer("Mac Pro (Late 2013)",
        "3.5 GHc 6-Core Intel Xeon E5",
        1024, 
        64,
        "macOS Big Sur", 
        2013, 
        1500)
    mystore.print_inventory(computer_1)
    mystore.buy(computer_1)
    mystore.sell(computer_1)
    mystore.refurbish(computer_1)
    mystore.print_inventory(computer_1)
    

main()