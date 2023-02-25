import random
from datetime import datetime

def random_numbers():
    unsorted_list = list(range(0, 1000))
    rand_numbers = []
    for x in unsorted_list:
        rand_numbers.append(random.randint(0, 10))

    return rand_numbers

def bubble(list_one):
    indexing_length = len(list_one)-1
    sorted = False

    while not sorted:
        sorted = True
        for i in range(0, indexing_length):
            if list_one[i] > list_one[i+1]:
                sorted = False
                list_one[i], list_one[i+1] = list_one[i+1], list_one[i]

    return list_one


def selection(list_two):
    indexing_length = range(0, len(list_two)-1)

    for i in indexing_length:
        min_value = i
        for j in range(i+1, len(list_two)):
            if list_two[j] < list_two[min_value]:
                min_value = j
        if min_value != i:
            list_two[min_value], list_two[i] = list_two[i], list_two[min_value]

    return list_two

def main():

    numbers = random_numbers()
    start_time = datetime.now()
    sorted_numbers_bubble = bubble(numbers)
    end_time = datetime.now()
    sorting_time_bubble = int((end_time - start_time).total_seconds() * 1000)
    print(sorted_numbers_bubble)
    print(f"Time to sort using the bubble method: {sorting_time_bubble} milliseconds")

    print("\n")
    
    start_time = datetime.now()
    sorted_numbers_selection = selection(numbers)
    end_time = datetime.now()
    sorting_time_selection = int((end_time - start_time).total_seconds() * 1000)
    print(sorted_numbers_selection)
    print(f"Time to sort using the selection method: {sorting_time_selection} milliseconds")

if __name__ == "__main__":
    main()













# import random

# class RandomList:
#     def __init__(self, unsorted_list):
#         self.unsorted = unsorted_list
#         self.rand_numbers = []
        
#     def random_numbers(self):
#         for x in self.unsorted:
#             self.rand_numbers.append(random.randint(0, 10))
#         print(self.rand_numbers)
#         return self.rand_numbers
    
#     def bubble_sort(self):
#         pass
    

# def main():

#     # Create an instance of the RandomList class with an unsorted list of integers from 1 to 100000
#     my_list = RandomList(list(range(1, 100_000)))

#     # Call the random_numbers method to generate a list of random numbers
#     my_list.random_numbers()


# if __name__ == "__main__":
#     main()