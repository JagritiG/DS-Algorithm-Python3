from hashtable import HashTable


class TestClassSll:

        def test_put(self):
                h = HashTable()
                h.put("key1", "Python")
                h.put("key2", "Pandas")
                assert h.map == {'key1': 'Python', 'key2': 'Pandas'}

        def test_get(self):
                h = HashTable()
                h.put("key1", "Python")
                h.put("key2", "Pandas")
                assert h.get("key1") == 'Python'
                assert h.get("key6") == None

        def test_search(self):
                h = HashTable()
                h.put("key1", "Python")
                h.put("key2", "Pandas")
                assert h.search("key1") == True
                assert h.search("key6") == False

        def test_replace(self):
                h = HashTable()
                h.put("key1", "Python")
                h.put("key2", "Pandas")
                assert h.map == {'key1': 'Python', 'key2': 'Pandas'}
                h.replace("key2", "Java")
                assert h.map == {'key1': 'Python', 'key2': 'Java'}

        def test_size(self):
                h = HashTable()
                size = h.size()
                # Test an empty hashtable
                assert size == 0
                # Test hashtable with entries
                h.put("key1", "Python")
                h.put("key2", "Pandas")
                size = h.size()
                assert size == 2

        def test_remove(self):
                h = HashTable()
                h.put("key1", "Python")
                h.put("key2", "Pandas")
                h.remove("key1")
                assert h.map == {'key2': 'Pandas'}
                assert str(h.remove("key5")) == 'No key-value pairs to remove.'


