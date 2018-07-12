class QueueNode(object):

    def __init__(self, value, nxt, prev):
        self.value = value
        self.next = nxt
        self.prev = prev

    def __repr__(self):
        nval = self.next and self.next.value or None

class Queue(object):

    def __init__(self):
        self.head = None
        self.tail = None


    def shift(self, obj):
        if self.tail:
            node = QueueNode(obj, None, self.tail)
            self.tail.next = node
            self.tail = node

        else:
            self.head = QueueNode(obj, None, None)
            self.tail = self.head

    def unshift(self):
        if self.tail:
            node = self.head
            if self.head == self.tail:
                self.head = None
                self.tail = None

            else:
                self.head = node.next
                self.head.prev = None
            return node.value

        else:
            return None


    def count(self):
        new_node = self.head
        count = 0
        while new_node:
            new_node = new_node.next
            count += 1
        return count

    def first(self):
        return self.head and self.head.value or None

    def last(self):
        return self.tail and self.tail.value or None














