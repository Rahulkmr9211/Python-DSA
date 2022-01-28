# Create Node
# Create linked list
# Add node to linked list
# Print linked list

class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None

	def isListEmpty(self):
		if self.head is None:
			return True
		else:
			return False

	def listLength(self):
		#10->20->Deepu->None
		currentNode = self.head
		length = 0
		while currentNode.next is not None:
			length +=1
			currentNode = currentNode.next
		return length

	def insertHead(self,newNode):
		temporaryNode = self.head 
		self.head = newNode
		self.head.next = temporaryNode
		del temporaryNode

	def insertAt(self,newNode,position):
		if position<0 or position>self.listLength():
			print('Invalid position')
			return

		if position == 0:
			self.insertHead(newNode)
			return
		currentNode = self.head
		currentPosition = 0
		while True:
			if currentPosition == position:
				previousNode.next = newNode
				newNode.next = currentNode
				break
			previousNode = currentNode
			currentNode = currentNode.next
			currentPosition += 1


	def insertEnd(self,newNode):
		#None->Rahul
		if self.head is None:
			self.head = newNode
		else:
			#Rahul,None -> kajal,None->
			lastNode = self.head
			# print('a',lastNode.data)
			# print('a1',lastNode.next)
			while True:
				if lastNode.next is None:
					break
				lastNode = lastNode.next
			lastNode.next = newNode
			# print('b',lastNode.data)
			# print('c',lastNode.next.data)

	def deleteEnd(self):
		lastNode = self.head
		while lastNode.next is not None:
			previousNode = lastNode
			lastNode = lastNode.next
		previousNode.next = None

	def deleteHead(self):
		if self.isListEmpty() is False:
			previousHead = self.head
			self.head = self.head.next
			previousHead.next = None 
		else:
			print('Linked List is Empty')

	def deleteAt(self,position):
		#checking invalid position
		if position < 0 or position >= self.listLength():
			print('Invalid position')
			return
		
		if self.isListEmpty() is False:
			if position == 0:
				self.deleteHead()
				return

			currentNode = self.head 
			currentPosition = 0
			while True:
				if currentPosition == position:
					previousNode.next = currentNode.next
					currentNode.next = None
					break
				currentPosition += 1
				previousNode = currentNode
				currentNode = currentNode.next


	def printList(self):
		if self.head is None:
			print('List in Empty')
			return
		currentNode = self.head
		while True:
			if currentNode is None:
				break
			print(currentNode.data)
			currentNode = currentNode.next


firstNode = Node(10) 
linkedList = LinkedList()
linkedList.insertEnd(firstNode)
secondNode = Node(20)
linkedList.insertEnd(secondNode)
thirdNode = Node("Deepu")
linkedList.insertEnd(thirdNode)
linkedList.deleteAt(1)
# print('#########')
linkedList.printList()

