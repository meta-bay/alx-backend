#!/usr/bin/env python3
'''
LFU caching module
'''
from base_caching import BaseCaching
from collections import OrderedDict, defaultdict


class LFUCache(BaseCaching):
    '''LFU caching system class'''
    def __init__(self):
        """Initialize"""
        super().__init__()
        self.freq = defaultdict(int)
        self.freq_list = defaultdict(OrderedDict)

    def put(self, key, item):
        """Add an item in the cache in lfu algorithm"""
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            self.update_freq(key)
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                min_freq = min(self.freq_list)
                discarded_key, _ = self.freq_list[min_freq].popitem(last=False)
                print(f"DISCARD: {discarded_key}")
                del self.cache_data[discarded_key]
                del self.freq[discarded_key]

                if not self.freq_list[min_freq]:
                    del self.freq_list[min_freq]

            self.cache_data[key] = item
            self.freq[key] = 1
            self.freq_list[1][key] = item

    def get(self, key):
        """Get an item by key"""
        if key is None or key not in self.cache_data:
            return None

        self.update_freq(key)
        return self.cache_data[key]

    def update_freq(self, key):
        """Update the frequency of a key"""
        freq = self.freq[key]
        del self.freq_list[freq][key]

        if not self.freq_list[freq]:
            del self.freq_list[freq]

        self.freq[key] += 1
        new_freq = self.freq[key]
        self.freq_list[new_freq][key] = self.cache_data[key]
