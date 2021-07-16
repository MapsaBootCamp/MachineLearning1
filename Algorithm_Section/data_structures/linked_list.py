from typing import Optional


class LinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next: Optional[LinkedListNode] = None
        self._has_refrence = False

    @property
    def has_refrence(self):
        return self._has_refrence

    def node_free(self):
        self._has_refrence = False

    def node_busy(self):
        self._has_refrence = True

    def __str__(self):
        return str(self.data)


class LinkedList:
    def __init__(self):
        self.head: Optional[LinkedListNode] = None

    def add_begin(self, node: LinkedListNode):
        assert node.has_refrence == False, "say kon tak par bashi! inja sarzamin monogamus hast."

        if not self.head:
            self.head = node
        else:
            node.next = self.head
            self.head = node
        node.node_busy()

    # def __next__(self):
    #     pass

    def __iter__(self):
        temp = self.head
        while temp:
            yield temp
            temp = temp.next

    def append(self, node: LinkedListNode):
        assert node.has_refrence == False, "say kon tak par bashi! inja sarzamin monogamus hast."

        if not self.head:
            self.head = node
        else:
            temp = self.head
            # while temp:
            #     if not temp.next:
            #         temp.next = node
            #         break
            #     temp = temp.next
            while temp.next:
                temp = temp.next
            temp.next = node
        node.node_busy()

    def pop(self, index=-1):
        pass

    def insert(self, node: LinkedListNode, index: int):
        assert node.has_refrence == False, "say kon tak par bashi! inja sarzamin monogamus hast."

        if not self.head:
            self.head = node

        if index == 0:
            self.add_begin(node)
        elif index > len(self)-1:
            self.append(node)
        elif index < 0:
            index += len(self)
            if index < 0:
                raise IndexError("index out of range")
            self.insert(node, index)
        else:
            count = 0
            temp = self.head
            while temp.next:
                if count == index - 1:
                    node.next = temp.next
                    temp.next = node
                    break
                temp = temp.next
                count += 1
        node.node_busy()

    def remove(self, node: LinkedListNode):
        pass

    def flush(self):
        pass

    def __len__(self):
        if not self.head:
            return 0
        else:
            count = 1
            temp = self.head
            while temp.next:
                count += 1
                temp = temp.next
            return count

    def __str__(self):
        if not self.head:
            return "(]"
        else:
            result = "("
            temp = self.head
            while temp:
                result = result + str(temp.data) + (", " if temp.next else "]")
                temp = temp.next
            return result


linkedlist1 = LinkedList()
node1 = LinkedListNode("ashkan")
node2 = LinkedListNode("asghar")
node3 = LinkedListNode(True)
node4 = LinkedListNode(25)

linkedlist1.add_begin(node1)
linkedlist1.add_begin(node2)
linkedlist1.append(node4)
linkedlist1.insert(node3, 2)

print(linkedlist1)
print(len(linkedlist1))


# a = list(linkedlist1)
# print(a[0])
