class Stack(object):

	def __init__(self):
		self.items = []

	def push(self, value):
		self.items.append(value)

	def pop(self):
		if(self.is_empty()):
			return None
		else:
			return self.items.pop()

	def seek(self):
		return self.items[-1]

	def is_empty(self):
		if not self.items:
			return True
		else:
			return False

	def printStack(self):
		print(self.items)



def operate():
	stack_length = int(input())
	stack_ops = map(int, input().split())

	mystack = Stack()

	for op in stack_ops:
		if op:
			mystack.push(op)
		else:
			# Its  a pop operation !
			if mystack.is_empty():
				print("Invalid")
				return
			else:
				mystack.pop()
	print("Valid")
	return

num_tests = int(input())

for i in range(num_tests):
	operate()