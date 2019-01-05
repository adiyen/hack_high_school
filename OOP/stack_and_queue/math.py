class numbers:
    def __init__(self):
        self.numbs = []

    def push(self, val):
        self.numbs.append(val)
    
    def total_count(self):
        return f"Total count = {len(self.numbs)}"

    def sum(self):
        storage = self.numbs.copy()
        self.sum = 0
        while storage:
            self.sum+=storage[-1]
            storage.pop()
        return f"Sum = {self.sum}"

        
    def multiply(self):
        storage = self.numbs.copy()
        product = 1
        while storage:
            product*=storage[-1]
            storage.pop()
        return f"Product = {product}"
    
    def mean(self):
        total = self.sum
        avg = total/len(self.numbs)
        return f"Mean = {int(avg)}"
    
    def min(self):
        storage = self.numbs.copy()
        min = storage[-1]
        for i in range(len(storage)-1):
            storage.pop()
            if storage[-1] < min:
                min = storage[-1]
        return f"Min = {min}"
        
    def max(self):
        storage = self.numbs.copy()
        max = storage[-1]
        for i in range(len(storage)-1):
            storage.pop()
            if storage[-1] > max:
                max = storage[-1]
        return f"Max = {max}"

numbers = numbers()

numb = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in range(10):
    numbers.push(numb[i])

print(numbers.total_count())
print(numbers.sum())
print(numbers.multiply())
print(numbers.mean())
print(numbers.min())
print(numbers.max())