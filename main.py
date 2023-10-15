from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

run = True
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
while run:
    prompt = input(f"What would you like? ({menu.get_items()}): ").lower()
    if prompt == "off":
        run = False
    elif prompt == "report":
        coffee_maker.report()
        money_machine.report()
    elif menu.find_drink(prompt) is not None:
        menu_item = menu.find_drink(prompt)
        if coffee_maker.is_resource_sufficient(menu_item):
            if money_machine.make_payment(menu_item.cost):
                coffee_maker.make_coffee(menu_item)
