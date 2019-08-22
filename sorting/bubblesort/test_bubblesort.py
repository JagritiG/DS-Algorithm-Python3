from bubblesort import bubbleSort


def test_bubbleSort():
    mylist = [12, 34, 67, 45, 23, 36, 5, 17, 40, 10]
    sorted_list = bubbleSort(mylist)
    assert sorted_list == [5, 10, 12, 17, 23, 34, 36, 40, 45, 67]


