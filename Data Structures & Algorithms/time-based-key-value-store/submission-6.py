class TimeMap:

    def __init__(self):
        # key: list of [val, timestamp]
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = [] # if key not in store add it
        self.store[key].append([value, timestamp]) # add value and timestamp entry into list

    def get(self, key: str, timestamp: int) -> str:
        res = "" # result
        values = self.store.get(key, []) # get everything that matches key

        l, r = 0, len(values) - 1 # Binary Search
        while l<=r:
            m = (l+r) //2
            if values[m][1] <= timestamp: # if the timestamp is valid
                res = values[m][0] # add it
                l = m + 1 # check right
            else:
                r = m - 1 # check left
        return res

        
