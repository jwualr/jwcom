#This program was created without the use of Artifical Intelligence
"""
The purpose of this program is to supply functions
for common functions in practice posts, to speed things up.
This program will be modified throughout the year to adapt to any new common techniques.
The main goal is to allow for fast menu creation, and give program title blocks a variable.
"""

def callBlock(split_length, block_name): # returns 2 values, for string splits and code block.
	strSpl = "="*split_length
	block_name = f"{strSpl}\n{block_name.upper()}\n{strSpl}"
	return strSpl, block_name

def intInp(msg = ""):
	while True:
		try:
			usIn = int(input(msg))
		except ValueError:
			print("\nPlease enter a valid integer.\n")
		else:
			return usIn

class EZMenu:
	"""
	This class makes it faster to create and manage input for simple output-based menus.
	Initiation requires an integer to create a tuple based on a range starting at 1 and ending with the integer.
	printLs requires a list of strings as an argument, printing a numbered version of that list.
	"""
	def __init__(self, list_len):
		self.set = tuple(range(1,list_len))
	def printLs(self, ls):
		itr = 0
		if len(self.set) > len(ls):
			raise TypeError(f"List must be of same size as {self}.set.")
		for i in self.set:
			print(f"{i}. {ls[itr]}")
			itr += 1
	def inp(self, msg):
		while True:
			try:
				usIn = int(input(f"{msg}"))
				if usIn > self.set[-1] or usIn < self.set[0]:
					raise ValueError
			except ValueError:
				print("\nPlease enter a valid integer.\n")
			else:
				return usIn

