# stack = []
#
# def reverse(text):
#     for letter in text:
#         stack.append(letter)
#
#
#     reversed_text = ''
#
#     while len(stack) > 0:
#         reversed_text += stack.pop()
#
#     return reversed_text
#
# print(reverse("hello world"))

import time


class Cinema:
    def __init__(self, name):
        self.name = name
        self.queue = ["Karim", "Asad", "Timur-chapchachap"]

    def add_customers(self, customer):
        self.queue.append(customer)
        return len(self.queue)

print("Welcome to the cinema! Please enter your name to get a queue!")
customer_name = input("Enter your name: ")

cinema = Cinema(customer_name)
customer_position = cinema.add_customers(customer_name)
print(f"Your position is {customer_position}")
print(f"Starting queue: {cinema.queue}")
print("-" * 40)

while len(cinema.queue) > 1:
    time.sleep(5)

    served_person = cinema.queue.pop(0)

    customer_position -= 1

    print(f"{served_person} is now served, now your turn is {customer_position} ")

print("-" * 40)
print(f"Welcome {customer_name}, now it is your turn to take a ticket!")




