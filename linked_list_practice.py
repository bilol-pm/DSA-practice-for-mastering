# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None
#
# class LinkedList:
#     def __init__(self):
#         self.head = None
#
#     def append(self, value):
#         new_node = Node(value)
#
#         if self.head == None:
#             self.head = new_node
#             return
#
#         current = self.head
#         while current.next:
#             current = current.next
#
#         current.next = new_node
#     def print_list(self):
#         current = self.head
#         while current:
#             print(current.value, end=" -> ")
#             current = current.next
#         print("None")
#
# my_list = LinkedList()
# my_list.append("10")
# my_list.append("20")
# my_list.append("30")
#
# print("My initial Linked List: ")
# my_list.print_list()
#
#
#


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_Node = Node(value)

        if self.head is None:
            self.head = new_Node
            return

        current = self.head
        while current.next:
            current = current.next

        current.next = new_Node

    def prepend(self, value):
        new_Node = Node(value)
        new_Node.next = self.head
        self.head = new_Node

    def print_list(self):
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")

    def get_length(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def get(self, index):
        current = self.head

        for _ in range(index):
            if current is None:
                return None
            current = current.next

        return current

    def set_value(self, index, value):
        temp = self.get(index)

        if temp:
            temp.value = value
            return True

        return False

my_list = LinkedList()
my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.prepend(4)
my_list.prepend(5)
my_list.prepend(6)
my_list.prepend(7)
my_list.prepend(8)
my_list.prepend(9)
my_list.prepend(10)

print("My LinkedList: ")
my_list.print_list()

length = my_list.get_length()
print(length)

node = my_list.get(2)
if node:
    print("Found element: ", node.value)
else:
    print("Element not found")

print("Before Change: ")
my_list.print_list()

my_list.set_value(5, 85)

print("After change: ")
my_list.print_list()