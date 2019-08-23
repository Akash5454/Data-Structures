class Priority_Queue():
    def __init__(self):
        self.queue = []
    def isEmpty(self):
        return len(self.queue) == 0
    def insert(self,data):
        self.queue.append(data)
    def delete(self):
        try:
            max = 0
            for i in range(len(self.queue)):
                if self.queue[i] > self.queue[max]:
                    max =  i
            item = self.queue[max]
            del self.queue[max]
            return item
        except IndexError:
            print()
            exit()
    def __str__(self):
        return ' '.join([str(i) for i in self.queue])
