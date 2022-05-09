class HTable(object):
    def __init__(self, length=100):
        # Initiate our array with empty values.
        self.array = [None] * length

    def hash(self, key):
        """Get the index of our array for a specific string key"""
        length = len(self.array)
        return hash(key) % length

    def add(self, key, value):
        """Add a value to our array by its key"""
        index = self.hash(key)
        if self.array[index] is not None:
            # This index already contain some values.
            # This means that this add MIGHT be an update
            # to a key that already exist. Instead of just storing
            # the value we have to first look if the key exist.
            for kvp in self.array[index]:
                # If key is found, then update
                # its current value to the new value.
                if kvp[0] == key:
                    kvp[1] = value
                    break
            else:
                # If no breaks was hit in the for loop, it
                # means that no existing key was found,
                # so we can simply just add it to the end.
                self.array[index].append([key, value])
        else:
            # This index is empty. We should initiate
            # a list and append our key-value-pair to it.
            self.array[index] = []
            self.array[index].append([key, value])

    def get(self, key):
        """Get a value by key"""
        index = self.hash(key)
        if self.array[index] is None:
            raise KeyError()
        else:
            # Loop through all key-value-pairs
            # and find if our key exist. If it does
            # then return its value.
            for kvp in self.array[index]:
                if kvp[0] == key:
                    return kvp[1]

            # If no return was done during loop,
            # it means key didn't exist.
            raise KeyError()

    def is_full(self):
        """Determines if the HashTable is too populated."""
        items = 0
        # Count how many indexes in our array
        # that is populated with values.
        for item in self.array:
            if item is not None:
                items += 1
        # Return bool value based on if the
        # amount of populated items are more
        # than half the length of the list.
        return items > len(self.array)/2

    def double(self):
        """Double the list length and re-add values"""
        ht2 = HTable(length=len(self.array)*2)
        for i in range(len(self.array)):
            if self.array[i] is None:
                continue

            # Since our list is now a different length,
            # we need to re-add all of our values to
            # the new list for its hash to return correct
            # index.
            for kvp in self.array[i]:
                ht2.add(kvp[0], kvp[1])

        # Finally we just replace our current list with
        # the new list of values that we created in ht2.
        self.array = ht2.array

    def __setitem__(self, key, value):
        self.add(key, value)

    def __getitem__(self, key):
        return self.get(key)
