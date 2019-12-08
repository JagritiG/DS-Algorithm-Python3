from stack.stack_using_pyList import PyListStack


class TestPyListStack:

    def test_is_empty(self):
        stack = PyListStack()
        assert stack.is_empty() is True
        stack.push("A")
        assert stack.is_empty() is False

    def test_top(self):
        stack = PyListStack()
        stack.push("A")
        assert stack.top() == "A"

    def test_pop(self):
        stack = PyListStack()
        stack.push("A")
        stack.push("B")
        assert stack._data == ['A', 'B']
        assert stack.__len__() == 2
        assert stack.pop() == "B"

    def test_pop_all(self):
        stack = PyListStack()
        stack.push("A")
        stack.push("B")
        stack.push("C")
        stack.push("D")
        assert stack._data == ["A", "B", "C", "D"]
        stack.pop_all()
        assert stack._data == []

    def test_min_item(self):
        stack = PyListStack()
        stack.push(4)
        stack.push(3)
        stack.push(6)
        stack.push(2)
        assert stack._data == [4, 3, 6, 2]
        result = stack.min_item()
        assert result == 2
        stack.push(1)
        assert stack._data == [1]
        result = stack.min_item()
        assert result == 1

