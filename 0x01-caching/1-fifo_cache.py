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

    def put(self, key, item):
        '''Creates dictionary in FIFO algorithm'''
        if key is None or item is None:
            pass
        else:
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                keys = []
                for key, _ in self.cache_data.items():
                    keys.append(key)
                print(f"DISCARD {keys[0]}")
                del self.cache_data[keys[0]]
                self.cache_data[key] = item

    def get(self, key):
        '''retreives the dictionary by key'''
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
