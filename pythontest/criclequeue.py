class  criclequeue:

	def __init__(self):
		self._MAX = 10
		self._QUEUE = [0,0,0,0,0,0,0,0,0,0]
		self._COUNT = 0

	def writeinqueue(self, num):
		current = self._COUNT % self._MAX
		self._COUNT+=1
		self._QUEUE[current] = num

	def getqueue(self):
		return self._QUEUE

cq = criclequeue()
i = 0
while i < 13:
	cq.writeinqueue(i)
	i += 1 
print cq.getqueue()