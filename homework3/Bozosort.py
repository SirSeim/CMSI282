from random import randint
import time

def bozo_sort (inputs):
    array = list(inputs)
    def swap (array, index1, index2):
        array[index1], array[index2] = array[index2], array[index1]

    def sorted (array):
        for index in range(0, len(array) - 1):
            if (array[index] > array[index + 1]):
                return False
        return True

    while (not sorted(array)):
        int1 = randint(0, len(array) - 1)
        int2 = randint(0, len(array) - 1)
        swap(array, int1, int2)

    return array

wip = [10,9,8,7,6,5,4,3,2,1]
trials = []

while (len(trials) < 10):
    start = time.time()
    bozo_sort(wip)
    end = time.time()
    trials.append(end-start)
    print len(trials)

print sum(trials)/len(trials)