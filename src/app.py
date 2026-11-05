
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            return False

        self.balance += amount
        return True

    def withdraw(self, amount):
        if amount <= 0:
            return False

        if self.balance < amount:
            return False

        self.balance -= amount
        return True

    def get_balance(self):
        return self.balance


def calculate_discount(price, discount):
    if discount < 0:
        return price

    return price - (price * discount / 100)


def calculate_discount_v2(price, discount):
    if discount < 0:
        return price

    return price - (price * discount / 100)


def calculate_discount_v3(price, discount):
    if discount < 0:
        return price

    return price - (price * discount / 100)


def calculate_tax(price):
    tax = price * 0.21
    return price + tax


def calculate_shipping(price):
    if price > 100:
        return 0

    return 10


def calculate_total(price, discount, shipping):
    discounted_price = calculate_discount(price, discount)
    total = discounted_price + shipping

    return total


def is_adult(age):
    if age >= 18:
        return True

    return False


def format_username(username):
    return username.lower().strip()


def generate_report(account):
    report = "Owner: " + account.owner
    report += "\nBalance: " + str(account.balance)

    return report


def unused_function():
    result = 10 * 20
    return result


def complicated_calculation(a, b, c, d):
    if a > 0:
        if b > 0:
            if c > 0:
                if d > 0:
                    return a + b + c + d
                else:
                    return a + b + c
            else:
                return a + b
        else:
            return a
    else:
        return 0
