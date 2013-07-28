class Skittle(object):
	"""A Skittle object has a color to describe it."""
	def __init__(self, color):
	self.color = color

class Bag(object):
	"""A Bag is a collection of skittles. All bags share the number
	of Bags ever made (sold) and each bag keeps track of its skittles
	in a list.
	"""
	number_sold = 0
	def __init__(self):
		self.skittles = ()
		Bag.number_sold += 1

	def tag_line(self):
		"""Print the Skittles tag line."""
		print("Taste the rainbow!")

	def print_bag(self):
		print(tuple(s.color for s in self.skittles))

	def take_skittle(self):
		"""Take the first skittle in the bag (from the front of the
		skittles list).
		"""
		skittle_to_eat = self.skittles[0]
		self.skittles = self.skittles[1:]
		return skittle_to_eat

	def add_skittle(self, s):
		"""Add a skittle to the bag."""
		self.skittles += (s,)

	def take_color(self, color):
		# indx = 0
		# for s in self.skittles:
		# 	if s.color == color:
		# 		self.skittles = self.skittles[0:indx] + self.skittles[indx+1:] 
		# 		return s
		# 	indx += 1
		# return None

		for i in range(len(self.skittles)):
			if self.skittles[i].color == color:
				self.skittles = self.skittles[:i] + self.skittles[i+1:] 
				return self.skittles[i]
		return None

	def take_all(self):
		for _ in range(len(self.skittles)):
			print (self.take_skittle().color)

class Email(object):
	"""Every email object has 3 instance variables: the message, the
	sender (their name), and the addressee (the destination’s name).
	"""
	def __init__(self, msg, sender, addressee):
		self.msg = msg
		self.sender = sender
		self.addressee = addressee

class Postman(object):
	"""Each Postman has an instance variable clients, which is a
	dictionary that associates client names with client objects.
	"""
	def __init__(self):
		self.clients = dict()

	def send(self, email):
		"""Take an email and put it in the inbox of the client it is
		addressed to."""
		client = self.clients[email.addressee] 
		client.receive(email)

	def register_client(self, client, client_name):
		"""Takes a client object and client_name and adds it to the
		clients instance variable.
		"""
		self.clients[client_name] = client

class Client(object):
	"""Every Client has instance variables name (which is used
	for addressing emails to the client), mailman (which is
	used to send emails out to other clients), and inbox (a
	list of all emails the client has received).
	"""
	def __init__(self, mailman, name):
		self.inbox = list()
		self.mailman = mailman
		self.name = name
		self.mailman.register_client(self, self.name)

	def compose(self, msg, recipient):
		"""Send an email with the given message msg to the given
		recipient."""
		email = Email(msg, self.name, recipient)
		self.mailman.send(email)

	def receive(self, email):
		"""Take an email and add it to the inbox of this client.
		"""
		self.inbox.append(email)

