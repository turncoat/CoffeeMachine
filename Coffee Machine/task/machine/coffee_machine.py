class CoffeeMachine:

    def __init__(self):
        self.state = 'main menu'
        self.supplies = {
            "water": 400,
            "milk": 540,
            "coffee beans": 120,
            "disposable cups": 9,
            "money": 550,
        }
        self.recipes = {
            "1": {"ingredients": {"water": 250,
                                  "coffee beans": 16,
                                  "disposable cups": 1},
                  "cost": 4},
            "2": {"ingredients": {"water": 350,
                                  "milk": 75,
                                  "coffee beans": 20,
                                  "disposable cups": 1},
                  "cost": 7},
            "3": {"ingredients": {"water": 200,
                                  "milk": 100,
                                  "coffee beans": 12,
                                  "disposable cups": 1},
                  "cost": 6}
        }
        self.questions = {
            "water": "Write how many ml of water do you want to add:",
            "milk": "Write how many ml of milk do you want to add:",
            "coffee beans": "Write how many grams of coffee beans do you want \
                to add:",
            "disposable cups": "Write how many disposable cups of coffee do \
                you want to add:"
        }

    def status(self):
        print(f"The coffee machine has:")
        for key, value in self.supplies.items():
            print(f"{value} of {key}")

    def buy(self, choice):
        supplies = dict(self.supplies)
        for key, value in self.recipes[choice]["ingredients"].items():
            if value > supplies[key]:
                print(f'Sorry, not enough {key}')
                break
            else:
                supplies[key] -= value
        else:
            self.supplies = supplies
            self.supplies['money'] += self.recipes[choice]['cost']
        self.state = 'main menu'

    def fill(self):
        for key, value in self.questions.items():
            print(value)
            self.supplies[key] += int(input())

    def take(self):
        print(f"I gave you ${self.supplies['money']}")
        self.supplies["money"] = 0

    def command(self, string):
        if self.state == 'main menu':
            if string == 'buy':
                self.state = 'buy menu'
                print('What do you want to buy? 1 - espresso, 2 - latte, \
                    3 - cappuccino, back - to main menu:')
            elif string == 'fill':
                self.fill()
            elif string == 'take':
                self.take()
            elif string == 'remaining':
                self.status()
            elif string == 'exit':
                global status
                status = False
        elif self.state == 'buy menu':
            if string != 'back':
                self.buy(string)
            else:
                self.state = 'main menu'


new_machine = CoffeeMachine()
print('Write action (buy, fill, take, remaining, exit):')
status = True
while status:
    user_input = input()
    new_machine.command(user_input)
