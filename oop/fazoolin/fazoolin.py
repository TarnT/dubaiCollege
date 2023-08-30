class Menu:
    def __init__(self, name, items, start_time, end_time):
        self.name = name
        self.items = items
        self.start_time = start_time
        self.end_time = end_time

    def __str__(self):
        return f"{self.name} menu, available from {self.start_time} to {self.end_time}."
    
    def calculate_bill(self, purchased_items):
        total = 0
        for item in purchased_items:
            if item in self.items.keys():
                total += self.items[item]
        return total
    
class Franchise():
    def __init__(self, address, menus):
        self.address = address
        self.menus = menus

    def __str__(self) -> str:
        return self.address

brunch_menu = {
  'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}

Brunch = Menu("brunch", brunch_menu, "11AM", "4PM")

early_bird_menu = {
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
}

EarlyBird = Menu("Early Bird", early_bird_menu, "3PM", "6PM")

dinner_menu = {
  'crostini with eggplant caponata': 13.00, 'caesar salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
}

Dinner = Menu("Dinner", dinner_menu, "5PM", "11PM")

kids_menu = {
  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}

KidMenu = Menu("Kid Menu", kids_menu, "11AM", "9PM")
print(Brunch.calculate_bill(["pancakes", "coffee", "espresso"]))

all_menus = [Brunch, EarlyBird, Dinner, KidMenu]
flagship_store = Franchise("1232 West End Road", all_menus)
new_installment = Franchise("12 East Mulberry Street", all_menus)
