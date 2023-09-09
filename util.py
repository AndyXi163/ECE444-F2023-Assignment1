class utils:
	def __init__(self):
		self.output = 0;
		
	def reversed(self, input):
		if (isinstance(input, str) or isinstance(input, float)): return -1;

		while (input > 0):
			self.output = self.output * 10;
			self.output += (input % 10);
			input = input // 10;
##		self.output = self.output // 10;
		return self.output;
		
	def formatter(self, input):
		if (isinstance(input, str) or isinstance(input, float)): return -1, -1;
	
		return bin(input), oct(input);
			
