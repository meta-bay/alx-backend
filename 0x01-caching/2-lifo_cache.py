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

    def put(self, key, item):
        '''creates dictionary in LIFO algorithm'''
        if key is not None or item is not None:
            self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            keys = []
            for k, _ in self.cache_data.items():
                keys.append(k)
            print(f"DISCARD {keys[-1]}")
            del self.cache_data[keys[-1]]

    def get(self, key):
        '''retreives the dictionary by key'''
        if key is None or key not in self.cache_data.items():
            return None
        return self.cache_data[key]
