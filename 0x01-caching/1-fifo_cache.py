#!/usr/bin/env python3
'''
FIFO caching module
'''
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    '''FIFO caching system class'''
    def __init__(self):
        '''Initialize'''
        super().__init__()
        self.key_order = []

    def put(self, key, item):
        '''Creates dictionary in FIFO algorithm'''
        if key is None or item is None:
            pass
        else:
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                print(f"DISCARD {self.key_order[0]}")
                del self.cache_data[self.key_order[0]]
                del self.key_order[0]
            self.key_order.append(key)
            self.cache_data[key] = item

    def get(self, key):
        '''retreives the dictionary by key'''
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
