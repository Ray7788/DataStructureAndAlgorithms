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

        # for i in range(self.hash_table_size):
        #     self.hashtable = [cell()] * self.hash_table_size
        self.hashtable = [None] * self.hash_table_size
        self.load_factor = 0.45

                
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

    def lastPrime(self, n):
        n = n - 1
        while not self.isPrime(n):
            n = n - 1
        return n

    # Functions for rehashing the hash table
    def rehash(self):
        self.hash_table_size = self.nextPrime(self.hash_table_size * 2)   # size of next hash table  
        temp_hash_table = self.hashtable
        # initialise new hash table
        self.hashtable = [None] * self.hash_table_size
        self.insert_number = 0
        self.collision_count = 0
        for i in range(len(temp_hash_table)):
            self.insert(temp_hash_table[i])
        
    def hashFunction(self, value):
        hash_value = 0
        if self.mode < 4:
            cValue = 31 # Prime after 26 Upper case and 26 Lower case 
            for val in value:
                hash_value = ord(val) + cValue * hash_value
        else:
            # a simple summation
            for val in value:
                hash_value = hash_value * 31 + ord(val)
        return hash_value % self.hash_table_size

    # Provide smart choices for different mode 
    def openAddressing_LINEAR_PROBING(self, hash_value):
        # Jump to next position
        return (hash_value + 1) % self.hash_table_size

    def openAddressing_QUADRATIC_PROBING(self, hash_value, i):
        # Use quadratic probing of the form: (i^2 + i) / 2
        return (hash_value + (i**2)) % self.hash_table_size

    def openAddressing_DOUBLE_HASHING(self, hash_value, i):
        h1 = hash_value % self.hash_table_size
        h2 = hash_value % self.lastPrime(self.hash_table_size)
        hash_value = (h1 + h2 * i) % self.hash_table_size
        return hash_value
        
        #     char_count = 0
        #     # Both upper and lower case 26 + 26 + 1
        #     sizeASCII = 53 
        #     power_ASCII = 0
        #     for val in value:
        #         char_count = (char_count + (ord(val) - ord('a') + 1) * power_ASCII) % self.hash_table_size
        #         power_ASCII = (power_ASCII * sizeASCII) % self.hash_table_size
        #     return int(char_count)

    # code for inserting into hash table
    def insert(self, value):
        if (self.insert_number / self.hash_table_size) > self.load_factor:
            self.rehash()

        if value == None:
            return

        hash_value = self.hashFunction(value)

        # SEPARATE_CHAINING ---------------------------------------------------------------------------------------------------
        if self.mode == HashingModes.HASH_1_SEPARATE_CHAINING.value or self.mode == HashingModes.HASH_2_SEPARATE_CHAINING.value:
            pass
        
        # LINEAR_PROBING ------------------------------------------------------------------------------------------------------
        elif self.mode == HashingModes.HASH_1_LINEAR_PROBING.value or self.mode == HashingModes.HASH_2_LINEAR_PROBING.value:
            while (self.hashtable[hash_value] is not None) and (self.hashtable[hash_value] != value):
                # hash_value = self.openAddressing_LINEAR_PROBING(hash_value)
                hash_value =  (hash_value + 1) % self.hash_table_size
                self.collision_count += 1
            if self.hashtable[hash_value] is None:                    # If the slot is empty
                self.hashtable[hash_value] = value
                self.insert_number += 1
            if self.hashtable[hash_value] == value:   
                pass    # If the value aready exist, just ignore it

        # QUADRATIC_PROBING ------------------------------------------------------------------------------------------------------
        elif self.mode == HashingModes.HASH_1_QUADRATIC_PROBING.value or self.mode == HashingModes.HASH_2_QUADRATIC_PROBING.value:
            i = 1
            while (self.hashtable[hash_value] is not None) and (self.hashtable[hash_value] != value):
                hash_value = self.openAddressing_QUADRATIC_PROBING(hash_value, i)
                i += 1
                self.collision_count += 1
            if self.hashtable[hash_value] is None:                    # If the slot is empty
                self.hashtable[hash_value] = value
                self.insert_number += 1

        # DOUBLE_HASHING ------------------------------------------------------------------------------------------------------
        elif self.mode == HashingModes.HASH_1_DOUBLE_HASHING.value or self.mode == HashingModes.HASH_2_DOUBLE_HASHING.value:
            i = 1
            while (self.hashtable[hash_value] is not None) and (self.hashtable[hash_value] != value):
                hash_value = self.openAddressing_DOUBLE_HASHING(hash_value, i)
                i += 1
                self.collision_count += 1
            if self.hashtable[hash_value] is None:                    # If the slot is empty
                self.hashtable[hash_value] = value
                self.insert_number += 1

    def find(self, value):
        hash_value = self.hashFunction(value)
        ini_hash_value = hash_value # back up

        # SEPARATE_CHAINING ---------------------------------------------------------------------------------------------------
        if self.mode == HashingModes.HASH_1_SEPARATE_CHAINING.value or self.mode == HashingModes.HASH_2_SEPARATE_CHAINING.value:
            pass

        # if self.hashtable[hash_value] is None:   
        #     return False
        # elif self.hashtable[hash_value] == value:       # If the value aready exist, just ignore it
        #     return True

        # LINEAR_PROBING ------------------------------------------------------------------------------------------------------
        elif self.mode == HashingModes.HASH_1_LINEAR_PROBING.value or self.mode == HashingModes.HASH_2_LINEAR_PROBING.value:
            while (self.hashtable[hash_value] is not None) and (self.hashtable[hash_value] != value):
                # hash_value = self.openAddressing_LINEAR_PROBING(hash_value)
                hash_value =  (hash_value + 1) % self.hash_table_size

                if hash_value == ini_hash_value:
                    return False
            if self.hashtable[hash_value] is None:   
                return False
            elif self.hashtable[hash_value] == value:       # If the value aready exist, just ignore it
                return True

        # QUADRATIC_PROBING ------------------------------------------------------------------------------------------------------
        elif self.mode == HashingModes.HASH_1_QUADRATIC_PROBING.value or self.mode == HashingModes.HASH_2_QUADRATIC_PROBING.value:
            i = 1
            while (self.hashtable[hash_value] is not None) and (self.hashtable[hash_value] != value): 
                i += 1
                hash_value = self.openAddressing_QUADRATIC_PROBING(hash_value, i)
                if hash_value == ini_hash_value:
                    return False
            if self.hashtable[hash_value] is None:   
                return False
            elif self.hashtable[hash_value] == value:       # If the value aready exist, just ignore it
                return True

        # DOUBLE_HASHING ------------------------------------------------------------------------------------------------------
        elif self.mode == HashingModes.HASH_1_DOUBLE_HASHING.value or self.mode == HashingModes.HASH_2_DOUBLE_HASHING.value:
            i = 1
            while (self.hashtable[hash_value] is not None) and (self.hashtable[hash_value] != value):
                i += 1
                hash_value = self.openAddressing_DOUBLE_HASHING(hash_value, i)
                if hash_value == ini_hash_value:
                   return False
            if self.hashtable[hash_value] is None:   
                return False
            elif self.hashtable[hash_value] == value:       # If the value aready exist, just ignore it
                return True

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
        self.state = 0 # state attribute 0 
        self.word = "" #  string word looking for 

    # getter & setter
    def get_state(self):
        return self.state

    def set_state(self, num):
        self.state = num

    def get_word(self):
        return self.word

    def set_word(self, word):
        self.word = word
        
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
