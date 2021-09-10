from linked_list.linked_list import LinkedList


class HashTable:

    def __init__(self, size=1024):
        self.size = size
        self.bucket = [None] * self.size

    def hash(self, key):

        """
        Argument: Key
        Return: Index for key
        """

        hash_index = 0
        for char in key:
            hash_index += ord(char)

        hash_index *= 657
        hash_index %= self.size
        return hash_index

    def add(self, key, value):

        """
        Argument: key, value
        Returns: Nothing
        """

        hash_index = self.hash(key)

        if not self.bucket[hash_index]:
            self.bucket[hash_index] = LinkedList()

        bucket = self.bucket[hash_index]
        bucket.insert([key, value])

    def get(self, key):

        """
        Argument: Key
        Return: value associated with key
        """
        hash_index = self.hash(key)

        if self.bucket[hash_index] is None:
            return None

        current = self.bucket[hash_index].head

        while current:
            if current.value[0] == key:
                return current.value[1]
            current = current.next

        return None

    def contains(self, key):

        """
        Argument: Key
        Return: boolean
        """

        hash_index = self.hash(key)

        if self.bucket[hash_index] is None:
            return False

        current = self.bucket[hash_index].head

        while current:
            if current.value[0] == key:
                return True
            current = current.next

        return False
