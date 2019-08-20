from queues import Queue


class TestClassQueue:

    def test_enqueue(self):
        q = Queue()
        q.enqueue('Python')
        assert list(q.items) == ['Python']
        # Add another item
        q.enqueue('Java')
        assert list(q.items) == ['Python', 'Java']

    def test_dequeue(self):
        q = Queue()
        q.dequeue()
        q.enqueue('Python')
        q.enqueue('Java')
        result = q.dequeue()
        assert result == 'Python'
        assert list(q.items) == ['Java']

    def test_size(self):
        q = Queue()
        assert q.size() == 0
        q.enqueue('Python')
        q.enqueue('Java')
        assert q.size() == 2

    def test_isEmpty(self):
        q = Queue()
        assert q.isEmpty() == True
        q.enqueue('Python')
        assert q.isEmpty() == False
