class Set:
    def __init__(self):
        self.data = dict()

    def add(self, x):
        self.data[x] = x

    def remove(self, x):
        if (x in self.data.keys()):
            del self.data[x]
        else:
            raise SetError(f"The element {x} does not exist in set")

    def contains(self, x):
        return True if (x in self.data.keys()) else False
    
    def is_empty(self):
        return True if (len(self.data) == 0) else False
    
    def size(self):
        return len(self.data)

    def union(self, new_set):
        temp = Set()
        for i in self.data:
            temp.add(i)

        for j in new_set.data.keys():
            temp.add(j)

        return temp

    def intersection(self, new_set):
        temp = Set()
        for i in self.data:
            for j in new_set.data.keys():
                if (i == j):
                    temp.add(i)

        return temp

    def difference(self, new_set):
        temp = Set()
        for i in self.data:
            if (i not in new_set.data.keys()):
                temp.add(i)

        return temp

    def printAll(self):
        print("{",end = "")
        count = 0
    
        for i in self.data.keys():
            print(f" {i}", end = ",") if count != len(self.data)-1 else print(f" {i}", end=" ")
            count +=1
        print("}")

class SetError(BaseException):
    err = ""
    def __init__ (self, x):
        self.err = x

    def getErr(self):
        return self.err
