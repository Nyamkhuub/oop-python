class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class List:
    def __init__(self):
        self.header = None
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

test = List()
test.add(1)
test.add(2)
test.add(3)
test.add('ene bol text')
test.add('hamgiin engiin baidlaar listiig heregjuullee!')
test.see()
