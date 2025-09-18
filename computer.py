# class Computer initializes and store information about computers
class Computer:

    description: str
    processor: str
    hardDrive: int
    memory: int
    operatingSystem:str
    year_made: int
    price: int
    
    # constructor method initializes parameters for computer
    def __init__(self, description: str,
                    processor_type: str,
                    hard_drive_capacity: int,
                    memory: int,
                    operating_system: str,
                    year_made: int,
                    price: int):
        self.description = description
        self.year_made = year_made
        self.processor = processor_type
        self.hard_drive = hard_drive_capacity
        self.operating_system = operating_system
        self.price = price
        self.memory = memory

    # updates the operating system from an older one to the new one
    def update_OS(self, computer_1):
        new_OS = "MacOS Monterey"
        print("Updating OS", computer_1.operating_system, ", to OS ", new_OS) 
        print("Done.\n")
    
    # updates the price of the computer depending on the year made
    def update_price(self, computer_1):
       new_price = computer_1.price
       if int(computer_1.year_made) < 2000:
                computer_1.price = 0 # too old to sell, donation only
       elif int(computer_1.year_made) < 2012:
                computer_1.price = 250 # heavily-discounted price on machines 10+ years old
       elif int(computer_1.year_made) < 2018:
                computer_1.price= 550 # discounted price on machines 4-to-10 year old machines
       else:
                computer_1.price = 1000 # recent stuff
            
       new_price = computer_1.price
       print("new price: ", new_price)

# computer information entered and printed
def main():
        computer_1 = Computer("Mac Pro (Late 2013)",
        "3.5 GHc 6-Core Intel Xeon E5",
        1024, 
        64,
        "macOS Big Sur", 
        2013, 
        1500)
        print(computer_1.description)

if __name__ == "__main__":
    main()