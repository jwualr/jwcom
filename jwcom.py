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

def intInp(msg = "", min_val = 0, max_val = 0):
	"""
	prints an input prompt using msg, then validates that this is an integer.
	optional paramters min_val and max_val are self explanatory.
	if these parameters are the same, then min and max won't be checked.
	"""
	while True:
		try:
			usIn = int(input(msg))
			if max_val < min_val:
				if usIn < min_val:
					raise ValueError
				else:
					return usIn
			if (min_val != max_val) and (usIn < min_val or usIn > max_val):
				raise ValueError
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
	def __init__(self, new_list):
		self.set = []
		for idx, i in enumerate(new_list):
			self.set.append(f"{idx+1}. {i}")
		self.set = tuple(self.set)
	def __str__(self):
		new_str = ""
		for i in self.set:
			new_str += i
			if int(i[0]) < len(self.set):
				new_str += '\n'
		return new_str
	def __len__(self):
		return len(self.set)
	def inp(self, msg):
		while True:
			try:
				usIn = int(input(f"{msg}"))
				if usIn > len(self.set) or usIn < 1:
					raise ValueError
			except ValueError:
				print("\nPlease enter a valid integer.\n")
			else:
				return usIn

class EZRMenu:
	"""
	takes in an object of type EZMenu.
	EZRMenu.run(defList) will run a list of functions corresponding to options of EZMenu.
	By default, instead of running the command at index -1, the loop will end.
	If lastExit is set to False, however, it will exit when a function run returns any from a list of words.
	However, as of right now it's implemented poorly and isn't recommended.
	"""
	def __init__(self, ezMen):
		if not isinstance(ezMen, EZMenu):
			raise TypeError("When initialzing EZRMenu, ezMen must be of type EZMenu")
		self.menYou = ezMen
	def run(self, defList, title = None, prompt = 'choose: ', lastExit = True):
		if not len(defList) == len(self.menYou):
			raise ValueError("defList must be of same length as menYou")
		if title:
			strSpl, clBl = callBlock(42, title)
		while True:
			if title:
				print(clBl)
			print(self.menYou)
			usIn = self.menYou.inp(prompt)
			if lastExit and usIn == len(defList):
				return
			elif defList[usIn-1] in {'exit', 'quit', 'leave', 'stop'}:
				return
			defList[usIn-1]()
