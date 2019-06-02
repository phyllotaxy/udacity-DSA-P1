from collections import OrderedDict

class LRU_Cache():

    def __init__(self, capacity):
        # Initialize class variables.
        self.ord_hmap = OrderedDict()
        # For the current problem, capacity is expected to be 5.
        self.ord_hmap_cap = capacity

    def get(self, key):
        # In case of a cache miss, get() should return -1.
        res = self.ord_hmap.get(key, -1)
        # If a cache hit happens, this counts as a most recent use. In this case,
        # we delete that entry from the hash map and add it again, so that the
        # least-recently-used order is preserved.
        if res != -1:
            value = self.ord_hmap.pop(key)
            self.ord_hmap[key] = value
        return res

    def set(self, key, value):
        # If the key is not yet in the hash map and the hash map is already full,
        # pop out the first item, as that one is the least recently used.
        if self.ord_hmap.get(key, -1) == -1 and len(self.ord_hmap) >= self.ord_hmap_cap:
            self.ord_hmap.popitem(last=False)
        # Insert the key/value pair.
        self.ord_hmap[key] = value

def main():
    tc_1()
    tc_2()
    tc_3()

# tests
def tc_1():
    our_cache = LRU_Cache(5)
    # empty cache
    print(our_cache.get(1))     # returns -1

def tc_2():
    our_cache = LRU_Cache(5)
    our_cache.set('apple', 2)
    our_cache.set('pear', 3)
    our_cache.set('orange', 5)
    our_cache.set('banana', 7)
    our_cache.set('grape', 11)
    # Cache is full.
    print(our_cache.get('apple'))   # returns 2
    our_cache.set('mango', 13)
    # As 'apple' was last queried, it became the most recently used, whereas
    # 'pear' became the least recently used, and will be deleted when adding 'mango'.
    print(our_cache.get('apple'))   # returns 2
    print(our_cache.get('pear'))    # returns -1

def tc_3():
    our_cache = LRU_Cache(5)
    our_cache.set(2, 'apple')
    our_cache.set(3, 'pear')
    our_cache.set(5, 'orange')
    our_cache.set(7, 'banana')
    our_cache.set(11, 'grape')
    # Cache is full.
    print(our_cache.get(2))     # returns apple
    print(our_cache.get(11))    # returns grape
    print(our_cache.get(3))     # returns pear
    print(our_cache.get(7))     # returns banana
    # 5 is now the least recently used.
    our_cache.set(13, 'mango')
    # 5 is deleted.
    print(our_cache.get(5))     # returns -1
    # All others are preserved
    print(our_cache.get(2))     # returns apple
    print(our_cache.get(3))     # returns pear
    print(our_cache.get(7))     # returns banana
    print(our_cache.get(11))    # returns grape
    print(our_cache.get(13))     # returns mango

if __name__ == '__main__':
    main()
