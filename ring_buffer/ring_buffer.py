class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []
        self.index = 0

    def append(self, item):
        if len(self.storage) < self.capacity: 
            # if below capacity add new item to end of list
            self.storage.append(item)
        # if at capacity should remove oldest and add new
        else:
            self.storage[self.index] = item
            self.index += 1
            if self.index == self.capacity:
                self.index = 0

    def get(self):
        return self.storage