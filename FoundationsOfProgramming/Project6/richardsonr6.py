class Deque:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def add_front(self, item):
        self.items.insert(0, item)

    def add_rear(self, item):
        self.items.append(item)

    def remove_front(self):
        return self.items.pop(0) if not self.is_empty() else None

    def remove_rear(self):
        return self.items.pop() if not self.is_empty() else None

    def peek_front(self):
        return self.items[0] if not self.is_empty() else None

    def peek_rear(self):
        return self.items[-1] if not self.is_empty() else None

    def display(self):
        print(self.items)

# create a new Deque object
my_deque = Deque()

# prompt the user for input and add elements to the deque
while True:
    item = input("Enter an item to add to the deque (press Enter to stop): ")
    if not item:
        break
    my_deque.add_rear(item)

# display the contents of the deque
print("Contents of the deque:")
my_deque.display()

# insert an element at the beginning of the deque
my_deque.add_front("New First Item")
print("Contents of the deque after adding element at the front:")
my_deque.display()

# insert an element at the end of the deque
my_deque.add_rear("New Last Item")
print("Contents of the deque after adding element at the rear:")
my_deque.display()