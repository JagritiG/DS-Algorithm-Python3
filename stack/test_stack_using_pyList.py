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
