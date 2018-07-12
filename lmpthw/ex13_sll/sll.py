class SingleLinkedListNode(object):

    def __init__(self, value, nxt):
        self.value = value
        self.next = nxt

    def __repr__(self):
        nval = self.next and self.next.value or None
        return f"[{self.value}:{repr(nval)}]"

class SingleLinkedList(object):

    def __init__(self):
        self.begin = None
        self.end = None

    def push(self, obj):
        """Appends a new value on the end of the list."""
        new_node = SingleLinkedListNode(obj, None)
        print("new node:", new_node)
        if self.begin == None:
            self.begin = new_node
            self.end = self.begin
        else:
            self.end.next = new_node
            self.end = new_node
        print(self.begin, self.end)

    def pop(self):
        """Removes the last item and returns it."""
        if self.end == None:
            return None
        elif self.end == self.begin:
            new_node = self.begin
            self.end = self.begin = None
            return new_node.value
        else:
            new_node = self.begin
            while new_node.next != self.end:
                new_node = new_node.next
            #assert self.end != new_node
            self.end = new_node
            return new_node.next.value



    def shift(self, obj):
        """Another name for push."""
        new_node = SingleLinkedListNode(obj, None)
        print("new node:", new_node)
        if self.end == None:
            self.begin = new_node
            self.end = self.begin
        else:
            new_node.next = self.begin
            self.begin = new_node
        print(f"self.begin is:{self.begin} self.begin.next is: {self.begin.next}")


    def unshift(self):
        """Removes the first item and returns it."""
        if self.begin == None:
            return None
        elif self.begin == self.end:
            new_node = self.begin
            self.begin = self.end = None
            return new_node.value
        else:
            value = self.begin.value
            self.begin = self.begin.next
            return value


    def remove(self, obj):
        """Finds a matching item and removes it from the list."""
        temp = self.begin

        if temp is not None:
            if temp.value == obj:
                self.begin = temp.next
                temp = None
                return

        while temp is not None:
            if temp.value == obj:
                break
            prev = temp
            temp = temp.next

        if temp == None:
            return

        # Unlink the node from linked list
        prev.next = temp.next

        temp = None



    def first(self):
        """Returns a reference to the first item, does not remove."""
        return self.begin.value

    def last(self):
        """Returns a reference to the last item, does not remove."""
        return self.end.value

    def count(self):
        """Counts the number of elements in the list."""
        new_node = self.begin
        count = 0
        while new_node:
            count += 1
            new_node = new_node.next
        return count

    def get(self, index):
        """Get the value at index."""
        nr = self.count()
        count = 0
        if nr == 0:
            return None
        elif index > nr:
            return "Error"
        else:
            node = self.begin
            while node:
                if nr == index:
                    return node.value
                else:
                    node = node.next

                count += 1


    def shift(self, obj):
                    """Another name for push."""


    def dump(self, mark):
        """Debugging function that dumps the contents of the list."""
        pass

colors = SingleLinkedList()
'''colors.push("blue")
colors.push("yellow")
colors.push("red")
colors.push("pink")
colors.push("orange")
print(">>>>> start shifting <<<<<")
print("colors count:", colors.count())
colors.shift("blue")
print(f"shift colors begin: {colors.begin}, colors end: {colors.end}")
print("colors count:", colors.count())
colors.shift("yellow")
print(f"shift colors begin: {colors.begin}, colors 2: {colors.begin}, colors end: {colors.end}")
print("colors count:", colors.count())
colors.shift("pink")
print(f"shift colors begin: {colors.begin}, colors end: {colors.end}")
print("colors count:", colors.count())
print("colors pop:", colors.pop())
print(f"colors begin: {colors.begin}, colors 2: {colors.begin.next}, colors end: {colors.end}")
print("colors count:", colors.count())
print("colors pop:", colors.pop())
print(f"colors begin: {colors.begin}, colors 2: {colors.begin.next}, colors end: {colors.end}")
print("colors count:", colors.count())
print("colors pop:", colors.pop())
print(f"colors begin: {colors.begin}")
print("colors count:", colors.count())
'''

#colors.unshift()
#colors.unshift()
