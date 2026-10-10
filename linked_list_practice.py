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
my_list = LinkedList()
my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.prepend(4)

print("My LinkedList: ")
my_list.print_list()