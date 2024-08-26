class  Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def InsertAtBegin(self, data, head):
        new_node = Node(data)
        if head is None:
            head = new_node
        else:
            new_node.next = head
            head = new_node
        return head

    def InsertAtEnd(self, data, head):
        if head is None:
            head = Node(data)
        else:
            new_node = Node(data)
            temp_node = head
            while temp_node.next is not None:
                temp_node = temp_node.next
            temp_node.next = new_node
        return head

    def InsertAtIndex(self, data, index, head):
        if index == 0:
            return self.InsertAtEnd(data, head)
        else:
            new_node = Node(data)
            temp_node = head
            position = 0
            while temp_node != None and position != index-1:
                position+=1
                temp_node = temp_node.next
            new_node.next = temp_node.next
            temp_node.next = new_node
        return head

    def printLinkedList(self, head):
        while head is not None:
            print(head.data, end=" ")




if __name__ == '__main__':
    #Create a linklist

    print("Menu operations : ")
    print("1. Insert at beginning of linked list")
    print("2. Insert at end of linked list")
    print("3. Insert at index of beginning of linked list")
    print("4. Insert at index of end of linked list")
    print("5. Print Linked List")


    user_input = int(input("Enter a number: "))
    ll = LinkedList()
    head = None
    if user_input == 1:
        print("Insert at beginning of linked list")
        data = int(input("Enter data: "))
        ll.InsertAtBegin(data, head)
        ll.printLinkedList(head)
    elif user_input == 2:
        print("Insert at end of linked list")
        data = int(input("Enter data: "))
        ll.InsertAtEnd()
    elif user_input == 3:
        print("Insert at index of beginning of linked list")
        data = int(input("Enter data: "))
        ll.InsertAtIndex(data, 0, ll)
    elif user_input == 4:
        ll.printLinkedList()


    #Linked List operations
    #insert at begning
    #insert at end
    #insert in between