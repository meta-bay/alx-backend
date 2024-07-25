#!/usr/bin/env python3
'''
LIFO caching module
'''
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    '''
    LIFO caching class
    '''
    def __init__(self):
        """Initialize"""
        super().__init__()
        self.key_order = []

    def put(self, key, item):
        '''creates dictionary in LIFO algorithm'''
        if key is None or item is None:
            pass
        else:
            length = len(self.cache_data)
            if length >= BaseCaching.MAX_ITEMS and key not in self.cache_data:
                print("DISCARD: {}".format(self.key_order[-1]))
                del self.cache_data[self.key_order[-1]]
                del self.key_order[-1]
            self.key_order.append(key)
            self.cache_data[key] = item

    def get(self, key):
        '''retreives the dictionary by key'''
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
