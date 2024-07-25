#!/usr/bin/env python3
'''
LRU caching module
'''
from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    '''LRU caching system class'''
    def __init__(self):
        '''Initialize'''
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        '''Creates dictionary in LRU algorithm'''
        if key is None or item is None:
            return

        if key in self.cache_data:
            # Remove the old value to update the order
            self.cache_data.pop(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            # Pop the first item (least recently used)
            discarded_key, _ = self.cache_data.popitem(last=False)
            print(f"DISCARD: {discarded_key}")

        # Insert the item as the most recently used
        self.cache_data[key] = item

    def get(self, key):
        '''retreives the dictionary by key'''
        if key is None or key not in self.cache_data:
            return None

        # Move the accessed item to the end to mark it as most recently used
        value = self.cache_data.pop(key)
        self.cache_data[key] = value
        return value
