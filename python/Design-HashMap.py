#Design a HashMap without using any built-in hash table libraries.

#Implement the MyHashMap class:
# -  MyHashMap() initializes the object with an empty map.
# -  void put(int key, int value) inserts a (key, value) pair into the HashMap. If the key already exists in the map, update the corresponding value.
# -  int get(int key) returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
# -  void remove(key) removes the key and its corresponding value if the map contains the mapping for the key.

class MyHashMap(object):

    def __init__(self):
        self.keys = []
        self.values = []

    def put(self, key, value):
        if self.contains(key):
            self.values[self.index(key)] = value
        else:
            self.keys.append(key)
            self.values.append(value)
        
    def get(self, key):
        if not self.contains(key):
            return -1 

        return self.values[self.index(key)]
        

    def remove(self, key):
        if self.contains(key):
            i = self.index(key)
            
            self.keys.pop(i)
            self.values.pop(i)
    
    def contains(self, key):
        return key in self.keys
        
    def index(self, key):
        return self.keys.index(key)
