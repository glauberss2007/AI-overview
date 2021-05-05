import numpy as np


class OrderedVector:

    def __init__(self, capacity):
        self.capacity = capacity
        self.last_position = -1
        self.values = np.empty(self.capacity, dtype=int)

    # O(n)
    def vector_print(self):
        if self.last_position == -1:
            print('The vector is empty')
        else:
            for i in range(self.last_position + 1):
                print(i, ' - ', self.values[i])

    # O(n)
    def insert(self, valor):
        if self.last_position == self.capacity - 1:
            print('Maximum capacity reached')
            return

        position = 0
        for i in range(self.last_position + 1):
            position = i
            if self.values[i] > valor:
                break
            if i == self.last_position:
                position = i + 1

        x = self.last_position
        while x >= position:
            self.values[x + 1] = self.values[x]
            x -= 1

        self.values[position] = valor
        self.last_position += 1

    # O(n)
    def linear_search(self, valor):
        for i in range(self.last_position + 1):
            if self.values[i] > valor:
                return -1
            if self.values[i] == valor:
                return i
            if i == self.last_position:
                return -1

    # O(log n)
    def binary_search(self, valor):
        lower_bound = 0
        upper_bound = self.last_position

        while True:
            current_position = int((lower_bound + upper_bound) / 2)

            if self.values[current_position] == valor:
                return current_position

            elif lower_bound > upper_bound:
                return -1

            else:

                if self.values[current_position] < valor:
                    lower_bound = current_position + 1

                else:
                    upper_bound = current_position - 1

    # O(n)
    def remove(self, value):
        position = self.linear_search(value)
        if position == -1:
            return -1
        else:
            for i in range(position, self.last_position):
                self.values[i] = self.values[i + 1]

            self.last_position -= 1