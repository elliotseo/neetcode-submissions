class StoreItem:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price
        
    def display_name(self) -> None:
        print(self.name)

    def display_price(self) -> None:
        print(self.price)
    



chips = StoreItem("Chips", 1.99) # Don't modify this line

# TODO: Access the attributes of the chips object and display them
chips.display_name()
chips.display_price()


