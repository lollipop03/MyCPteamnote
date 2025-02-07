'''PBDS'''

import bisect

class PBDS:
    def __init__(self, iterable=None):
        self._data = []
        if iterable:
            for item in iterable:
                self.insert(item)

    def insert(self, item):
        idx = bisect.bisect_left(self._data, item)
        self._data.insert(idx, item)

    def delete(self, item):
        idx = bisect.bisect_left(self._data, item)
        if idx < len(self._data) and self._data[idx] == item:
            self._data.pop(idx)

    def kth_element(self, k):
        if 0 <= k < len(self._data):
            return self._data[k]

    def order_of_key(self, key):
        return bisect.bisect_left(self._data, key)

    def __iter__(self):
        return iter(self._data)

    def __len__(self):
        return len(self._data)
