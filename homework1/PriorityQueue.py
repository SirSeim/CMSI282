import math

class PriorityQueue:
    def __init__ (self):
        self.array = []
        self.size = 0

    def add (self, value):
        self.array.append(value)
        counter = len(self.array) - 1
        while counter > 1:
            half_counter = math.floor(counter / 2)
            if self.array[counter] > self.array[half_counter]:
                replacement = self.array[half_counter]
                self.array[half_counter] = self.array[counter]
                self.array[counter] = replacement
            counter = half_counter
        self.size += 1

    def peek (self):
        if self.size < 1:
            return None
        else:
            result = self.array[0]
            self.array[0] = self.array.pop(len(self.array) - 1)
            counter = 0
            while counter < len(self.array):
                # Finish Siftdown
            return result

    def remove (self):
        result = self.peek()
        if result is not None:
            self.size -= 1
        return result

    def __len__ (self):
        return self.size

    def __str__ (self):
        return "This is a PriorityQueue"

