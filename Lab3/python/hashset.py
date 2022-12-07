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
        self.hash_table_size = self.insert_number * 2   # size of next hash table  
        temp_hash_table = self.hashtable
        # initialise new hash table
        self.hashtable = [None] * self.hash_table_size
        self.insert_number = 0
        self.collision_count = 0
        for i in range(len(temp_hash_table)):
            self.insert(temp_hash_table[i])
        
    def hashFunction(self, value):
        hash_value = 0
        if self.mode <= 3:
            cValue = 51 # Prime after 26 Upper case and 26 Lower case 
            for val in value:
                hash_value = ord(val) + cValue * hash_value
        else:
            # a simple summation
            for val in value:
                hash_value += ord(val)
        return hash_value % self.hash_table_size

    # Provide smaert choices for different mode 
    def openAddressing(self, mode, hash_value, i):
        if mode == 00: # Jump to next position
            return (hash_value + 1) % self.hash_table_size    
        if mode == 11: # Use quadratic probing of the form: (i^2 + i) / 2
            hash_value = (hash_value + (i**2 + i) / 2 ) % self.hash_table_size
            return hash_value
        if mode == 22:  
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

        # else:
        #     char_count = 0
        #     for val in value:
        #         char_count += ord(val)
        #     length = len(str(char_count))
        #     if length > 3:
        #         mid_int = 100 * int((str(char_count)[length // 2 - 1])) \
        #                   + 10 * int((str(char_count)[length // 2])) \
        #                   + 1 * int((str(char_count)[length // 2 + 1]))
        #     else:
        #         mid_int = char_count
        #     return mid_int % self.hash_table_size

    # code for inserting into hash table
    def insert(self, value):
        if (self.insert_number / self.hash_table_size) > self.load_factor:
            self.rehash()

        hash_value = self.hashFunction(value)

        # SEPARATE_CHAINING ---------------------------------------------------------------------------------------------------
        if self.mode == HashingModes.HASH_1_SEPARATE_CHAINING.value or self.mode == HashingModes.HASH_2_SEPARATE_CHAINING.value:
            print("d")
        
        # elif self.hashtable[hash_value] is None:    pass
        elif self.hashtable[hash_value] == value:   pass    # If the value aready exist, just ignore it
        # LINEAR_PROBING ------------------------------------------------------------------------------------------------------
        elif self.mode == HashingModes.HASH_1_LINEAR_PROBING.value or self.mode == HashingModes.HASH_2_LINEAR_PROBING.value:
            while (self.hashtable[hash_value] is not None) and (self.hashtable[hash_value] != value):
                hash_value = self.openAddressing(00, hash_value)
                self.collision_count += 1
            if self.hashtable[hash_value] is None:                    # If the slot is empty
                self.hashtable[hash_value] = value
                self.insert_number += 1

        # QUADRATIC_PROBING ------------------------------------------------------------------------------------------------------
        elif self.mode == HashingModes.HASH_1_QUADRATIC_PROBING.value or self.mode == HashingModes.HASH_2_QUADRATIC_PROBING.value:
            i = 1
            while (self.hashtable[hash_value] is not None) and (self.hashtable[hash_value] != value):
                hash_value = self.openAddressing(11, hash_value, i)
                i += 1
                self.collision_count += 1
            if self.hashtable[hash_value] is None:                    # If the slot is empty
                self.hashtable[hash_value] = value
                self.insert_number += 1

        # DOUBLE_HASHING ------------------------------------------------------------------------------------------------------
        elif self.mode == HashingModes.HASH_1_DOUBLE_HASHING.value or self.mode == HashingModes.HASH_2_DOUBLE_HASHING.value:
            i = 1
            while (self.hashtable[hash_value] is not None) and (self.hashtable[hash_value] != value):
                hash_value = self.openAddressing(22, hash_value, i)
                i += 1
                self.collision_count += 1
            if self.hashtable[hash_value] is None:                    # If the slot is empty
                self.hashtable[hash_value] = value
                self.insert_number += 1

                

    def find(self, value):
        hash_value = self.hashFunc(value)
        ini_hash_value = hash_value

        # SEPARATE_CHAINING ---------------------------------------------------------------------------------------------------
        if self.mode == HashingModes.HASH_1_SEPARATE_CHAINING.value or self.mode == HashingModes.HASH_2_SEPARATE_CHAINING.value:
            print("d")

        elif self.hashtable[hash_value] is None:   
            return False
        elif self.hashtable[hash_value] == value:       # If the value aready exist, just ignore it
            return True

        # LINEAR_PROBING ------------------------------------------------------------------------------------------------------
        elif self.mode == HashingModes.HASH_1_LINEAR_PROBING.value or self.mode == HashingModes.HASH_2_LINEAR_PROBING.value:
            while (self.hashtable[hash_value] is not None) and (self.hashtable[hash_value] != value):
                hash_value = self.openAddressing(00, hash_value)
                if hash_value == ini_hash_value:
                    return False


        # QUADRATIC_PROBING ------------------------------------------------------------------------------------------------------
        elif self.mode == HashingModes.HASH_1_QUADRATIC_PROBING.value or self.mode == HashingModes.HASH_2_QUADRATIC_PROBING.value:
            i = 1
            while (self.hashtable[hash_value] is not None) and (self.hashtable[hash_value] != value): 
                i += 1
                hash_value = self.openAddressing(11, hash_value, i)
                if hash_value == ini_hash_value:
                    return False

        # DOUBLE_HASHING ------------------------------------------------------------------------------------------------------
        elif self.mode == HashingModes.HASH_1_DOUBLE_HASHING.value or self.mode == HashingModes.HASH_2_DOUBLE_HASHING.value:
            i = 1
            while (self.hashtable[hash_value] is not None) and (self.hashtable[hash_value] != value):
                i += 1
                hash_value = self.openAddressing(22, hash_value, i)
                if hash_value == ini_hash_value:
                   return False


        if self.hashtable[hash_value] is None:
            return False
        elif self.hashtable[hash_value] == value:
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
