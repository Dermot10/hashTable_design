# Example of hashTable data structure, with chaining for collision handling
class HashTable:
    def __init__(self): 
        self.bucketSize = 10
        self.buckets = [[] for i in range(self.bucketSize)]

#Unambigious representation of HashTable 
    def __repr__(self):
        print(self.buckets) 

#funciton to get hash value of the key
    def get_hash(self, key): 
        h = 0 
        for i in key: h += ord(i)
        return h % self.bucketSize
                
#Data encapsulation, getter method to access the data members
    def __getitem__(self, key): 
        h = self.get_hash(key)
        for element in self.buckets[h]: 
            if element[0] == key: return element[1]


#Data encapsulation, setter method to modify the data members 
#Validation logic to set key and value to the hashTable buckets.  
    def __setitem__(self, key, element): 
        h = self.get_hash(key)
        found = False
        for index, element in enumerate(self.buckets[h]):
             if len(element) == 2 and element[0] == key: 
                 self.buckets[index][h] = (key, element)
                 found = True 
                 break 
        if not found: 
            self.buckets[h].append((key, element))
    
#Method to delete the element found at the indicated index
    def __delitem__(self, key): 
        h = self.get_hash(key)
        for index, element in enumerate(self.buckets[h]):
            if element[0] == key: 
                del self.buckets[h][index]
    

cars = HashTable()
cars.__repr__()
cars.get_hash("lambo")
cars.__setitem__("lambo", "yellow")
cars.__setitem__("mercedes", "black")
cars.__setitem__("BMW", "black")
cars.__setitem__("Audi", "white")
cars.__setitem__("Ferrari", "Red")
cars.__repr__()
print("")
print(cars.__getitem__("Audi"))
cars.__delitem__("Audi")
cars.__repr__()


