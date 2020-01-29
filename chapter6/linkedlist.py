class ListNode:
    def __init__(self, data, link=None):
        self.data = data
        self.link = link

class LinkedList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._length = 0

    def addfirst(self, item):
        self._length += 1
        self._head = ListNode(item, self._head)
        if self._tail is None:
            self._tail = self._head

    def addlast(self, item):
        if self._head is None:
            self.addfirst(item)
        else:
            self._tail.link = ListNode(item)
            self._tail = self._tail.link
            self._length += 1

    def removefirst(self):
        self._length -= 1
        item = self._head.data
        self._head = self._head.link
        if self._head is None:
            self._tail = None
        return item

    def removelast(self):
        if self._head is self._tail:
            return self.removefirst()

        cur_node = self._head
        while cur_node is not self._tail:
            cur_node = cur_node.link

        item = self._tail.data
        self._tail = cur_node
        self._tail.link = None
        self._length -= 1
        return item

    def __len__(self):
        return self._length
