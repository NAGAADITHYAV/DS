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
        print(f"List has a total of {n} nodes")
        return n

    def search(self, value):
        pass

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
        pass

    def delete_last_node(self):
        pass

    def reverse_list(self):
        pass

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
ll.count_nodes()
# ll.display_list()