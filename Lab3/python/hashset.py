from enum import Enum
import config

class hashset:
    def __init__(self):
        # TODO: create initial hash table
        self.verbose = config.verbose
        self.mode = config.mode
        self.hash_table_size = config.init_size
        self.collision_count = 0 # count number of collisions
        self.insert_number = 0 # count the current inserted values numbers
        self.hashtable = [None] * self.hash_table_size

                
    # Helper functions for finding prime numbers
    def isPrime(self, n):
        i = 2
        while (i * i <= n):
            if (n % i == 0):
                return False
            i = i + 1
        return True
        
    def nextPrime(self, n):
        while (not self.isPrime(n)):
            n = n + 1
        return n

    # Functions for rehashing the hash table
    def rehash(self):
        self.hash_table_size = self.insert_number * 2   # size of next hash table  
        temp_hash_table = self.hashtable[:]
        # initialise new hash table
        self.hashtable = [None] * self.hash_table_size
        for i in range(len(temp_hash_table)):
            self.hashtable[i] = temp_hash_table[i]
        
    # Provide smaert choices for different mode 
    def hashFunction(self, value):
        if self.mode <= 3 :
            char_count = 0
            # Both upper and lower case 26 + 26 + 1
            sizeASCII = 53 
            power_ASCII = 0
            for val in value:
                char_count = (char_count + (ord(val) - ord('a') + 1) * power_ASCII) % self.hash_table_size
                power_ASCII = (power_ASCII * sizeASCII) % self.hash_table_size
            return int(char_count)

        else:
            char_count = 0
            for val in value:
                char_count += ord(val)
            length = len(str(char_count))
            if length > 3:
                mid_int = 100 * int((str(char_count)[length // 2 - 1])) \
                          + 10 * int((str(char_count)[length // 2])) \
                          + 1 * int((str(char_count)[length // 2 + 1]))
            else:
                mid_int = char_count
            return mid_int % self.hash_table_size


    def insert(self, value):
        # code for inserting into  hash table

        print("Placeholder")
        
    def find(self, value):
        # TODO code for looking up in hash table
        print("Placeholder")
        
    def print_set(self):
        # TODO code for printing hash table
        print("Placeholder")
        
    def print_stats(self):
        # TODO code for printing statistics
        print("Placeholder")
        
# This is a cell structure assuming Open Addressing
# It should contain and element that is the key and a state which is empty, in_use or deleted
# You will need alternative data-structures for separate chaining
class cell:
    def __init__(self):
        pass
        
class state(Enum):
    empty = 0
    in_use = 1
    deleted = 2
        
# Hashing Modes
class HashingModes(Enum):
    HASH_1_LINEAR_PROBING=0
    HASH_1_QUADRATIC_PROBING=1
    HASH_1_DOUBLE_HASHING=2
    HASH_1_SEPARATE_CHAINING=3
    HASH_2_LINEAR_PROBING=4
    HASH_2_QUADRATIC_PROBING=5
    HASH_2_DOUBLE_HASHING=6
    HASH_2_SEPARATE_CHAINING=7
