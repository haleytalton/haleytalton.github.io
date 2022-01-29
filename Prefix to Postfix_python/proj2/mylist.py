# node class
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)


class MyList:

    def __init__(self):
        self.head = None

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __len__(self):
        curr = self.head
        size = 0
        while curr is not None:
            size += 1
            curr = curr.next
        return size

    def __getitem__(self, index):
        if len(self) <= index:
            raise IndexError
        curr = self.head
        for i in range(index):
            curr = curr.next
        return curr.data

    def append(self, node):
        new_node = Node(node)
        if self.head is None:
            self.head = new_node
            return
        n = self.head
        while n.next is not None:
            n = n.next
        n.next = new_node

    def remove_head(self):
        if self.head is None:
            return None
        temp = self.head
        self.head = self.head.next
        return temp

    def __repr__(self):
        nodes = []
        for node in self:
            nodes.append(node.data)
        return "".join(nodes)

    def string_to_list(self, string):
        if len(string) == 0:
            return
        for i in range(len(string)):
            value = string[i]
            self.append(value)

    def remove_node(self, value):
        prev = None
        curr = self.head
        while curr:
            if curr.data == value:
                if prev:
                    prev.next = curr.next
                else:
                    self.head = curr.next
                return True
            prev = curr
            curr = curr.next
        return False

