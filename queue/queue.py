class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
class queue:
    def __init__(self):
        self.header = None
        self.tail = None
    def isNone(self):
        return self.header == None
    def push(self, value):
        if self.isNone():
            self.header = Node(value)
            self.tail = self.header
        else:
            curr = Node(value)
            self.tail.next = curr
            self.tail = curr
    def front(self):
        return self.header.value
    def pop(self):
        self.header = self.header.next

test = queue()
test.push(1)
test.push('a')
test.push(2)
test.push(23)

print(test.front())
test.pop()
print('---------')
while test.isNone() == False:
    print(test.front())
    test.pop()
print(test.isNone())
