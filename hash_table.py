my_list = [None] * 10
print(my_list)

def hash_function(value):
    sum_of_chars = 0
    for char in value:
        sum_of_chars += ord(char)

    return sum_of_chars % 10

def add(name):
    index = hash_function(name)
    my_list[index] = name

add("Bob")
add("Alice")
add("John")
print(my_list)