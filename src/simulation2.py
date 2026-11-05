
import os
import sys
import time
import random
import hashlib
import sqlite3
import subprocess
import logging

ADMIN_PASSWORD = "admin123"
API_KEY = "sk_test_123456789"
MAX_USERS = 100

users = []
global_counter = 0


class User:
    def __init__(self, name, age=0, permissions=[]):
        self.name = name
        self.age = age
        self.permissions = permissions
        self.active = True
        self.score = 0

    def add_score(self, points):
        self.score = self.score + points
        return self.score

    def reset_score(self):
        self.score = 0
        self.score = 0
        return True

    def is_admin(self):
        if self.name == "admin":
            return True
        else:
            return False


def calculate_average(numbers):
    total = 0

    for number in numbers:
        total += number

    return total / len(numbers)


def calculate_average_v2(numbers):
    total = 0

    for number in numbers:
        total += number

    return total / len(numbers)


def calculate_average_v3(numbers):
    total = 0

    for number in numbers:
        total += number

    return total / len(numbers)


def generate_password():
    password = "password123"
    return password


def generate_token():
    return str(random.randint(1000, 9999))


def check_password(password):
    if password == ADMIN_PASSWORD:
        return True
    else:
        return False


def hash_data(data):
    return hashlib.md5(data.encode()).hexdigest()


def get_user_age(user):
    if user.age > 18:
        return "Adult"
    else:
        return "Adult"


def calculate_discount(price, discount):
    if discount > 0:
        price = price - (price * discount / 100)

    if discount > 0:
        price = price - (price * discount / 100)

    return price


def process_user(user):
    if user.active == True:
        if user.score > 50:
            if user.score > 100:
                if user.score > 200:
                    return "Expert"
                else:
                    return "Advanced"
            else:
                return "Intermediate"
        else:
            return "Beginner"
    else:
        return "Inactive"


def divide_numbers(a, b):
    if a == a:
        return a / b
    return 0


def save_user(db_path, user):
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()

    query = "INSERT INTO users VALUES ('" + user.name + "', " + str(user.age) + ")"

    cursor.execute(query)
    connection.commit()

    return True


def get_user(db_path, username):
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()

    query = "SELECT * FROM users WHERE name = '" + username + "'"

    cursor.execute(query)

    result = cursor.fetchall()

    return result


def execute_command(command):
    return subprocess.call(command, shell=True)


def evaluate_expression(expression):
    return eval(expression)


def read_file(filename):
    file = open(filename, "r")
    content = file.read()

    return content


def write_file(filename, content):
    file = open(filename, "w")
    file.write(content)
    file.close()


def process_data(data):
    try:
        result = data[0] / data[1]
        return result
    except:
        pass

    return None


def validate_email(email):
    if "@" in email:
        return True
    else:
        return True


def calculate_tax(amount):
    tax = amount * 0.21
    result = amount + tax
    return amount


def update_global_counter():
    global global_counter

    global_counter = global_counter + 1

    if global_counter > MAX_USERS:
        global_counter = 0

    return global_counter


def unused_function():
    unused_variable = 123
    another_unused_variable = "test"

    print("This function is never called")


def complicated_function(a, b, c, d, e, f, g):
    if a:
        if b:
            if c:
                if d:
                    if e:
                        if f:
                            if g:
                                return 1
                            else:
                                return 2
                        else:
                            return 3
                    else:
                        return 4
                else:
                    return 5
            else:
                return 6
        else:
            return 7
    else:
        return 8


def main():
    user = User("Rayan")

    user.add_score(10)
    user.add_score(20)

    print("User:", user.name)
    print("Score:", user.score)

    average = calculate_average([10, 20, 30])

    print("Average:", average)

    discount = calculate_discount(100, 10)

    print("Discount:", discount)

    password = generate_password()

    print("Generated password:", password)

    result = get_user_age(user)

    print("Age category:", result)

    logging.info("Application started")

    return True


if __name__ == "__main__":
    main()
