#Example of hashTable data structure with collision handled by linear probing
class HashTable: 
    def __init__(self): 
        self.bucketSize = 5 
        self.buckets = [None for i in range(self.bucketSize)]

    def  __repr__(self): 
        return self.buckets

    def get_hash(self, key): 
        h = 0
        for i in key: h += ord(i)
        return h % self.bucketSize

    #__setter__ method used to validate input which modifies data members
    # Incrementing the location within the hashTable by one if collision occurs
    def __setitem__(self, key, value): 
        h = self.get_hash(key)
        while self.buckets[h] is not None: 
            print("Collision has occured")
            h = (h+1) % self.bucketSize
        self.buckets[h] = ((key, value))
    
    def __getitem__(self, key): 
        h = self.get_hash(key)
        for element in self.buckets[h]:
            if element == key: 
                return element
