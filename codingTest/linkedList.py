class ListNode:
    def __init__(self, val=0 , next= None ):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, val):
        if not self.head:
            self.head = ListNode(val, None)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = ListNode(val, None)

    def insert(self, val, pos):
        new_node = ListNode(val)
        if pos == 0:
            new_node.next = self.head
            self.head = new_node
            return

        current = self.head
        current_pos = 0
        while current.next and current_pos < pos - 1:
            current = current.next
            current_pos += 1

        new_node.next = current.next
        current.next = new_node

    def delete(self, val):
        if not self.head:
            return

        if self.head.val == val:
            self.head = self.head.next
            return

        current = self.head
        while current.next:
            if current.next.val == val:
                current.next = current.next.next
                return
            current = current.next

    def view(self):
        node = self.head
        while node:
            print(node.val, end=" -> ")
            node = node.next
        print("None")


lst = [1,2,3] #이걸 링크드 리스트 로만들어봄

l1 = LinkedList()

for n in lst:
    l1.append(n)



print("Initial List:")
l1.view()

# Insert a new value
l1.insert(4, 1) # Insert 4 at position 1
print("After Insertion:")
l1.view()

# Delete a value
l1.delete(2) # Delete the node with value 2
print("After Deletion:")
l1.view()
