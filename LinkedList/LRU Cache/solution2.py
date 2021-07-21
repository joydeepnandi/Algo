from collections import OrderedDict

class LRUCache:

    def __init__(self, maxSize):
        self.cache=OrderedDict()
        self.maxSize = maxSize or 1

    def insertKeyValuePair(self, key, value):

        # Write your code here.

        self.cache[key]=value

        self.cache.move_to_end(key)

        if len(self.cache)>self.maxSize:

            self.cache.popitem(last=False)

            

    def getValueFromKey(self, key):
      # Write your code here.

        if key not in self.cache:

            return None

        self.cache.move_to_end(key)

        return self.cache[key]


    def getMostRecentKey(self):

        # Write your code here.

        return next(reversed(self.cache))
