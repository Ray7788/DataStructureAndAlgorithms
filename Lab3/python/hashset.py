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
        self.linked_hash_table = [SeparateChaining() for x in range(self.hash_table_size)]

                
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
        # store them in the new double sized array
        for i in range(len(temp_hash_table)):
            self.insert(temp_hash_table[i])
        
    def hashFunction(self, value):
        hash_value = 0
        if self.mode < 4:
            # BKDR
            seed = 53 # Prime after 26 Upper case and 26 Lower case 
            for val in value:
                hash_value = ord(val) + seed * hash_value
        else:
            # ELF
            for val in value:
                hash_value = (hash_value << 4) + ord(val)
                x = hash_value & 0xF0000000
                if (x != 0):
                    hash_value ^= (x >> 24)
                hash_value &= ~x
        return hash_value % self.hash_table_size

    # Provide smart choices for different mode 
    def openAddressing_LINEAR_PROBING(self, hash_value):
        # Jump to next position
        return (hash_value + 1) % self.hash_table_size

    def openAddressing_QUADRATIC_PROBING(self, hash_value, i):
        # Use quadratic probing of the form: (i^2 + i) / 2
        return (hash_value + (i**2)) % self.hash_table_size

    def openAddressing_DOUBLE_HASHING(self, hash_value, i):
        # use two variables
        h1 = hash_value % self.hash_table_size
        h2 = self.lastPrime(self.hash_table_size) - (hash_value % self.hash_table_size)
        hash_value = (h1 + h2 * i) % self.hash_table_size
        return hash_value

    # code for inserting into hash table
    def insert(self, value):
        if (self.insert_number / self.hash_table_size) > self.load_factor:
            self.rehash()

        if value == None:
            return

        hash_value = self.hashFunction(value)

        # SEPARATE_CHAINING ---------------------------------------------------------------------------------------------------
        if self.mode == HashingModes.HASH_1_SEPARATE_CHAINING.value or self.mode == HashingModes.HASH_2_SEPARATE_CHAINING.value:
            # If the value has been found in the linked list, then just return
            if self.find(value):
                return
            # else append the value
            else:
                self.linked_hash_table[hash_value].append(value)
                self.insert_number += 1
        
        # LINEAR_PROBING ------------------------------------------------------------------------------------------------------
        elif self.mode == HashingModes.HASH_1_LINEAR_PROBING.value or self.mode == HashingModes.HASH_2_LINEAR_PROBING.value:
            while (self.hashtable[hash_value] is not None) and (self.hashtable[hash_value] != value):
                hash_value = self.openAddressing_LINEAR_PROBING(hash_value)
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
            if self.hashtable[hash_value] == value:   
                pass    # If the value aready exist, just ignore it

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
            if self.hashtable[hash_value] == value:   
                pass    # If the value aready exist, just ignore it

    def find(self, value):
        hash_value = self.hashFunction(value)
        ini_hash_value = hash_value # back up

        # SEPARATE_CHAINING ---------------------------------------------------------------------------------------------------
        if self.mode == HashingModes.HASH_1_SEPARATE_CHAINING.value or self.mode == HashingModes.HASH_2_SEPARATE_CHAINING.value:
            return self.linked_hash_table[hash_value].find(value)

        # LINEAR_PROBING ------------------------------------------------------------------------------------------------------
        elif self.mode == HashingModes.HASH_1_LINEAR_PROBING.value or self.mode == HashingModes.HASH_2_LINEAR_PROBING.value:
            while (self.hashtable[hash_value] is not None) and (self.hashtable[hash_value] != value):
                hash_value = self.openAddressing_LINEAR_PROBING(hash_value)

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
                hash_value = self.openAddressing_QUADRATIC_PROBING(hash_value, i)
                i += 1
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
                hash_value = self.openAddressing_DOUBLE_HASHING(hash_value, i)
                i += 1
                if hash_value == ini_hash_value:
                   return False
            if self.hashtable[hash_value] is None:   
                return False
            elif self.hashtable[hash_value] == value:       # If the value aready exist, just ignore it
                return True

    def print_set(self):
        # Print the set if choose the separate chaining
        if self.mode == 3 or self.mode == 7:
            pass
            for i in range(len(self.linked_hash_table)):
                if self.linked_hash_table[i] is not None:
                    print(" " + self.linked_hash_table[i].__repr__())
        # Open method manner for printing
        else:
            print("Hashset is: ")
            for i in range(len(self.hashtable)):
                if self.hashtable[i] is not None:
                    print(" " + self.hashtable[i])
        
        
    def print_stats(self):
        if self.verbose == 0:
            return
        elif self.verbose == 1:
            print("The number of collision is: " + str(self.collision_count))
        elif self.verbose == 2:
            print("The number of collision is: " + str(self.collision_count))
            print("The average number of collision per insert is: " + str(self.collision_count / self.insert_number))
        elif self.verbose == 3:
            print("The number of collision is: " + str(self.collision_count))
            print("The average number of collision per insert is: " + str(self.collision_count / self.insert_number))
            print("The size of the hashtable is: " + str(self.hash_table_size))
        elif self.verbose == 4:
            print("The number of collision is: " + str(self.collision_count))
            print("The average number of collision per insert is: " + str(self.collision_count / self.insert_number))
            print("The size of the hashtable is: " + str(self.hash_table_size))
            print("The number of values inserted is: " + str(self.insert_number))
        
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
        
# An extra class used to implement separate chaining
class SeparateChaining:
    class Node:
        def __init__(self, item):
            self.item = item
            self.next = None

        def __str__(self):
            return str(self.item)

    # The iterable linked list class
    class LinkedListGenerator:
        def __init__(self, node):
            self.node = node

        def __next__(self):
            if self.node:
                current_node = self.node
                self.node = current_node.next
                return current_node.item
            else:
                raise StopIteration

        def __iter__(self):
            return self

    def __init__(self, iterable=None):
        self.head = None
        self.tail = None
        if iterable:
            self.extend(iterable)

    # Append node
    def append(self, obje):
        node = SeparateChaining.Node(obje)
        if not self.head:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    # Find node
    def find(self, obje):
        for n in self:
            if n == obje:
                return True
        else:
            return False

    # Iterator the linked list
    def __iter__(self):
        return self.LinkedListGenerator(self.head)

    # print the link list
    def __repr__(self):
        return '<<' + ','.join(map(str, self)) + '>>'

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