class Node:
    def __init__(self, song_name):
        self.song_name = song_name
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, song_name):
        new_node = Node(song_name)

        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next

        current.next = new_node

    def prepend(self, song_name):
        new_node = Node(song_name)
        new_node.next = self.head
        self.head = new_node

    def print_playlist(self):
        current = self.head
        while current:
            print(current.song_name, end=" -> ")
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

    def insert(self, index, song_name):
        if index < 0 or index > self.get_length():
            return False

        if index == 0:
            self.prepend(song_name)
            return True

        if index == self.get_length():
            self.append(song_name)
            return True

        new_node = Node(song_name)
        temp = self.get(index - 1)

        new_node.next = temp.next
        temp.next = new_node
        return True



print("My Playlist: ")
playList = LinkedList()
playList.append("Hastamanu")
playList.append("Sani sevaman")
playList.append("Qaro kozim")
playList.append("Laylo")
playList.append("Sen ketma")
playList.prepend("Bu sehir")


print("Before change: ")
playList.print_playlist()
print("After change: ")
playList.insert(3, "Elif dedim")
playList.print_playlist()
