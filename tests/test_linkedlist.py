from implemetation_ds.linkedlist import LinkedList, Node, create_linked_list

def test_to_list():
    output = [2, 3, 4, 5]
    ll = LinkedList()
    ll.push_back(2)
    ll.push_back(3)
    ll.push_back(4)
    ll.push_back(5)

    assert output == ll.to_list()