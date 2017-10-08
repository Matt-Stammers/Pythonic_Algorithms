# This is the basic node datastructure used to build a linkedlist

class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext
        
node1 = Node(1)
print(node1.getData()) # will print 1 as 1 is in the Node.
node1 = Node(2)
print(node1.getData()) # This now prints 2 as now 2 is in the Node. it has displaced 1.

# Here is our linkedlist:

class UnorderedList:

    def __init__(self):
        self.head = None
        
    def isEmpty(self): # if the head of the list is empty will return None
        return self.head == None
        
    def add(self,item): # this adds an item to the list in the next position
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp
        
    def size(self): # this gives the size of the unordered linked list
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()

        return count
        
    def search(self,item): # this will search for the node and return true if it exists
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found
        
    def remove(self,item): # up until now we have only been able to traverse one way. This time we add the previous function that can inch-worm backwards
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

            if previous == None:
                self.head = current.getNext()
            else:
                previous.setNext(current.getNext())
        
mylist = UnorderedList()
mylist.add(1)
mylist.add(2)
mylist.add(3)
mylist.add(4)
mylist.add(5)
mylist.add(10)
print(mylist.search(3)) # Will return True as 3 is now contained in a node in the linked list. This is detected during the traversal of the list
print(mylist.size()) # the list is now 6 long
print(mylist.search(10)) # 10 is in there. Yay!
mylist.remove(10) # bye bye 10
print(mylist.size()) # dropped to 5
print(mylist.search(10)) # now 10 is not in there

