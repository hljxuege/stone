import os 
with open('color.txt') as f:
	for line in f:
		words = filter(lambda x: x, line.rstrip().split(' '))
		_buf = "('%s', '%s'),#%s"%( words[0], ' '.join(words[1: -1]), words[-1])
		print _buf
		
		
		
