from stack.stacks import Stack


class TestClassStack:

    def test_push(self):
        stack = Stack()
        stack.push('Python')
        assert stack.items == ['Python']
        # Add another item
        stack.push('Java')
        assert stack.items == ['Python', 'Java']

    def test_pop(self):
        stack = Stack()
        stack.pop()
        stack.push('Python')
        stack.push('Java')
        result = stack.pop()
        assert result == 'Java'
        assert stack.items == ['Python']

    def test_peek(self):
        stack = Stack()
        stack.push('Python')
        assert stack.peek() == 'Python'
        stack.pop()
        assert stack.items == []

    def test_size(self):
        stack = Stack()
        assert stack.size() == 0
        stack.push('Python')
        stack.push('Java')
        assert stack.size() == 2

    def test_isEmpty(self):
        stack = Stack()
        assert stack.isEmpty() == True
        stack.push('Python')
        assert stack.isEmpty() == False




