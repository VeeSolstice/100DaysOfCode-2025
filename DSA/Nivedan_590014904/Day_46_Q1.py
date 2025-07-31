class queue:
    def __init__(self):
        self.data = []
    def enqueue(self,data):
        self.data.append(data)
    def dequeue(self):
        if self.data:
            return self.data.pop(0)
    def display(self):
        print("Queue:", self.data)
    def size(self):
        return len(self.data)
    def is_empty(self):
        if self.data == []:
            return True
        else:
            return False
q = queue()
n = int(input("Enter the number of elements: "))
for i in range(n):
    val = int(input(f"Enter the {i+1} element: "))
    q.enqueue(val)
minimum =None
for j in range(q.size()):
    ele = q.dequeue()
    if minimum is None or ele < minimum  :
        minimum = ele
    q.enqueue(ele)
print(minimum)
q.display()
