class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

def union(llist_1, llist_2):
    elems_1 = collect_elems(llist_1)
    elems_2 = collect_elems(llist_2)
    u = elems_1.union(elems_2)
    return generate_llist(u)

def intersection(llist_1, llist_2):
    elems_1 = collect_elems(llist_1)
    elems_2 = collect_elems(llist_2)
    i = elems_1.intersection(elems_2)
    return generate_llist(i)

def collect_elems(llist):
    elems = set()
    pointer = llist.head
    while pointer:
        elems.add(pointer.value)
        pointer = pointer.next
    return elems

def generate_llist(elem_set):
    llist = LinkedList()
    for elem in elem_set:
        llist.append(elem)
    return llist

def main():
    tc_1()
    tc_2()
    tc_3()
    tc_4()

# two empty linked lists
def tc_1():
    linked_list_1 = LinkedList()
    linked_list_2 = LinkedList()
    print (union(linked_list_1,linked_list_2))
    print (intersection(linked_list_1,linked_list_2))
    # prints two empty strings

# one empty linked list
def tc_2():
    linked_list_1 = LinkedList()
    linked_list_2 = LinkedList()
    element_1 = [3,2,4,35,6,65,6,4,3,21]
    for i in element_1:
        linked_list_1.append(i)
    print (union(linked_list_1,linked_list_2))
    # prints only the elements from the first list
    # As union is by definition a set operation, duplicates from linked_list_1
    # are removed.
    print (intersection(linked_list_1,linked_list_2))
    # prints empty string

# test case 1 given from assignment
def tc_3():
    linked_list_1 = LinkedList()
    linked_list_2 = LinkedList()
    element_1 = [3,2,4,35,6,65,6,4,3,21]
    element_2 = [6,32,4,9,6,1,11,21,1]
    for i in element_1:
        linked_list_1.append(i)
    for i in element_2:
        linked_list_2.append(i)
    print (union(linked_list_1,linked_list_2))
    print (intersection(linked_list_1,linked_list_2))

# test case 2 given from assignment
def tc_4():
    linked_list_3 = LinkedList()
    linked_list_4 = LinkedList()
    element_1 = [3,2,4,35,6,65,6,4,3,23]
    element_2 = [1,7,8,9,11,21,1]
    for i in element_1:
        linked_list_3.append(i)
    for i in element_2:
        linked_list_4.append(i)
    print (union(linked_list_3,linked_list_4))
    print (intersection(linked_list_3,linked_list_4))

if __name__ == "__main__":
    main()
