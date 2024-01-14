from foo_module.bbsort import sorter

def test_sorter():
    arr = [5, 4, 3, 2, 1]
    assert sorter(arr) == [1, 2, 3, 4, 5]


