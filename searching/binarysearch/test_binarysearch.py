from binarysearch import binarySearch


def test_binarysearch():
    mylist = [5, 10, 12, 17, 23, 34, 36, 40, 45, 67]
    assert binarySearch(mylist, 50) == False
    assert binarySearch(mylist, 36) == True
