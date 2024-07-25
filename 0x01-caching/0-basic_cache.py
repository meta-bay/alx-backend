#!/usr/bin/env python3
'''
basic caching module
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
        '''puts the key and value in the dictionary'''
        if key is None or item is None:
            pass
        else:
            self.cache_data[key] = item

    def get(self, key):
        '''retreives the value'''
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
