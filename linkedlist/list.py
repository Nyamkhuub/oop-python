class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class List:
    def __init__(self, *elements):
        self.header = None
        for element in elements:
            self.add(element)
    def add(self, value):
        if self.header == None:
            self.header = Node(value)
        else:
            curr = self.header
            while curr.next != None:
                curr = curr.next
            curr.next = Node(value)
    def see(self):
        curr = self.header
        while(curr != None):
            print(curr.value)
            curr = curr.next
    def remove(self, value):
        curr = self.header
        prev = self.header
        hasElement = False
        while curr != None:
            if curr.value == value:
                if curr == self.header:
                    self.header = self.header.next
                    hasElement = True
                    break
                prev.next = curr.next
                hasElement = True
                break
            prev = curr
            curr = curr.next
        if hasElement:
            print('Amjilttai ustgalaa!')
        else:
            print('tuhain haij baigaa utga listend baihgui bna')

test = List(1, 2, 3, 4, 'ene bol test')
test.see()
test.add('testing add function')
print('-----------')
test.remove(1)
print('-----------')
test.see()
