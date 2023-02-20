
# def main():

#     class Deque:
        
#         def __init__(self, data, add):
#             self.data = data
#             self.add = add
        
#         # def add_begin(self):
#         #     return self.data.appendleft()

#         # def add_end(self):
#         #     return self.data.append()

#         def display(self):
#             self.data = input("Add to the deque: ")
#             if input == "left":
#                 self.data.appendleft()
#             elif input == "right":
#                 self.data.append()

# main()

from collections import deque

people = ["Mario", "Luigi", "Toad"]
queue = deque(people)