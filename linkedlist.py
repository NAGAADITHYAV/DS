class Node:
    def __init__(self, value = 0, next = None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self, head = None):
        self.head = head
        print('Created a LinkedList')
    
    def display_list(self):
        parser = self.head
        while(parser):
            print(parser.value, end='')
            parser = parser.next
            if not parser:
                print('')
                break
            print('->', end='')
        
    def count_nodes(self):
        n = 0
        parser = self.head
        while parser:
            parser = parser.next
            n += 1
        # print(f"List has a total of {n} nodes")
        return n

    def search(self, value):
        parser = self.head
        while(parser):
            if parser.value == value:
                return True
            parser = parser.next
        return False

    def insert_in_beginning(self, data):
        node = Node(data)
        if not self.head:
            self.head = node
        else:
            node.next = self.head
            self.head = node
        print(f"Inserted {data} at the start")
        self.display_list()

    def insert_at_end(self, data):
        node = Node(data)
        parser = self.head
        if not parser:
            self.head = node
        while(parser):
            if not parser.next:
                parser.next = node
                break
            parser = parser.next
        print('Inserted at the end', data)
        self.display_list()

    def create_list(self):
        pass

    def insert_after(self, data, value):
        pass

    def insert_before(self, data, value):
        pass

    def insert_at_position(self, data, position):
        pass

    def delete_node(self, value):
        pass

    def delete_first_node(self):
        if self.head:
            self.head = self.head.next
        # self.display_list()

    def delete_last_node(self):
        if not self.head:
            return
        if self.head and not self.head.next:
            self.head = None
        parser = self.head
        while(parser):
            if parser.next and not parser.next.next:
                parser.next = parser.next.next
                break
            parser = parser.next
        # self.display_list()

    def reverse_list(self):
        if not self.head or not self.head.next:
            return
        
        parser = self.head
        prev = None
        while(parser):
            next_node = parser.next
            parser.next = prev
            prev = parser
            parser = next_node
        self.head = prev

    def bubble_sort_byExdata(self):
        pass

    def bubble_sort_byExlinks(self):
        pass

    def has_cylce(self):
        pass

    def merge_list(self, newlst):
        pass

ll = LinkedList(Node(1))
ll.insert_at_end(2)
ll.count_nodes()
ll.insert_in_beginning(0)
ll.insert_in_beginning(-1)
ll.insert_at_end(3)
ll.count_nodes()
ll.delete_first_node()
ll.delete_last_node()
print(ll.search(2))
print(ll.search(4))
ll.reverse_list()
ll.display_list()
ll.reverse_list()
ll.display_list()
# ll.display_list()