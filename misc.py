from basic_data_structures import *

class MyDS1:
    def __init__(self, n):
        self.arr = np.empty(n)
        self.times = np.empty(n)
        self.time = 0
        self.val = 0

    def set(self, i, val):
        self.arr[i] = val
        self.times[i] = self.time

    def get(self, i):
        if self.times[i] < self.time:
            return self.val
        else:
            return self.arr[i]

    def set_all(self, val):
        self.val = val
        self.time += 1


class MyDS2:
    def __init__(self, n):
        self.arr = np.empty(n)
        self.max1 = 0
        self.max2 = 0
        self.size = 0

    def insert(self):
        self.arr[self.size] = self.max1
        self.size += 1

    def increase(self, i):
        if self.arr[i] < self.max1:
            self.arr[i] = self.max1

        self.arr[i] += 1
        if self.max2 < self.arr[i]:
            self.max2 = self.arr[i]

    def get(self, i):
        if self.arr[i] < self.max1:
            return 0
        else:
            return self.arr[i] - self.max1

    def reset(self):
        self.max1 = self.max2
