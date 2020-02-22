from ds.slinkedl import LinkedList


def test_insert_at_begin():
    list = LinkedList()
    list.insert_at_begin(1)
    assert list.head.value == 1


def test_reverse():
    list = LinkedList()
    list.insert_at_begin(1)
    list.insert_at_end(2)
    list.reverse()
    assert list.head.value == 2
