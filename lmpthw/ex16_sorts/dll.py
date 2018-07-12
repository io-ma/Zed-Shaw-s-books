class DoubleLinkedListNode(object):

    def __init__(self, value, nxt, prev):
        self.value = value
        self.next = nxt
        self.prev = prev

    def __repr__(self):
        nval = self.next and self.next.value or None
        pval = self.prev and self.prev.value or None
        return f"[{self.value}, {repr(nval)}, {repr(pval)}]"

class DoubleLinkedList(object):

    def __init__(self):
        self.begin = None
        self.end = None

    def _invariant(self):
        # if 0 elements, self.begin = self.end = None
        if self.begin == None:
            assert self.end == None
        # if there is 1 element, self.begin = self.end(point at same node)
        if self.begin:
            # the first element's prev must be None
            assert self.begin.prev == None
        # the last element's next must be None
            assert self.end.next == None

    def push(self, obj):
        """Appends a new value on the end of the list."""
        if self.end:
            new_node = DoubleLinkedListNode(obj, None, self.end)
            self.end.next = new_node
            self.end = new_node
        else:
            new_node = DoubleLinkedListNode(obj, None, None)
            self.begin = new_node
            self.end = self.begin


    def pop(self):
        """Removes the last item and returns it."""
        if self.end:
            node = self.end
            if self.end == self.begin:
                self.end = None
                self.begin = None
            else:
                self.end = node.prev
                self.end.next = None
                if self.end == self.begin:
                    self.begin.next = None
            return node.value
        else:
            return None


    def shift(self, obj):
        """Actually just another name for push."""
        '''if self.begin:
            new_node = DoubleLinkedListNode(obj, self.begin, None)
            self.begin.prev = new_node
            self.begin = new_node
        else:
            new_node = DoubleLinkedListNode(obj, None, None)
            self.end = new_node
            self.begin = self.end'''
        self.push(obj)


    def unshift(self):
        """Removes the first item(from begin) and returns it."""
        if self.begin:
            node = self.begin
            if self.begin == self.end:
                self.begin = None
                self.end = None
            else:
                self.begin = node.next
                self.begin.prev = None
            return node.value
        else:
            return None


    def detach_node(self, node):
        """Detaches node from list"""
        if self.end == node:
            self.pop()
        elif self.begin == node:
            self.unshift()
        else:
            nxt = node.next
            prev = node.prev
            prev.next = nxt
            next.prev = prev

    def remove(self, obj):
        """Finds a matching item and removes it from the list."""
        node = self.begin
        count = 0
        while node:
            if node.value == obj:
                self.detach_node(node)
                return count
            else:
                count += 1
                node = node.next
        return -1

    def first(self):
        """Returns a reference to the first item, does not remove."""
        return self.begin and self.begin.value or None

    def last(self):
        """Returns a reference to the last item, does not remove."""
        return self.end and self.end.value or None

    def count(self):
        """Counts the number of elements in the list."""
        new_node = self.begin
        count = 0
        while new_node:
            new_node = new_node.next
            count += 1
        return count


    def get(self, index):
        """Get the value at index."""
        node = self.begin
        i = 0
        while node:
            if i == index:
                return node.value
            else:
                i += 1
                node = node.next
        return None


    def dump(self, mark):
        """Debugging function that dumps the contents of the list."""
        node = self.begin
        print(">>>> ", end="")
        while node:
            print(node, end="")
            node = node.next
        print()

colors = DoubleLinkedList()
colors.push("Red")
print(f"Colours count: {colors.count()}")
