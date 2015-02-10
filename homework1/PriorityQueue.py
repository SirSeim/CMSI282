import math

class PriorityQueue:
    def __init__ (self):
        self.array = []

    def add (self, value):
        if len(self) < 2:
            self.array[0] = None
            self.array[1] = value
        else:
            self.array.append(value)
        counter = len(self.array) - 1
        while counter > 1:
            half_counter = math.floor(counter / 2)
            if self.array[counter] > self.array[half_counter]:
                replacement = self.array[half_counter]
                self.array[half_counter] = self.array[counter]
                self.array[counter] = replacement
            counter = half_counter

    def peek (self):
        if len(self) < 2:
            return None
        else:
            return self.array[1]

    def remove (self):
        result = self.peek()
        if result is not None:
            self.array[1] = self.array.pop(len(self.array) - 1)
            counter = 1
            while counter * 2 <= len(self.array):
                first_child = counter * 2
                second_child = counter * 2 + 1
                if second_child 
                if self.array[first_child] > self.array[second_child]:
                    
        return result

    def __len__ (self):
        return len(self.array)

    def __str__ (self):
        return "This is a PriorityQueue"


