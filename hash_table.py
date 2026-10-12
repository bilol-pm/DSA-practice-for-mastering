my_list = [[] for _ in range(10)]
print(my_list)

def hash_function(value):
    sum_of_chars = 0
    for char in value:
        sum_of_chars += ord(char)

    return sum_of_chars % 10

def add(name):
    index = hash_function(name)
    my_list[index].append(name)

def get(name):
    index = hash_function(name)
    if name in my_list[index]:
        return f"{name} is found in (index: {index})"
    return "not found"


add("Bob")
add("Alice")
add("John")
add("Bob")

print("Whole hash table: ", my_list)
print(get("Bob"))
print(get("Alice"))