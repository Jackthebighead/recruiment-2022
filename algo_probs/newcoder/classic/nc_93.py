# 题意：LRU设计

import sys
import collections
class Solution:
    def __init__(self,k):
            import collections
            self.dict = collections.OrderedDict()
            self.k = k
    def set(self,key,value):
        if key in self.dict:
            self.dict.pop(key)
            self.dict[key] = value
        else:
            if len(self.dict) == self.k:
                self.dict.popitem(last=True)
            self.dict[key] = value
    def get(self,key):
        if key not in self.dict: 
            return -1
        value = self.dict.pop(key)
        self.dict[key] = value
        return value