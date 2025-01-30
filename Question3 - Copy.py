#create the node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

#Create the linked lists
class LinkedList:
    def __init__(self):
        self.head = None  

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete_by_value(self, value): # Function for deleting
        temp = self.head
        if temp and temp.data == value:
            self.head = temp.next
            return
        prev = None
        while temp and temp.data != value:
            prev = temp
            temp = temp.next
        if temp:
            prev.next = temp.next

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

linkedlist = LinkedList()
linkedlist.append(10)
linkedlist.append(20)
linkedlist.insert_at_beginning(5)
linkedlist.delete_by_value(10)
linkedlist.display()
