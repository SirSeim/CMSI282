class PriorityQueue:
    def __init__ (self):
        self.array = []

    def add (self, value):
        if len(self.array) < 2:
            self.array.append(None)
            self.array.append(value)
        else:
            self.array.append(value)
        counter = len(self.array) - 1
        while counter > 1:
            half_counter = counter / 2
            if self.array[counter] > self.array[half_counter]:
                self.switch(counter, half_counter)
            counter = half_counter

    def peek (self):
        if len(self.array) < 2:
            return None
        else:
            return self.array[1]

    def remove (self):
        result = self.peek()
        if result is not None:
            self.switch(1, len(self.array) - 1)
            self.array.pop(len(self.array) - 1)

            counter = 1
            while counter * 2 <= len(self.array) - 1:
                child = counter * 2
                if child < len(self.array) - 1 and self.array[child] < self.array[child + 1]:
                    child += 1
                if not self.array[counter] < self.array[child]:
                    break
                self.switch(counter, child)
                counter = child
                    
        return result

    def switch (self, first, second):
        replacement = self.array[first]
        self.array[first] = self.array[second]
        self.array[second] = replacement

    def __len__ (self):
        return len(self.array) - 1

    def __str__ (self):
        print_queue = PriorityQueue()
        for value in self.array[1:]:
            print_queue.add(value)

        end = len(print_queue)
        result = "["
        for index in range(0, end):
            result += "\'"
            result += str(print_queue.remove())
            result += "\'"
            if index < end - 1 :
                result += ", "
        result += "]"
        return result