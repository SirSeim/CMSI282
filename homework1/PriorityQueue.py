class PriorityQueue:
    def __init__ (self):
        self.array = []
        self.size = 0

    def add (self, value):
        # Add to Heap
        # Correct Heap
        self.size += 1

    def peek (self):
        if self.size < 1:
            return None
        else:
            result = self.array[0]
            # Correct Heap
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

