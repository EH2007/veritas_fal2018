class Stack:
  def __init__(self):
    self.items = []

  def push(self, item):
    self.items.append(item)

  def pop(self):
    self.items.pop()
  
  def size(self):
    return len(self.items)
  
  def isEmpty(self):
    return len(self.items) == 0

  def peek(self):
    return self.items[len(self.items) - 1]


s = Stack()
s.push(4)
s.push(20394812)
s.push("Sldkf")
s.push(2234.123487)
s.push(True)
s.pop()
print(s.isEmpty())
print(s.size())
print(s.peek())
print(s.items)