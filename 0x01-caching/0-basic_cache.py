#!/usr/bin/env python3
'''
basic cashing module
'''
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    '''
    Cashing system class
    '''
    def __init__(self):
        '''Initialize'''
        super().__init__()

    def put(self, key, item):
        if key is not None or item is not None:
            self.cache_data[key] = item

    def get(self, key):
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
