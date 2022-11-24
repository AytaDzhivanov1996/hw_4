from hw_2.index_of import index_of

def test_index_of():
    assert index_of([2, 7, 3, 2, 4], 2) == 0
    assert index_of([1, 2, 3, 2, 5], 7) == -1
    assert index_of([1, 2, 3, 2, 5], 2, -3) == 3
