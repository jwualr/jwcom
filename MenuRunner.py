from . import jwcom
class EZRMenu:
	"""
	This thing is a mess.
	It takes in an object of type EZMenu.
	EZRMenu.run(defList) will run a list of functions corresponding to options of EZMenu.
	By default, instead of running the command at index -1, the loop will end.
	If lastExit is set to False, however, it will exit when a function run returns any from a list of words.
	This is pretty much useless if your functions return anything or aren't editing some global.
	"""
	def __init__(self, ezMen):
		if not isinstance(ezMen, jwcom.EZMenu):
			raise TypeError("When initialzing EZRMenu, ezMen must be of type EZMenu")
		self.menYou = ezMen
	def run(self, defList, title = None, prompt = 'choose: ', lastExit = True):
		if not len(defList) == len(self.menYou):
			raise ValueError("defList must be of same length as menYou")
		if title:
			strSpl, clBl = jwcom.callBlock(42, title)
		while True:
			if title:
				print(clBl)
			print(self.menYou)
			usIn = self.menYou.inp(prompt)
			if lastExit and usIn == len(defList):
				return
			if isinstance(defList[usIn-1], (list, tuple)): #also possible: create dict with keys of function and args, with args corresponding to list of args? something similar.
				argLs = []
				for i in defList[usIn-1][1:-1]:
					argLs.append(i)
				defList[usIn-1][0](argLs)
			else:
					if defList[usIn-1]() in {'exit', 'quit', 'leave', 'stop'}: #what should be done if a function returns something?
						return
