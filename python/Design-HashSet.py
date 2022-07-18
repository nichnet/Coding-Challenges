#Design a HashSet without using any built-in hash table libraries.

#Implement MyHashSet class:
# -  void add(key) Inserts the value key into the HashSet.
# -  bool contains(key) Returns whether the value key exists in the HashSet or not.
# -  void remove(key) Removes the value key in the HashSet. If key does not exist in the HashSet, do nothing.

class MyHashSet(object):
    
    def __init__(self):
        self.values = []

    def add(self, key):
        self.values.append(key)

    def remove(self, key):
        while self.contains(key):
            self.values.remove(key)

    def contains(self, key):
        return key in self.values
