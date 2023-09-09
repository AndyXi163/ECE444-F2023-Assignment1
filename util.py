class utils:
	def __init__(self):
		self.output = 0;
		
	def reversed(self, input):
		while (input > 0):
			self.output += (input%10);
			self.output *= 10;
			input = input / 10;
		self.output = self.output/10;
		return self.output;
		
	def formatter(self, input):
		return int(input, base=2), int(input, base=8);
			
