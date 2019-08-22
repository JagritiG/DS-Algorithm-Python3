from linearsearch import linearSearch


def test_linearsearch():
    mylist = [12, 34, 67, 45, 23, 36, 5, 17, 40, 10]
    assert linearSearch(mylist, 50) == False
    assert linearSearch(mylist, 36) == True
