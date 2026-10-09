import ctypes


class MyList:

    def __init__(self):
        self.size = 1
        self.n = 0
        # create a c type array with size = self.size
        self.A = self.__make_array(self.size)

    def __len__(self):
        return self.n

    def __str__(self):
        result = ""
        for i in range(self.n):
            result += str(self.A[i]) + ", "
        return "[" + result[:-2] + "]"

    def append(self, item):
        if self.n == self.size:
            self.__resize(2 * self.size)
        self.A[self.n] = item
        self.n += 1

    def __resize(self, new_capacity):
        B = self.__make_array(new_capacity)
        for i in range(self.n):
            B[i] = self.A[i]
        self.A = B
        self.size = new_capacity

    def __make_array(self, capacity):
        return (capacity * ctypes.py_object)()


l = MyList()
l.append("Hello")
l.append(True)
l.append(3.14)
print(len(l))
print(l)
